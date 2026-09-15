from unittest.mock import patch

import pytest
import requests

from tagoio_sdk.infrastructure import api_sse


def fakeResponse(status):
    response = requests.Response()
    response.status_code = status
    return response


def testOpenSSEListeningUsesTimeoutAndRaisesOnErrorStatus():
    with patch.object(api_sse.requests, "get", return_value=fakeResponse(401)) as get:
        with pytest.raises(requests.HTTPError):
            api_sse.openSSEListening({"token": "t", "channel": "analysis_trigger"})

    kwargs = get.call_args.kwargs
    assert kwargs["stream"] is True
    assert kwargs["timeout"] == api_sse.SSE_REQUEST_TIMEOUT
    assert api_sse.SSE_REQUEST_TIMEOUT[1] > 15
