from datetime import datetime
from typing import List
from typing import Literal
from typing import Optional
from typing import TypedDict

from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.Common_Type import Query
from tagoio_sdk.common.Common_Type import TagsObj


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
