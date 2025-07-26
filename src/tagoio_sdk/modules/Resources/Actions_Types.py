from datetime import datetime
from typing import Dict
from typing import List
from typing import Literal
from typing import Optional
from typing import TypedDict
from typing import Union

from tagoio_sdk.common.Common_Type import Conditionals
from tagoio_sdk.common.Common_Type import ExpireTimeOption
from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.Common_Type import Query
from tagoio_sdk.common.Common_Type import TagsObj


ActionType = Literal["condition", "resource", "interval", "schedule", "mqtt_topic", "usage_alert", "condition_geofence"]


class TriggerGeofenceValueType(TypedDict, total=False):
    center: Optional[List[float]]
    """E.g [longitude, latitude]"""
    radius: Optional[float]
    coordinates: Optional[List[List[float]]]
    """E.g [[longitude, latitude], [longitude, latitude], ...]"""


class ActionTypeScriptParams(TypedDict):
    script: List[GenericID]
    type: Literal["script"]


class ActionTypeNotificationParams(TypedDict):
    message: str
    subject: str
    type: Literal["notification"]


class ActionTypeNotificationRunParams(TypedDict):
    message: str
    subject: str
    run_user: GenericID
    type: Literal["notification_run"]


class ActionTypeEmailParams(TypedDict):
    message: str
    subject: str
    to: str
    type: Literal["email"]


class ActionTypeSMSParams(TypedDict):
    message: str
    to: str
    type: Literal["sms"]


class ActionTypeMQTTParams(TypedDict):
    bucket: str
    payload: str
    topic: str
    type: Literal["mqtt"]


class ActionTypePostParams(TypedDict):
    headers: Dict
    type: Literal["post"]
    url: str


ActionTypeParams = Union[
    ActionTypeScriptParams,
    ActionTypeNotificationParams,
    ActionTypeNotificationRunParams,
    ActionTypeEmailParams,
    ActionTypeSMSParams,
    ActionTypeMQTTParams,
    ActionTypePostParams,
]


class ActionTriggerResourceType(TypedDict):
    resource: Literal["device", "bucket", "file", "analysis", "action", "am", "user", "financial", "profile"]
    when: Literal["create", "update", "delete"]
    tag_key: str
    tag_value: str


class ActionTriggerIntervalType(TypedDict):
    interval: str


class ActionTriggerCronType(TypedDict):
    timezone: Union[str, datetime]
    cron: str
    """The cron expression"""


class ActionTriggerConditionType(TypedDict, total=False):
    device: str
    variable: str
    __annotations__ = {"is": Conditionals}
    """Using '__annotations__' to define this field because 'is' is a Python reserved keyword."""
    value: str
    second_value: Optional[str]
    value_type: Literal["string", "number", "boolean", "*"]
    unlock: Optional[bool]


class ActionTriggerUsageType(TypedDict):
    service_or_resource: Literal[
        "input",
        "output",
        "analysis",
        "data_records",
        "sms",
        "email",
        "run_users",
        "push_notification",
        "file_storage",
        "device",
        "dashboard",
        "action",
        "tcore",
        "team_members",
        "am",
    ]
    condition: Literal["=", ">"]
    condition_value: float


class ActionTriggerGeofenceType(TypedDict, total=False):
    device: str
    variable: str
    __annotations__ = {"is": Literal["IN", "OUT"]}
    """Using '__annotations__' to define this field because 'is' is a Python reserved keyword."""
    value: TriggerGeofenceValueType
    unlock: Optional[bool]


ActionTriggerType = Union[
    ActionTriggerResourceType,
    ActionTriggerIntervalType,
    ActionTriggerCronType,
    ActionTriggerConditionType,
    ActionTriggerUsageType,
    ActionTriggerGeofenceType,
]


class ActionCreateInfo(TypedDict, total=False):
    name: str
    """The name for the action"""
    profile: Optional[GenericID]
    """Profile identification"""
    active: Optional[bool]
    """True if the action is active or not. The default is true"""
    tags: Optional[List[TagsObj]]
    """An array of tags"""
    description: Optional[str]
    """Description of the action"""
    lock: Optional[bool]
    type: Optional[ActionType]
    """Type of action"""
    trigger: Optional[List[ActionTriggerType]]
    """Array of trigger configuration according to type"""
    action: ActionTypeParams
    """Action configuration"""
    trigger_when_unlock: Optional[bool]
    """Trigger the action when unlock condition is met"""


class ActionInfo(ActionCreateInfo):
    id: GenericID
    last_triggered: ExpireTimeOption
    updated_at: datetime
    created_at: datetime


class MQTTResourceAction(TypedDict, total=False):
    client_id: str
    connected_at: str
    disconnect_at: Optional[str]


class ActionQuery(Query):
    fields: Optional[List[Literal["name", "active", "last_triggered", "created_at", "updated_at"]]]
    filter: Optional[ActionInfo]
