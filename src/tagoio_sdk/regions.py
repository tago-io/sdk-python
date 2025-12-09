import os

from typing import Literal
from typing import Optional
from typing import TypedDict
from typing import Union


class RegionsObjApi(TypedDict):
    """Region configuration with API/SSE endpoints."""

    api: str
    sse: str


class RegionsObjTDeploy(TypedDict):
    """Region configuration with TagoIO Deploy Project ID."""

    tdeploy: str


RegionsObj = Union[RegionsObjApi, RegionsObjTDeploy]
"""Region configuration object (either API/SSE pair or TDeploy)"""

Regions = Literal["us-e1", "eu-w1", "env"]
"""Supported TagoIO regions"""

# Runtime region cache
runtimeRegion: Optional[RegionsObj] = None

# Object of Regions Definition
regionsDefinition: dict[str, Optional[RegionsObjApi]] = {
    "us-e1": {
        "api": "https://api.tago.io",
        "sse": "https://sse.tago.io/events",
    },
    "eu-w1": {
        "api": "https://api.eu-w1.tago.io",
        "sse": "https://sse.eu-w1.tago.io/events",
    },
    "env": None,  # process object should be on trycatch
}


def getConnectionURI(region: Optional[Union[Regions, RegionsObj]] = None) -> RegionsObjApi:
    """
    Get connection URI for API and SSE.

    Args:
        region: Region identifier or configuration object

    Returns:
        Region configuration with API and SSE endpoints

    Raises:
        ReferenceError: If invalid region is specified
    """
    global runtimeRegion

    # Handle tdeploy in RegionsObj - takes precedence
    if isinstance(region, dict) and "tdeploy" in region:
        tdeploy = region["tdeploy"].strip()
        if tdeploy:
            return {
                "api": f"https://api.{tdeploy}.tagoio.net",
                "sse": f"https://sse.{tdeploy}.tagoio.net/events",
            }

    normalized_region = region
    if isinstance(normalized_region, str) and normalized_region == "usa-1":
        normalized_region = "us-e1"

    value: Optional[RegionsObjApi] = None
    if isinstance(normalized_region, str):
        value = regionsDefinition.get(normalized_region)
    elif isinstance(normalized_region, dict):
        # If it's already a RegionsObj with api/sse, use it
        if "api" in normalized_region and "sse" in normalized_region:
            value = normalized_region

    if value is not None:
        return value

    if runtimeRegion is not None:
        return runtimeRegion

    if region is not None and region != "env":
        raise ReferenceError(f"> TagoIO-SDK: Invalid region {region}.")

    try:
        api = os.environ.get("TAGOIO_API")
        sse = os.environ.get("TAGOIO_SSE")

        if not api and region != "env":
            raise Exception("Invalid Env")

        return {"api": api or "", "sse": sse or ""}
    except Exception:
        # if not noRegionWarning:
        #     print("> TagoIO-SDK: No region or env defined, using fallback as usa-1.")
        #     noRegionWarning = True

        return regionsDefinition["us-e1"]


def setRuntimeRegion(region: RegionsObj) -> None:
    """
    Set region in-memory to be inherited by other modules when set in the Analysis runtime
    with `Analysis.use()`.

    Example:
        ```python
        def my_analysis(context, scope):
            # this uses the region defined through `use`
            resources = Resources({"token": token})

            # it's still possible to override if needed
            europe_resources = Resources({"token": token, "region": "eu-w1"})

        Analysis.use(my_analysis, {"region": "us-e1"})
        ```

    Args:
        region: Region configuration object
    """
    global runtimeRegion
    runtimeRegion = region
