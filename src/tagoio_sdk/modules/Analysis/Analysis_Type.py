from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from typing import TypedDict
from typing import Union

from tagoio_sdk.regions import Regions
from tagoio_sdk.regions import RegionsObj


AnalysisFunction = Callable[[Any, Any], Any]


class AnalysisConstructorParams(TypedDict, total=False):
    token: Optional[str]
    """Analysis token for authentication"""
    region: Optional[Union[Regions, RegionsObj]]
    """Region configuration for the analysis"""
    autostart: Optional[bool]
    """
    Auto start analysis after instance the class.
    If turned off, you can start analysis by calling [AnalysisInstance].start().
    Default: True
    """
    load_env_on_process: Optional[bool]
    """
    Load TagoIO Analysis envs on process environment.

    Warning: It's not safe to use on external analysis.
    It will load all env on process, then if the external analysis receives multiple requests
    simultaneously, it can mess up.

    Default: False
    """


AnalysisEnvironment = Dict[str, str]


AnalysisToken = str


AnalysisID = str


class TagoContext:
    """
    TagoIO Analysis Context interface.
    As current version of the SDK doesn't provide the full TagoContext interface.
    """

    token: AnalysisToken
    analysis_id: AnalysisID
    environment: List[AnalysisEnvironment]
    log: Callable[..., None]
