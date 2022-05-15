from typing import Literal, Optional, TypedDict, Union


class DeviceInfo(TypedDict):
    id: str
    profile: str
    name: Optional[str]
    description: Optional[str]
    visible: Optional[bool]


class DataQueryBase(TypedDict):
    variables: Union[str, list[str]]
    groups: Union[str, list[str]]
    ids: Union[str, list[str]]


class DataQueryDefault(DataQueryBase):
    query: Literal["default"]
    qty: int
    details: bool
    ordination: Literal["descending", "ascending"]
    skip: int


class DataQueryFirstLast(DataQueryBase):
    query: Literal[
        "last_item",
        "last_value",
        "last_location",
        "last_insert",
        "first_item",
        "first_value",
        "first_location",
        "first_insert",
    ]


DataQuery = Union[DataQueryDefault, DataQueryFirstLast]
