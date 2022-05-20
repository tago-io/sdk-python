from typing import TypedDict

from tagoio_sdk.infrastructure.api_request import RequestParams, apiRequest
from tagoio_sdk.regions import Regions, getConnectionURI


class DoRequestParams(RequestParams):
    url: None


class GenericModuleParams(TypedDict):
    token: str
    region: Regions


class TagoIOModule(object):
    def __init__(self, params: GenericModuleParams) -> None:
        self.token = params.get("token")
        self.region = params.get("region")
        self.validateParams()
        pass

    def validateParams(self) -> None:
        if self.token is None:
            raise Exception("Token is invalid")
        pass

    def doRequest(self, params: DoRequestParams) -> dict[str, any]:
        url = getConnectionURI(self.region)["api"]
        return apiRequest({**params, "url": url, "headers": {"token": self.token}})

    @staticmethod
    def doRequestAnonymous(params: DoRequestParams, region: Regions) -> dict[str, any]:
        url = getConnectionURI(region)["api"]
        return apiRequest({**params, "url": url, "headers": {}})
