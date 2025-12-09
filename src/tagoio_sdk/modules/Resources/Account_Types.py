from datetime import datetime
from typing import Literal
from typing import Optional
from typing import TypedDict

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


class AccountCreateInfo(TypedDict, total=False):
    name: str
    email: str
    password: str
    cpassword: str
    country: Optional[str]
    timezone: str
    company: Optional[str]
    newsletter: Optional[bool]
    developer: Optional[bool]


OTPType = Literal["sms", "email", "authenticator"]


class TokenCreateInfo(TypedDict):
    profile_id: GenericID
    email: str
    password: str
    pin_code: str
    otp_type: OTPType
    name: str


class LoginCredentials(TypedDict):
    email: str
    password: str
    otp_type: OTPType
    pin_code: str


class ProfileListInfoForLogin(TypedDict):
    id: GenericID
    name: str


class LoginResponse(TypedDict):
    type: str
    id: GenericID
    email: str
    company: str
    name: str
    profiles: list[ProfileListInfoForLogin]
