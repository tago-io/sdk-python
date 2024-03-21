from typing import Union
from urllib.parse import urlencode, urljoin
from sseclient import SSEClient
from tagoio_sdk.common.tagoio_module import GenericModuleParams
from tagoio_sdk.regions import getConnectionURI


class OpenSSEWithID(GenericModuleParams):
    def __init__(self, channel: str, resource_id: str):
        super().__init__()
        self.channel = channel
        self.resource_id = resource_id


class OpenSSEWithoutID(GenericModuleParams):
    def __init__(self, channel: str):
        super().__init__()
        self.channel = channel


OpenSSEConfig = Union[OpenSSEWithID, OpenSSEWithoutID]

channelsWithID = ["device_inspector", "analysis_console", "ui_dashboard"]
channelsWithoutID = ["notification", "analysis_trigger", "ui"]
channels = channelsWithID + channelsWithoutID


def isChannelWithID(params: OpenSSEConfig) -> bool:
    return params.channel in channelsWithID


def openSSEListening(params: OpenSSEConfig) -> SSEClient:
    base_url = getConnectionURI(params.region)["sse"]
    url = urljoin(base_url, "/events")

    query_params = {"token": params.token}
    if isChannelWithID(params):
        query_params["channel"] = f"{params.channel}.{params.resource_id}"
    else:
        query_params["channel"] = params.channel

    url += "?" + urlencode(query_params)

    return SSEClient(url)
