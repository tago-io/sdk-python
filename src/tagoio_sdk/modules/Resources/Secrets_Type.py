from datetime import datetime
from typing import List, Optional, TypedDict, Literal

from tagoio_sdk.common.Common_Type import GenericID, TagsObj, Query


class SecretsInfo(TypedDict):
    id: GenericID
    key: str
    tags: Optional[List[TagsObj]]
    value_length: int
    created_at: datetime
    updated_at: datetime


class SecretsCreate(TypedDict):
    key: str
    value: str
    tags: Optional[List[TagsObj]]


class SecretsEdit(TypedDict, total=False):
    value: str
    tags: Optional[List[TagsObj]]


class SecretsFilter(TypedDict):
    key: str
    tags: Optional[List[TagsObj]]


class SecretsQuery(Query):
    fields: Optional[List[Literal["id", "key", "tags", "created_at", "updated_at"]]]
    filter: Optional[SecretsFilter]
