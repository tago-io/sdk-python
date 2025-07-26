from datetime import datetime
from typing import Any
from typing import List
from typing import Literal
from typing import Optional
from typing import TypedDict

from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.Common_Type import Query


class IDeviceParameters(TypedDict, total=False):
    name: Optional[str]
    label: Optional[str]
    type: Optional[Literal["text", "dropdown", "switch", "number"]]
    default: Any
    group: Optional[Literal["default", "main", "advanced", "hide"]]
    options: Optional[List[Any]]
    """Optional only for dropdown"""


class ConnectorCreateInfo(TypedDict, total=False):
    name: Optional[str]
    description: Optional[str]
    logo_url: Optional[str]
    device_parameters: Optional[List[IDeviceParameters]]
    networks: Optional[List[GenericID]]
    payload_encoder: Optional[str]
    payload_decoder: Optional[str]
    """Base64 decoded string"""
    install_text: Optional[str]
    """Refers to the **description** in the Documentation settings"""
    install_end_text: Optional[str]
    """Refers to the **completion text** in the Documentation settings"""
    device_annotation: Optional[str]


class ConnectorInfo(ConnectorCreateInfo):
    id: GenericID
    public: bool
    description: Optional[str]
    logo_url: Optional[str]
    created_at: datetime
    updated_at: datetime
    device_parameters: Optional[List[IDeviceParameters]]
    networks: Optional[List[GenericID]]
    install_text: Optional[str]
    """Refers to the **description** in the Documentation settings"""
    install_end_text: Optional[str]
    """Refers to the **completion text** in the Documentation settings"""
    device_annotation: Optional[str]


class ConnectorQuery(Query):
    fields: Optional[
        List[
            Literal[
                "name",
                "id",
                "description",
                "logo_url",
                "install_text",
                "install_end_text",
                "device_annotation",
                "payload_decoder",
                "networks",
            ]
        ]
    ]
    filter: Optional[ConnectorInfo]
