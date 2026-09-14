from types import SimpleNamespace
from unittest.mock import patch

import pytest
import requests

from tagoio_sdk.modules.Analysis import Analysis as analysis_module
from tagoio_sdk.modules.Analysis.Analysis import Analysis


ANALYSIS_INFO = {"name": "post-processor", "run_on": "external"}


class FakeStream:
    def __init__(self, script):
        self.script = script

    def events(self):
        for item in self.script:
            if isinstance(item, BaseException):
                raise item
            yield SimpleNamespace(data=item)


def httpError(status):
    response = requests.Response()
    response.status_code = status
    return requests.HTTPError(response=response)


def runListener(streams, sleep):
    handled = []

    def fakeOpen(_params):
        item = streams.pop(0)
        if isinstance(item, BaseException):
            raise item
        return item

    with (
        patch.object(Analysis, "doRequest", return_value=ANALYSIS_INFO),
        patch.object(analysis_module, "openSSEListening", side_effect=fakeOpen),
        patch.object(analysis_module.time, "sleep", side_effect=sleep),
        patch.object(
            Analysis, "_runLocal", side_effect=lambda *args: handled.append(args)
        ),
    ):
        Analysis({"token": "abcde12345"}).init(lambda context, scope: None)

    return handled


def testReconnectsAfterStreamDrop():
    sleeps = []
    trigger = '{"payload": {"analysis_id": "a1", "environment": [], "data": [1]}}'
    streams = [
        FakeStream([requests.ConnectionError("reset by peer")]),
        FakeStream([trigger, KeyboardInterrupt()]),
    ]

    handled = runListener(streams, sleeps.append)

    assert len(handled) == 1
    assert handled[0][1] == [1]
    assert sleeps == [analysis_module.SSE_RECONNECT_BASE_DELAY]


def testBackoffGrowsAndResetsAfterSuccessfulConnect():
    sleeps = []
    streams = [
        requests.ConnectionError("refused"),
        requests.ConnectionError("refused"),
        requests.ConnectionError("refused"),
        FakeStream([requests.ConnectionError("reset")]),
        requests.ConnectionError("refused"),
        FakeStream([KeyboardInterrupt()]),
    ]

    runListener(streams, sleeps.append)

    base = analysis_module.SSE_RECONNECT_BASE_DELAY
    assert sleeps == [base, base * 2, base * 4, base, base * 2]


def testBackoffIsCapped():
    sleeps = []
    streams = [requests.ConnectionError("refused")] * 12 + [
        FakeStream([KeyboardInterrupt()])
    ]

    runListener(streams, sleeps.append)

    assert max(sleeps) == analysis_module.SSE_RECONNECT_MAX_DELAY
    assert sleeps[-1] == analysis_module.SSE_RECONNECT_MAX_DELAY


def testRetriesOnServerError():
    sleeps = []
    streams = [httpError(502), FakeStream([KeyboardInterrupt()])]

    runListener(streams, sleeps.append)

    assert len(sleeps) == 1


def testAuthErrorStopsWithNonZeroExit():
    sleeps = []
    streams = [FakeStream([KeyboardInterrupt()]), httpError(401)]

    with pytest.raises(SystemExit) as exc:
        runListener([httpError(401)], sleeps.append)

    assert exc.value.code == 1
    assert sleeps == []
    assert len(streams) == 2


def testKeyboardInterruptDuringBackoffStopsCleanly():
    def interrupt(_delay):
        raise KeyboardInterrupt()

    streams = [requests.ConnectionError("refused"), FakeStream([])]

    runListener(streams, interrupt)

    assert len(streams) == 1
