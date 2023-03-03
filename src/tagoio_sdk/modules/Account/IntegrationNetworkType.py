from datetime import datetime
from typing import Optional, TypedDict, Literal, Union
from tagoio_sdk.common.Common_Type import TokenData, GenericID, Query


class serial_number(TypedDict):
    mask: Optional[str]
    label: Optional[str]
    image: Optional[str]
    case: Optional[str]
    help: Optional[str]
    required: bool


class IDeviceParameters(TypedDict):
    name: Optional[str]
    label: Optional[str]
    type: Optional[Literal["text", "dropdown", "switch", "number"]]
    default: Optional[any]
    group: Optional[Literal["default", "main", "advanced", "hide"]]
    options: Optional[list[any]]


class NetworkCreateInfo(TypedDict):
    name: Optional[str]
    description: Optional[str]
    logo_url: Optional[str]
    icon_url: Optional[str]
    banner_url: Optional[str]
    device_parameters: Optional[list[IDeviceParameters]]
    middleware_endpoint: Optional[str]
    payload_encoder: Optional[str]
    payload_decoder: Optional[str]
    public: Optional[bool]
    documentation_url: Optional[str]
    serial_number: Optional[serial_number]
    require_devices_access: Optional[bool]


class NetworkInfo(NetworkCreateInfo):
    id: GenericID
    name: Optional[str]
    description: Optional[str]
    logo_url: Optional[str]
    icon_url: Optional[str]
    banner_url: Optional[str]
    device_parameters: Optional[list[IDeviceParameters]]
    middleware_endpoint: Optional[str]
    payload_encoder: Optional[str]
    payload_decoder: Optional[str]
    public: Optional[bool]
    documentation_url: Optional[str]
    serial_number: Optional[serial_number]


class NetworkTokenInfo(TokenData):
    created_at: datetime
    updated_at: datetime
    Network: GenericID
    type: Literal["type", "Network"]


NetworkQuery = Union[
    Query,
    Literal[
        "name",
        "description",
        "logo_url",
        "icon_url",
        "banner_url",
        "device_parameters",
        "middleware_endpoint",
        "payload_encoder",
        "payload_decoder",
        "serial_number",
        "documentation_url",
        "public",
        "created_at",
        "updated_at",
    ],
]
