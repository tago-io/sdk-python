from typing import List, Optional, Any
from datetime import datetime
from typing import Literal, TypedDict

from tagoio_sdk.common.Common_Type import GenericID, Query, TagsObj


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
