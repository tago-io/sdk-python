from typing import List
from typing import Literal
from typing import Optional
from typing import TypedDict

from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.Common_Type import Query


GenericToken = str
"""Token used on TagoIO, string with 34 characters"""


class TokenCreateResponse(TypedDict):
    token: GenericToken
    name: str
    profile: GenericID
    verification_code: Optional[str]
    """[Optional] Verification code to validate middleware requests."""


class ServiceAuthorizationFilter(TypedDict):
    name: str
    token: GenericToken


class ServiceAuthorizationQuery(Query):
    fields: Optional[List[Literal["name", "token", "verification_code", "created_at"]]]
    filter: Optional[ServiceAuthorizationFilter]
