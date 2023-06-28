from datetime import datetime
from typing import Optional, TypedDict

from tagoio_sdk.common.Common_Type import GenericID


class AccountOptions(TypedDict):
    user_view_welcome: bool
    decimal_separator: str
    thousand_separator: str
    last_whats_new: Optional[datetime]


class AccountOpt(TypedDict):
    authenticator: bool
    sms: bool
    email: bool


class AccountInfo(TypedDict):
    active: bool
    name: str
    email: str
    country: Optional[str]
    timezone: str
    company: Optional[str]
    newsletter: Optional[bool]
    developer: Optional[bool]
    blocked: bool
    id: GenericID
    language: str
    last_login: Optional[datetime]
    options: AccountOptions
    phone: Optional[str]
    send_invoice: bool
    stripe_id: Optional[str]
    type: str
    plan: str
    created_at: datetime
    updated_at: datetime
    otp: Optional[AccountOpt]
