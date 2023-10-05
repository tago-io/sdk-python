from datetime import datetime
from typing import Any, Literal, Optional, TypedDict, Union

from tagoio_sdk.common.Common_Type import GenericID

HexColor = str


class NotificationTriggerAnalysis(TypedDict):
    analysis_id: GenericID


class NotificationTriggerHTTP(TypedDict):
    url: str
    method: Literal["POST", "GET", "PUT", "DELETE", "REDIRECT"]
    body: dict[str, Any]


class NotificationTriggerProfile(TypedDict):
    share_profile: Literal["accept", "refuse"]


class NotificationButton(TypedDict):
    id: str
    label: str
    color: Optional[str]
    triggers: Union[
        NotificationTriggerAnalysis,
        NotificationTriggerHTTP,
        list[NotificationTriggerProfile],
    ]


class NotificationIconImage(TypedDict):
    image_url: str
    bg_color: Optional[HexColor]
    fit: Optional[Literal["fill", "contain", "cover"]]


class NotificationIconSVG(TypedDict):
    svg_url: str
    svg_color: Optional[HexColor]
    bg_color: Optional[HexColor]


class NotificationCreate(TypedDict):
    title: str
    message: str
    read: Optional[bool]
    icon: Optional[Union[NotificationIconSVG, NotificationIconImage]]
    buttons: Optional[list[NotificationButton]]
    buttons_enabled: Optional[bool]
    buttons_autodisable: Optional[bool]


class NotificationInfoBasic(TypedDict):
    id: GenericID
    created_at: datetime


class NotificationCreateReturn(TypedDict):
    id: GenericID


NotificationInfo = NotificationInfoBasic and NotificationCreate
