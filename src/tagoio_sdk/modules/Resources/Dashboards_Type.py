from datetime import datetime
from typing import Literal
from typing import Optional
from typing import TypedDict
from typing import Union

from tagoio_sdk.common.Common_Type import ExpireTimeOption
from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.Common_Type import GenericToken
from tagoio_sdk.common.Common_Type import TagsObj
from tagoio_sdk.modules.Resources.Buckets_Type import BucketDeviceInfo


class Arrangement(TypedDict):
    widget_id: str
    x: Union[int, float]
    y: Union[int, float]
    width: Union[int, float]
    height: Union[int, float]
    tab: Optional[str]


class DashboardCreateInfo(TypedDict):
    label: str
    arrangement: list[Arrangement]
    tags: list[TagsObj]
    visible: bool


class icon(TypedDict):
    url: str
    color: Optional[str]


class conditions(TypedDict):
    key: str
    value: str


class filter_conditions(TypedDict):
    blueprint_device: str
    tag_key: str
    type: str


class shared(TypedDict):
    id: str
    email: str
    name: str
    free_account: bool
    allow_tags: bool
    expire_time: str
    allow_share: bool


class blueprint_devices(TypedDict):
    conditions: list[conditions]
    name: str
    id: str
    label: str
    filter_conditions: list[filter_conditions]
    theme: any
    setup: any


class DashboardInfo(TypedDict):
    id: GenericID
    created_at: datetime
    updated_at: datetime
    last_access: datetime
    group_by: list
    tabs: list
    icon: icon
    background: any
    type: str
    blueprint_device_behavior: Literal["more_than_one", "always"]
    blueprint_selector_behavior: Literal[
        "open", "closed", "always_open", "always_closed"
    ]
    blueprint_devices: blueprint_devices
    theme: any
    setup: any
    shared: shared


class WidgetData(TypedDict):
    origin: GenericID
    qty: Optional[Union[int, float]]
    timezone: Optional[str]
    variables: Optional[str]
    bucket: Optional[GenericID]
    query: Optional[Literal["min", "max", "count", "avg", "sum"]]
    start_date: Optional[Union[datetime, str]]
    end_date: Optional[Union[datetime, str]]
    overwrite: Optional[bool]


class WidgetResource(TypedDict):
    filter: list[TagsObj]


DeviceResourceView = Literal[
    f"tags.{str}",
    f"param.{str}",
    "name",
    "id",
    "bucket_name",
    "network_name",
    "connector_name",
    "connector",
    "network",
    "bucket",
    "last_input",
    "created_at",
    "active",
]


class WidgetDeviceResource(TypedDict):
    type: Literal["device"]
    view: DeviceResourceView
    editable: Literal["name", f"tags.{str}", f"param.{str}"]


class EditDeviceResource(TypedDict):
    device: GenericID
    name: Optional[str]
    active: Optional[bool]
    edit: dict[str, Union[str, bool]]


class EditResourceOptions(TypedDict):
    identifier: Optional[str]


class WidgetInfo(TypedDict):
    analysis_run: Optional[GenericID]
    dashboard: Optional[GenericID]
    display: any
    data: Optional[list[WidgetData]]
    resource: Optional[list[WidgetDeviceResource]]
    id: Optional[GenericID]
    label: str
    realtime: Optional[bool]
    type: str


class DevicesRelated(BucketDeviceInfo):
    bucket: GenericID


class AnalysisRelated(TypedDict):
    id: GenericID
    name: str


class PostDataModel(TypedDict):
    origin: GenericID
    variable: str


class blueprint_devices(TypedDict):
    origin: GenericID
    id: GenericID
    bucket: Optional[GenericID]


class widgetOverwrite(TypedDict):
    start_date: Optional[any]
    end_date: Optional[any]
    timezone: Optional[any]


class GetDataModel(TypedDict):
    overwrite: Optional[widgetOverwrite]
    blueprint_devices: Optional[list[blueprint_devices]]
    page: Optional[Union[int, float]]
    amount: Optional[Union[int, float]]


class PublicKeyResponse(TypedDict):
    token: GenericToken
    expire_time: ExpireTimeOption


EditDataModel = PostDataModel and {id: GenericID}

PublicKeyResponse = PublicKeyResponse

widgetOverwriteOptions = Literal["start_date", "end_date", "timezone"]
