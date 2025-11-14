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
    fields: Optional[
        List[
            Literal["name", "active", "run_on", "last_run", "created_at", "updated_at"]
        ]
    ]


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


SnippetRuntime = Literal[
    "node-legacy", "python-legacy", "node-rt2025", "python-rt2025", "deno-rt2025"
]
"""Available runtime environments for snippets"""


class SnippetItem(TypedDict):
    """Individual snippet metadata"""

    id: str
    """Unique identifier for the snippet"""
    title: str
    """Human-readable title"""
    description: str
    """Description of what the snippet does"""
    language: str
    """Programming language (typescript, javascript, python)"""
    tags: List[str]
    """Array of tags for categorization"""
    filename: str
    """Filename of the snippet"""
    file_path: str
    """Full path to the file in the runtime directory"""


class SnippetsListResponse(TypedDict):
    """API response containing all snippets metadata for a runtime"""

    runtime: SnippetRuntime
    """Runtime environment identifier"""
    schema_version: int
    """Schema version for the API response format"""
    generated_at: str
    """ISO timestamp when the response was generated"""
    snippets: List[SnippetItem]
    """Array of all available snippets for this runtime"""
