from datetime import datetime
from typing import Literal
from typing import Optional
from typing import TypedDict
from typing import Union


GenericID = str
"""ID used on TagoIO, string with 24 character"""


Base64 = str

GenericToken = str
"""Token used on TagoIO, string with 36 characters"""

ExpireTimeOption = Union[Literal["never"], datetime]

PermissionOption = Literal["write", "read", "full", "deny"]

Conditionals = Literal["<", ">", "=", "!", "><", "*"]


class TokenCreateResponse(TypedDict):
    token: GenericToken
    expire_date: ExpireTimeOption
    permission: PermissionOption


class TagsObj(TypedDict):
    key: str
    value: str


class File(TypedDict, total=False):
    url: str
    md5: str
    path: str


class FixedPositionValue(TypedDict):
    color: str
    icon: str
    value: str
    x: str
    y: str


class SentValue(TypedDict, total=False):
    label: str
    value: Union[str, int, float, bool]


class Metadata(TypedDict, total=False):
    color: Optional[str]
    x: Optional[Union[str, int, float]]
    y: Optional[Union[str, int, float]]
    label: Optional[str]
    file: Optional[File]
    icon: Optional[str]
    fixed_position: Optional[dict[str, FixedPositionValue]]
    sentValues: Optional[list[SentValue]]
    old_value: Optional[Union[str, int, float, bool]]


Latitude = float
Longitude = float


class LocationGeoJSON(TypedDict):
    type: Literal["Point"]
    coordinates: list[Union[Longitude, Latitude]]


class LocationLatLng(TypedDict):
    lat: float
    lng: float


class Data(TypedDict):
    """A bird with a flight speed exceeding that of an unladen swallow.

    Attributes:
        id     Data ID.
        device  ID of the device holding the data.
        variable    Name of the variable for the data.
        value   Data value
    """

    id: str
    device: str
    variable: str
    value: Union[str, float, int, bool]
    group: str
    unit: str
    location: LocationGeoJSON
    metadata: any
    time: datetime
    created_at: datetime


class DataCreate(TypedDict, total=False):
    variable: str
    value: Optional[Union[str, int, float, bool]]
    group: Optional[str]
    unit: Optional[str]
    metadata: Optional[Metadata]
    time: Optional[Union[str, datetime]]
    location: Optional[Union[LocationGeoJSON, LocationLatLng, None]]


class DataEdit(TypedDict, total=False):
    id: str
    value: Optional[Union[str, int, float, bool]]
    group: Optional[str]
    unit: Optional[str]
    metadata: Optional[Metadata]
    time: Optional[Union[str, datetime]]
    location: Optional[Union[LocationGeoJSON, LocationLatLng, None]]


class TokenDataList(TypedDict):
    token: GenericToken
    name: str
    type: str
    permission: PermissionOption
    serie_number: Optional[str]
    last_authorization: Optional[datetime]
    verification_code: Optional[str]
    expire_time: ExpireTimeOption
    ref_id: str
    created_at: datetime
    created_by: Optional[str]


class TokenData(TypedDict):
    name: str
    expire_time: Optional[ExpireTimeOption]
    permission: PermissionOption
    serie_number: Optional[str]
    verification_code: Optional[str]
    middleware: Optional[str]


class Query(TypedDict):
    """Query object for pagination

    Args:
        page (Optional[int]): 1

        amount (Optional[int]): ["id", "name"]

        fields (Optional[list[str]]): {"name": "test"}

        filter (Optional[any]): 20

        orderBy (Optional[list[Literal["asc", "desc"]]]): ["name": "asc"]

    Example:
    ```python
        {
            "page": 1,
            "fields": ["id", "name"],
            "filter": {"name": "test"},
            "amount": 20,
            "orderBy": ["name", "asc"]
        }
    ```
    """

    page: Optional[int]
    amount: Optional[int]
    fields: Optional[list[str]]
    filter: Optional[any]
    orderBy: Optional[list[Literal["asc", "desc"]]]
