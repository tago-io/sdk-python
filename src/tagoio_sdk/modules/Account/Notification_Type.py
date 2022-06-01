from typing import Any, Literal, TypedDict, Union

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
    color: str
    triggers: Union[
        NotificationTriggerAnalysis,
        NotificationTriggerHTTP,
        list[NotificationTriggerProfile],
    ]


class NotificationIconImage(TypedDict):
    image_url: str
    bg_color: HexColor
    fit: Literal["fill", "contain", "cover"]


class NotificationIconSVG(TypedDict):
    svg_url: str
    svg_color: HexColor
    bg_color: HexColor


class NotificationCreate(TypedDict):
    title: str
    message: str
    read: bool
    icon: Union[NotificationIconSVG, NotificationIconImage]
    buttons: list[NotificationButton]
    buttons_enabled: bool
    buttons_autodisable: bool
