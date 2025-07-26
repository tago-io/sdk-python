from datetime import datetime
from typing import TypedDict
from typing import Union

from tagoio_sdk.common.Common_Type import GenericID


class ProfileListInfo(TypedDict):
    id: GenericID
    name: str
    logo_url: str


class ProfileLimit(TypedDict):
    input: Union[int, float]
    output: Union[int, float]
    sms: Union[int, float]
    email: Union[int, float]
    analysis: Union[int, float]
    data_records: Union[int, float]
    run_users: Union[int, float]
    push_notification: Union[int, float]
    file_storage: Union[int, float]


class ProfileAddOns(TypedDict):
    custom_dns: bool
    """
    Whether the profile has the Custom Domain add-on purchased.
    """
    mobile: bool
    """
    Whether the profile has the Custom Mobile App add-on purchased.
    """


class info(TypedDict):
    id: GenericID
    account: GenericID
    name: str
    logo_url: str
    banner_url: str
    created_at: datetime
    updated_at: datetime


class ProfileInfo(TypedDict):
    info: info
    allocation: ProfileLimit
    addons: ProfileAddOns
    account_plan: str


class amount(TypedDict):
    device: Union[int, float]
    bucket: Union[int, float]
    dashboard: Union[int, float]
    dashboard_shared: Union[int, float]
    analysis: Union[int, float]
    action: Union[int, float]
    am: Union[int, float]
    run_users: Union[int, float]
    dictionary: Union[int, float]
    connectors: Union[int, float]
    networks: Union[int, float]
    tcore: Union[int, float]


class limit_used(TypedDict):
    input: Union[int, float]
    output: Union[int, float]
    analysis: Union[int, float]
    sms: Union[int, float]
    email: Union[int, float]
    data_records: Union[int, float]
    run_users: Union[int, float]
    push_notification: Union[int, float]
    file_storage: Union[int, float]
    tcore: Union[int, float]


class ProfileSummary(TypedDict):
    limit: ProfileLimit
    amount: amount
    limit_used: limit_used
    addons: ProfileAddOns
