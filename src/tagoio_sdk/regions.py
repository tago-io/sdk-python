import os

from contextlib import suppress
from typing import Literal
from typing import Optional
from typing import TypedDict


class RegionDefinition(TypedDict):
    api: str
    realtime: str
    sse: str


# noRegionWarning = False

regionsDefinition = {
    "usa-1": {
        "api": "https://api.tago.io",
        "realtime": "wss://realtime.tago.io",
        "sse": "https://sse.tago.io/events",
    },
    "env": None,  # ? process object should be on trycatch.
}

Regions = Literal["usa-1", "env"]


def getConnectionURI(region: Optional[Regions]) -> RegionDefinition:
    value = None
    with suppress(KeyError):
        value = regionsDefinition[region]

    if value is not None:
        return value

    if region is not None and region != "env":
        raise Exception(f"> TagoIO-SDK: Invalid region {region}.")

    try:
        api = os.environ.get("TAGOIO_API")
        realtime = os.environ.get("TAGOIO_REALTIME")
        sse = os.environ.get("TAGOIO_SSE")

        if not api and region != "env":
            raise Exception("Invalid Env")

        return {"api": api, "realtime": realtime, "sse": sse}
    except Exception:
        # global noRegionWarning
        # if noRegionWarning is False:
        #     print("> TagoIO-SDK: No region or env defined, using fallback as usa-1.")
        #     noRegionWarning = True

        return regionsDefinition["usa-1"]
