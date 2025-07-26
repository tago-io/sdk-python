from datetime import datetime
from typing import Any
from typing import Dict
from typing import List
from typing import Literal
from typing import Optional
from typing import TypedDict
from typing import Union

from tagoio_sdk.common.Common_Type import Base64
from tagoio_sdk.common.Common_Type import ExpireTimeOption
from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.Common_Type import Query
from tagoio_sdk.common.Common_Type import TagsObj


class ScriptFile(TypedDict):
    name: str
    content: Base64
    language: Literal["node", "python"]


class AnalysisCreateInfo(TypedDict, total=False):
    name: str
    description: Optional[str]
    interval: Optional[str]
    run_on: Optional[Literal["tago", "external"]]
    file_name: Optional[str]
    runtime: Optional[Literal["node", "python"]]
    active: Optional[bool]
    profile: Optional[GenericID]
    variables: Optional[List[Dict[str, Union[str, int, bool]]]]
    tags: Optional[List[TagsObj]]


class AnalysisInfo(AnalysisCreateInfo):
    id: GenericID
    token: str
    last_run: ExpireTimeOption
    created_at: datetime
    updated_at: datetime
    locked_at: Any
    console: Optional[List[str]]


class AnalysisQuery(Query):
    fields: Optional[List[Literal["name", "active", "run_on", "last_run", "created_at", "updated_at"]]]


class AnalysisListItem(TypedDict, total=False):
    id: Optional[GenericID]
    name: Optional[str]
    active: Optional[bool]
    run_on: Optional[Literal["tago", "external"]]
    last_run: Optional[ExpireTimeOption]
    created_at: Optional[str]
    updated_at: Optional[str]
    locked_at: Optional[str]
    console: Optional[List[str]]
