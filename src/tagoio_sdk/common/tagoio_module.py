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

    def _converter_dict_param_filter(self, params: dict) -> None:
        """
        Convert filter params to API format

        Args:
            params (dict): params to be converted
        """
        if params is None or not params.get("filter"):
            return
        filter_params = params["filter"]
        params.pop("filter")
        for key, value in filter_params.items():
            if isinstance(value, list):
                for i, item in enumerate(value):
                    for sub_key, sub_value in item.items():
                        converted_key = f"filter[{key}][{i}][{sub_key}]"
                        params[converted_key] = sub_value
            elif isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    converted_key = f"filter[{key}][{sub_key}]"
                    params[converted_key] = sub_value
            else:
                params[key] = value

    def doRequest(self, params: DoRequestParams) -> dict[str, any]:
        url = getConnectionURI(self.region)["api"]
        self._converter_dict_param_filter(params=params.get("params", {}))
        return apiRequest({**params, "url": url, "headers": {"token": self.token}})

    @staticmethod
    def doRequestAnonymous(params: DoRequestParams, region: Regions) -> dict[str, any]:
        url = getConnectionURI(region)["api"]
        return apiRequest({**params, "url": url, "headers": {}})
