from datetime import datetime
from typing import List
from typing import Literal
from typing import Optional
from typing import TypedDict
from typing import Union

from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.Common_Type import Query
from tagoio_sdk.common.Common_Type import TagsObj


class SQLParam(TypedDict):
    """Positional parameter as ``{"key": "$n", "value": "..."}``."""

    key: str
    value: str


class SQLCreateInfo(TypedDict, total=False):
    name: str
    description: Optional[str]
    query: str
    params: Optional[List[SQLParam]]
    cache_enabled: Optional[bool]
    cache_ttl_seconds: Optional[int]
    rate_limit_rpm: Optional[int]
    active: Optional[bool]
    tags: Optional[List[TagsObj]]


class SQLInfo(SQLCreateInfo):
    id: GenericID
    version: int
    created_at: datetime
    updated_at: datetime


class SQLQuery(Query):
    fields: Optional[
        List[
            Literal[
                "id",
                "name",
                "description",
                "query",
                "params",
                "cache_enabled",
                "cache_ttl_seconds",
                "rate_limit_rpm",
                "active",
                "tags",
                "version",
                "created_at",
                "updated_at",
            ]
        ]
    ]
    filter: Optional[SQLInfo]


class SQLExecuteObj(TypedDict, total=False):
    params: Optional[List[SQLParam]]
    test: Optional[bool]
    after_device: Optional[GenericID]


class SQLColumn(TypedDict):
    name: str
    type: Literal["string", "number", "timestamp", "boolean", "json"]


class SQLExecuteResult(TypedDict):
    columns: List[SQLColumn]
    rows: List[dict[str, Union[str, float, bool, None, dict, list]]]
    row_count: int
    execution_ms: int
    served_from_cache: bool


class SQLVersionInfo(TypedDict):
    query: str
    params: List[SQLParam]
    created_at: Optional[datetime]


class SQLTableInfo(TypedDict, total=False):
    function: str
    label: str
    tag_form: Optional[str]
    columns: List[SQLColumn]
    dynamic: Optional[bool]


class SQLResourceItem(TypedDict):
    id: GenericID
    name: str


class SQLTablesResources(TypedDict):
    devices: List[SQLResourceItem]
    entities: List[SQLResourceItem]


class SQLTablesResult(TypedDict):
    tables: List[SQLTableInfo]
    resources: SQLTablesResources


class SQLTablesQuery(TypedDict, total=False):
    filter: Optional[str]
    amount: Optional[int]
    page: Optional[int]
    entity_id: Optional[GenericID]
