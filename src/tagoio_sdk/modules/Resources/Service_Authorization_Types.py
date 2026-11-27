from typing import List
from typing import Literal
from typing import Optional
from typing import TypedDict

from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.Common_Type import Query
from tagoio_sdk.common.Common_Type import TokenData
from tagoio_sdk.common.Common_Type import TokenDataList


GenericToken = str
"""Token used on TagoIO, string with 34 characters"""


class ServiceAuthorizationCreateInfo(TokenData, total=False):
    analysis: Optional[GenericID]
    """
    [Optional] Luau Analysis whose MQTT Endpoint this authorization connects devices to.
    Set at creation only; it cannot change later.
    """


class TokenCreateResponse(TypedDict):
    token: GenericToken
    name: str
    profile: GenericID
    verification_code: Optional[str]
    """[Optional] Verification code to validate middleware requests."""


class ServiceAuthorizationListItem(TokenDataList, total=False):
    analysis: Optional[GenericID]
    """Luau Analysis the authorization is bound to for the MQTT Endpoint, or None."""


class ServiceAuthorizationFilter(TypedDict, total=False):
    name: str
    token: GenericToken
    analysis: GenericID
    """Only the authorizations bound to this Analysis."""


class ServiceAuthorizationQuery(Query):
    fields: Optional[
        List[Literal["name", "token", "verification_code", "created_at", "analysis"]]
    ]
    filter: Optional[ServiceAuthorizationFilter]
