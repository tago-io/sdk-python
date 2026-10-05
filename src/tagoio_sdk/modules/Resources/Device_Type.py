from datetime import datetime
from typing import Literal
from typing import Optional
from typing import TypedDict
from typing import Union

from tagoio_sdk.common.Common_Type import ExpireTimeOption
from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.Common_Type import GenericToken
from tagoio_sdk.common.Common_Type import PermissionOption
from tagoio_sdk.common.Common_Type import TagsObj
from tagoio_sdk.modules.Resources.Buckets_Type import DataStorageType


class bucket(TypedDict):
    id: GenericID
    name: str


class DeviceInfo(TypedDict):
    id: GenericID
    """
    Device ID.
    """
    type: DataStorageType
    """
    Device's data storage (bucket) type.
    """
    profile: GenericID
    """
    ID of the profile that owns the device.
    """
    bucket: bucket
    """
    Bucket storing the device's data.
    """
    last_output: datetime or None
    """
    Date for the device's last output.
    """
    last_input: datetime or None
    """
    Date for the device's last input.
    """
    updated_at: datetime
    """
    Date for the device's last update.
    """
    created_at: datetime
    """
    Date for the device's creation.
    """
    inspected_at: datetime or None
    """
    Date for the device's last inspection.
    """
    last_retention: datetime or None
    """
    Date for the device's last data retention.
    """
    mutable_variable_regex: str or None
    """
    Regex that routes each variable to the mutable side at insert time (unanchored substring match).

    It must not match every variable or no variable; use a mutable or immutable device for those cases.

    Present for Hybrid devices. Can only be changed while the device is empty.
    """


class DeviceInfoList(TypedDict):
    id: GenericID
    """
    Device ID.
    """
    type: DataStorageType
    """
    Device's data storage (bucket) type.
    """
    profile: GenericID
    """
    ID of the profile that owns the device.
    """
    last_output: datetime or None
    """
    Date for the device's last output.
    """
    last_input: datetime or None
    """
    Date for the device's last input.
    """
    updated_at: datetime
    """
    Date for the device's last update.
    """
    created_at: datetime
    """
    Date for the device's creation.
    """
    inspected_at: datetime or None
    """
    Date for the device's last inspection.
    """
    last_retention: datetime or None
    """
    Date for the device's last data retention.
    """
    bucket: GenericID


class DeviceQuery(TypedDict):
    page: Union[int, float]
    """
    Page of list starting from 1
    """
    amount: Union[int, float]
    """
    Amount of items will return.
    """
    fields: list[
        Literal[
            "id",
            "type",
            "profile",
            "last_output",
            "last_input",
            "updated_at",
            "created_at",
            "inspected_at",
            "last_retention",
        ]
    ]
    """
    Array of field names.
    """
    filter: DeviceInfo
    """
    Filter object.
    """
    orderBy: list[
        Literal[
            "name",
            "visible",
            "active",
            "last_input",
            "last_output",
            "created_at",
            "updated_at",
            "asc",
            "desc",
        ]
    ]
    """
    Tuple with a field and an order
    """
    resolveBucketName: Optional[bool]


DeviceListItem = DeviceInfoList


class ConfigurationParams(TypedDict):
    sent: bool
    key: str
    value: str
    id: Optional[str]


class DeviceCreateResponse(TypedDict):
    device_id: GenericID
    bucket_id: GenericID
    token: GenericToken


class DeviceCreateInfoBasic(TypedDict):
    name: str
    """
    Device name.
    """
    connector: GenericID
    """
    Connector ID.
    """
    network: GenericID
    """
    Network ID.
    """
    type: Optional[DataStorageType]
    """
    Device's data storage (bucket) type.

    :default: "legacy"
    """
    description: Optional[str or None]
    """
    Description of the device.
    """
    active: Optional[bool]
    """
    Set if the device will be active.
    """
    visible: Optional[bool]
    """
    Set if the device will be visible.
    """
    configuration_params: Optional[list[ConfigurationParams]]
    """
    An array of configuration params
    """
    tags: Optional[list[TagsObj]]
    """
    An array of tags
    """
    serie_number: Optional[str]
    """
    Device serial number.
    """
    connector_parse: Optional[bool]
    """
    If device will use connector parser
    """
    parse_function: Optional[str]
    """
    Javascript code for use as payload parser
    """


class DeviceCreateInfoBasicMutable(TypedDict):
    name: str
    """
    Device name.
    """
    connector: GenericID
    """
    Connector ID.
    """
    network: GenericID
    """
    Network ID.
    """
    type: Literal["mutable"]
    """
    Device's data storage (bucket) type.

    :default: "legacy"
    """
    description: str or None
    """
    Description of the device.
    """
    active: bool
    """
    Set if the device will be active.
    """
    visible: bool
    """
    Set if the device will be visible.
    """
    configuration_params: list[ConfigurationParams]
    """
    An array of configuration params
    """
    tags: list[TagsObj]
    """
    An array of tags
    """
    serie_number: str
    """
    Device serial number.
    """
    connector_parse: bool
    """
    If device will use connector parser
    """
    parse_function: str
    """
    Javascript code for use as payload parser
    """


class DeviceCreateInfoBasicImmutable(TypedDict):
    name: str
    """
    Device name.
    """
    connector: GenericID
    """
    Connector ID.
    """
    network: GenericID
    """
    Network ID.
    """
    type: Literal["immutable"]
    """
    Device's data storage (bucket) type.

    :default: "legacy"
    """
    description: str or None
    """
    Description of the device.
    """
    active: bool
    """
    Set if the device will be active.
    """
    visible: bool
    """
    Set if the device will be visible.
    """
    configuration_params: list[ConfigurationParams]
    """
    An array of configuration params
    """
    tags: list[TagsObj]
    """
    An array of tags
    """
    serie_number: str
    """
    Device serial number.
    """
    connector_parse: bool
    """
    If device will use connector parser
    """
    parse_function: str
    """
    Javascript code for use as payload parser
    """
    chunk_period: Literal["day", "week", "month", "quarter"]
    """
    Chunk division to retain data in the device.

    Required for Immutable devices.
    """
    chunk_retention: Union[int, float]
    """
    Amount of chunks to retain data according to the `chunk_period`.

    Integer between in the range of 0 to 36 (inclusive).

    Required for Immutable devices.
    """


class DeviceCreateInfoBasicHybrid(TypedDict):
    name: str
    """
    Device name.
    """
    connector: GenericID
    """
    Connector ID.
    """
    network: GenericID
    """
    Network ID.
    """
    type: Literal["hybrid"]
    """
    Device's data storage (bucket) type.

    :default: "legacy"
    """
    description: str or None
    """
    Description of the device.
    """
    active: bool
    """
    Set if the device will be active.
    """
    visible: bool
    """
    Set if the device will be visible.
    """
    configuration_params: list[ConfigurationParams]
    """
    An array of configuration params
    """
    tags: list[TagsObj]
    """
    An array of tags
    """
    serie_number: str
    """
    Device serial number.
    """
    connector_parse: bool
    """
    If device will use connector parser
    """
    parse_function: str
    """
    Javascript code for use as payload parser
    """
    chunk_period: Literal["day", "week", "month", "quarter"]
    """
    Chunk division to retain data in the device.

    Required for Immutable devices.
    """
    chunk_retention: Union[int, float]
    """
    Amount of chunks to retain data according to the `chunk_period`.

    Integer between in the range of 0 to 36 (inclusive).

    Required for Immutable devices.
    """
    mutable_variable_regex: str
    """
    Regex that routes each variable to the mutable side at insert time (unanchored substring match).

    It must not match every variable or no variable; use a mutable or immutable device for those cases.

    Required for Hybrid devices. Can only be changed while the device is empty.
    """


DeviceCreateInfoMutable = DeviceCreateInfoBasicMutable

DeviceCreateInfoImmutable = DeviceCreateInfoBasicImmutable

DeviceCreateInfoHybrid = DeviceCreateInfoBasicHybrid

DeviceCreateInfo = (
    DeviceCreateInfoMutable or DeviceCreateInfoImmutable or DeviceCreateInfoHybrid
)


class DeviceEditInfo(TypedDict):
    name: str
    """
    Device name.
    """
    connector: GenericID
    """
    Connector ID.
    """
    network: GenericID
    """
    Network ID.
    """
    description: str or None
    """
    Description of the device.
    """
    active: bool
    """
    Set if the device will be active.
    """
    visible: bool
    """
    Set if the device will be visible.
    """
    configuration_params: list[ConfigurationParams]
    """
    An array of configuration params
    """
    tags: list[TagsObj]
    """
    An array of tags
    """
    serie_number: str
    """
    Device serial number.
    """
    connector_parse: bool
    """
    If device will use connector parser
    """
    parse_function: str
    """
    Javascript code for use as payload parser
    """
    chunk_retention: Union[int, float]
    """
    Amount of chunks to retain data according to the `chunk_period`.

    Integer between in the range of 0 to 36 (inclusive).

    Required for Immutable devices.
    """
    mutable_variable_regex: Optional[str]
    """
    Regex that routes each variable to the mutable side at insert time (unanchored substring match).

    It must not match every variable or no variable; use a mutable or immutable device for those cases.

    Required for Hybrid devices. Can only be changed while the device is empty.
    """


DeviceEditInfo = DeviceEditInfo


class DeviceEmptyParams(TypedDict, total=False):
    route: Literal["mutable", "immutable"]
    """
    For Hybrid devices only: empty a single side of the device instead of everything.
    "mutable" truncates the editable variables; "immutable" drops the telemetry chunks.
    Omit to remove all data (every device type).
    """


class TokenData(TypedDict):
    name: str
    """
    A name for the token.
    """
    expire_time: ExpireTimeOption
    """
    The time for when the token should expire.
    It will be randomly generated if not included.
    Accepts “never” as value.
    """
    permission: PermissionOption
    """
    Token permission should be 'write', 'read' or 'full'.
    """
    serie_number: Optional[str]
    """
    [optional] The serial number of the device.
    """
    verification_code: Optional[str]
    """
    [optional] Verification code to validate middleware requests.
    """
    middleware: Optional[str]
    """
    [optional] Middleware or type of the device that will be added.
    """


class DeviceTokenDataList(TypedDict):
    token: GenericToken
    device_id: GenericID
    network_id: GenericID
    name: str
    permission: PermissionOption
    serie_number: str or None
    last_authorization: str or None
    expire_time: ExpireTimeOption
    created_at: str


class ListDeviceTokenQuery(TypedDict):
    page: Union[int, float]
    """
    Page of list starting from 1
    """
    amount: Union[int, float]
    """
    Amount of items will return.
    """
    fields: list[
        Literal[
            "token",
            "device_id",
            "network_id",
            "name",
            "permission",
            "serie_number",
            "last_authorization",
            "expire_time",
            "created_at",
        ]
    ]
    """
    Array of field names.
    """
    filter: DeviceTokenDataList
    """
    Filter object.
    """
    orderBy: Optional[
        list[
            Literal[
                "name",
                "permission",
                "serie_number",
                "last_authorization",
                "created_at",
                "asc",
                "desc",
            ]
        ]
    ]
    """
    Tuple with a field and an order
    """


class DeviceChunkData(TypedDict):
    id: str
    """
    Chunk ID in format 'from_to' (Unix timestamps).
    """
    from_date: str
    """
    Start date of the chunk (ISO 8601).
    """
    to_date: str
    """
    End date of the chunk (ISO 8601).
    """
    amount: Union[int, float]
    """
    Amount of data records in the chunk.
    """


class DeviceDataBackup(TypedDict):
    deviceID: GenericID
    """
    Device ID.
    """
    file_address: str
    """
    File path in TagoIO Files where backup will be saved.
    Can use template variables: $DEVICE$, $CHUNK$, $FROM$, $TO$, $TIMESTAMP$.
    """
    headers: Optional[bool]
    """
    Include CSV headers in the exported file.
    """


class DeviceDataBackupResponse(TypedDict):
    file_address: str
    """
    Final file path where the backup was saved.
    """
    chunk_id: Optional[str]
    """
    Chunk ID if backup was for a specific chunk.
    """


class DeviceDataRestore(TypedDict):
    deviceID: GenericID
    """
    Device ID.
    """
    file_address: str
    """
    File path in TagoIO Files to restore data from (CSV format).
    """


class DeviceStatisticsQuery(TypedDict, total=False):
    periodicity: Literal["hour", "day", "month"]
    """
    Interval between items (default: "hour"). Also sets the default range and the longest range allowed:
    1 month for "hour", 3 months for "day", and 12 months for "month".
    """
    start_date: Union[str, datetime]
    """
    Start of the range. Send it together with end_date. If either one is missing, the default range
    for periodicity is used: the last 24 hours for "hour", the last 3 months for "day",
    and the last 12 months for "month".
    """
    end_date: Union[str, datetime]
    """
    End of the range. Must not be before start_date.
    """
    timezone: str
    """
    IANA timezone used to read start_date and end_date as local times (default: "UTC").
    Send the dates as strings without a UTC offset when you set it.
    """


class DeviceStatistic(TypedDict, total=False):
    time: datetime
    """
    When the counters were recorded.
    """
    device_input: Union[int, float]
    """
    Data records added to the device since the start of the month. Missing when there was no input this month.
    """
    device_output: Union[int, float]
    """
    Data records returned by the device since the start of the month. Missing when there was no output this month.
    """
