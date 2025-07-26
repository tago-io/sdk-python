import os

from typing import Optional

from tagoio_sdk.common.tagoio_module import GenericModuleParams


def get_params(params: Optional[GenericModuleParams] = None) -> GenericModuleParams:
    if params is None:
        params = {"token": os.environ.get("T_ANALYSIS_TOKEN")}
    return params
