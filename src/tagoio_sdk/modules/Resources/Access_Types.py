from datetime import datetime
from typing import Any
from typing import List
from typing import Literal
from typing import Optional
from typing import TypedDict

from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.Common_Type import Query
from tagoio_sdk.common.Common_Type import TagsObj


class Permissions(TypedDict):
    effect: Literal["allow", "deny"]
    action: List[str]
    resource: List[str]


class AccessCreateInfo(TypedDict):
    name: str
    permissions: List[Permissions]
    targets: List[Any]
    profile: Optional[GenericID]
    tags: Optional[List[TagsObj]]
    active: Optional[bool]


class AccessInfo(AccessCreateInfo):
    id: GenericID
    created_at: datetime
    updated_at: datetime


class AccessQuery(Query):
    fields: Optional[List[Literal["name", "active", "created_at", "updated_at"]]]
