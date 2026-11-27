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
from tagoio_sdk.common.Common_Type import RunTypeOptions
from tagoio_sdk.common.Common_Type import TagsObj


class ScriptFile(TypedDict):
    name: str
    content: Base64
    language: RunTypeOptions


class AnalysisMqttEvents(TypedDict, total=False):
    """
    Session events of the MQTT Endpoint that also run the code; a PUBLISH always runs it.
    info returns all three keys; create and edit accept any subset.
    """

    connect: bool
    """Run the code when a device connects. Default False."""
    subscribe: bool
    """Run the code once per filter when a device subscribes. Default False."""
    unsubscribe: bool
    """Run the code once per filter when a device unsubscribes. Default False."""


class AnalysisMqttPorts(TypedDict):
    """Ports devices use to reach the MQTT Endpoint."""

    plain: int
    """Port without TLS."""
    secure: int
    """Port with TLS."""


class AnalysisMqttChanges(TypedDict, total=False):
    """MQTT Endpoint settings on create and edit. Edit merges them into the stored settings."""

    active: bool
    """Turns the MQTT Endpoint on or off. Luau Analyses only."""
    events: AnalysisMqttEvents
    """Session events to turn on or off."""


class AnalysisMqtt(AnalysisMqttChanges, total=False):
    """MQTT Endpoint state of an Analysis, as info returns it."""

    host: str
    """Read only. Host devices connect to; present only when the instance configures one."""
    ports: AnalysisMqttPorts
    """Read only. Ports devices connect to; present only with host."""


AnalysisMqttOutcome = Literal["ran", "failed", "refused", "rate_limited", "too_large"]
"""How an MQTT Endpoint test run ended."""


class AnalysisMqttTry(TypedDict, total=False):
    """Message for an MQTT Endpoint test run."""

    topic: str
    """Required. Topic name, without +, #, or NUL."""
    payload: str
    """Required. Payload the code receives, as a string."""
    qos: Literal[0, 1, 2]
    """QoS of the message. Default 1."""


class AnalysisMqttTryResult(TypedDict):
    """Result of an MQTT Endpoint test run."""

    outcome: AnalysisMqttOutcome
    """How the run ended."""
    duration_ms: int
    """Time the run took to answer, admission wait included, in milliseconds."""


class AnalysisCreateInfo(TypedDict, total=False):
    name: str
    description: Optional[str]
    interval: Optional[str]
    run_on: Optional[Literal["tago", "external"]]
    file_name: Optional[str]
    runtime: Optional[RunTypeOptions]
    active: Optional[bool]
    profile: Optional[GenericID]
    variables: Optional[List[Dict[str, Union[str, int, bool]]]]
    tags: Optional[List[TagsObj]]
    mqtt: Optional[AnalysisMqttChanges]
    """MQTT Endpoint settings. Luau Analyses only; other runtimes answer 400."""


class AnalysisInfo(AnalysisCreateInfo):
    id: GenericID
    token: str
    last_run: ExpireTimeOption
    created_at: datetime
    updated_at: datetime
    locked_at: Any
    console: Optional[List[str]]
    mqtt: Optional[AnalysisMqtt]
    """MQTT Endpoint state. Returned by info, not by list."""


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


SnippetRuntime = Literal["node-legacy", "python-legacy", "node-rt2025", "python-rt2025", "deno-rt2025"]
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
