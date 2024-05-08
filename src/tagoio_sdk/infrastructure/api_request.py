import json
import os
import platform
import time
from typing import Literal, Optional, TypedDict

import requests

from tagoio_sdk import __version__, config


class RequestParams(TypedDict):
    method: Literal["post", "get", "put", "delete"]
    url: str
    path: str
    headers: dict[str, str]
    body: Optional[any]
    params: Optional[any]
    headers: Optional[any]


class TagoIORequestError(Exception):
    """Exception raised for TagoIO API errors.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str = "Internal Error"):
        self.message = message
        super().__init__(self.message)


def getUserAgent() -> str:
    systemBanner = "(External; Python/{} {})".format(
        platform.python_version(), platform.platform()
    )
    banner = (
        "(Running at TagoIO)"
        if os.environ.get("T_ANALYSIS_CONTEXT") is not None
        else systemBanner
    )

    banner = "TagoIO-SDK|Python|{} {}".format(__version__, banner)
    return banner


class ResultHandlerResponse(TypedDict):
    data: Optional[any]
    error: Optional[str]


def resultHandler(req: requests.Response) -> ResultHandlerResponse:
    responseJson = req.json()

    if responseJson.get("status") is False or (
        req.status_code >= 400 and req.status_code < 500
    ):
        return {"error": responseJson.get("message")}

    return {"data": responseJson.get("result")}


def apiRequest(requestParams: RequestParams) -> dict[str, any]:
    sessionHTTP = requests.Session()
    sessionHTTP.headers.update(
        {
            **requestParams["headers"],
            "user-agent": getUserAgent(),
            "content-type": "application/json",
        }
    )

    url = "{}{}".format(requestParams["url"], requestParams["path"])
    dataBody = json.dumps(requestParams.get("body"), default=str)
    if dataBody == "null":
        dataBody = None

    def request() -> ResultHandlerResponse:
        return resultHandler(
            sessionHTTP.request(
                method=requestParams["method"],
                url=url,
                data=dataBody,
                params=requestParams.get("params"),
                timeout=config.tagoSDKconfig["requestTimeout"],
            )
        )

    result = None
    resulterror = None
    for _ in range(config.tagoSDKconfig["requestAttempts"]):
        try:
            resultBack = request()
            if resultBack.get("error") is not None:
                resulterror = resultBack.get("error")
            else:
                result = resultBack.get("data")
            break
        except Exception as e:
            resulterror = str(e.args[0].reason)
        time.sleep(1.5)

    if result is None:
        raise TagoIORequestError(resulterror)

    return result
