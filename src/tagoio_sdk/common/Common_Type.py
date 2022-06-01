from datetime import datetime
from typing import Literal, TypedDict, Union

GenericID = str
"""ID used on TagoIO, string with 24 character"""


Base64 = str


class LocationGeoJSON(TypedDict):
    type: Literal["Point"]
    coordinates: list[str]


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
