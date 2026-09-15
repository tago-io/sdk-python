from typing import Literal
from typing import Union
from urllib.parse import urlencode
from urllib.parse import urljoin

import requests

from sseclient import SSEClient

from tagoio_sdk.common.tagoio_module import GenericModuleParams
from tagoio_sdk.regions import getConnectionURI


channelsWithID = ["device_inspector", "analysis_console", "ui_dashboard"]
channelsWithoutID = ["notification", "analysis_trigger", "ui"]
channels = channelsWithID + channelsWithoutID

# ? (connect, read) seconds. The server emits a keep-alive comment every 5s, so a
# ? read that stays silent this long means the connection is dead.
SSE_REQUEST_TIMEOUT = (10, 60)


class OpenSSEWithID(GenericModuleParams):
    channel: Literal["device_inspector", "analysis_console", "ui_dashboard"]
    resources_id: str


class OpenSSEWithoutID(GenericModuleParams):
    channel: Literal["notification", "analysis_trigger", "ui"]


OpenSSEConfig = Union[OpenSSEWithID, OpenSSEWithoutID]


def isChannelWithID(params: OpenSSEConfig) -> bool:
    return params.get("channel") in channelsWithID


def openSSEListening(params: OpenSSEConfig) -> SSEClient:
    base_url = getConnectionURI(params.get("region"))["sse"]
    url = urljoin(base_url, "/events")

    query_params = {}
    if isChannelWithID(params):
        query_params["channel"] = (
            f"{params.get('channel')}.{params.get('resources_id')}"
        )
    else:
        query_params["channel"] = params.get("channel")

    query_params["token"] = params.get("token")

    url += "?" + urlencode(query_params)

    response = requests.get(
        url,
        stream=True,
        headers={"Accept": "text/event-stream"},
        timeout=SSE_REQUEST_TIMEOUT,
    )
    response.raise_for_status()

    return SSEClient(response)
