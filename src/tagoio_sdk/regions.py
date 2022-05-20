import os
from contextlib import suppress
from typing import Literal, TypedDict


class RegionDefinition(TypedDict):
    api: str
    realtime: str


noRegionWarning = False

regionsDefinition = {
    "usa-1": {"api": "https://api.tago.io", "realtime": "wss://realtime.tago.io"},
    "env": None,  # ? process object should be on trycatch.
}

Regions = Literal["usa-1", "env"]


def getConnectionURI(region: Regions) -> RegionDefinition:
    value = None
    with suppress(KeyError):
        value = regionsDefinition[region]

    if value is not None:
        return value

    if region is not None and region != "env":
        raise Exception("> TagoIO-SDK: Invalid region {}.".format(region))

    try:
        api = os.environ.get("TAGOIO_API") or ""
        realtime = os.environ.get("TAGOIO_REALTIME") or ""

        if api == "" and region != "env":
            raise Exception("Invalid Env")

        return {"api": api, "realtime": realtime}
    except:
        global noRegionWarning
        if noRegionWarning is False:
            print("> TagoIO-SDK: No region or env defined, using fallback as usa-1.")
            noRegionWarning = True

        return regionsDefinition["usa-1"]
