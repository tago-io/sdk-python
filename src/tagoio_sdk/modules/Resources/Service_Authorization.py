from typing import List
from typing import Optional

from tagoio_sdk.common.Common_Type import TokenData
from tagoio_sdk.common.Common_Type import TokenDataList
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Resources.Service_Authorization_Types import GenericToken
from tagoio_sdk.modules.Resources.Service_Authorization_Types import (
    ServiceAuthorizationQuery,
)
from tagoio_sdk.modules.Resources.Service_Authorization_Types import TokenCreateResponse
from tagoio_sdk.modules.Utils.dateParser import dateParserList


class ServiceAuthorization(TagoIOModule):
    def tokenList(self, query: Optional[ServiceAuthorizationQuery] = None) -> List[TokenDataList]:
        """
        @description:
            Retrieves a paginated list of all service authorization tokens with filtering and sorting options.

        @see:
            https://help.tago.io/portal/en/kb/articles/218-authorization Authorization

        @example:
            If receive an error "Authorization Denied", check policy **Service Authorization** / **Access** in Access Management.
            ```python
            resources = Resources()
            result = resources.serviceAuthorization.tokenList({
                "page": 1,
                "fields": ["name", "token", "verification_code"],
                "amount": 20
            })
            print(result)  # [ { 'name': 'API Service Token', 'token': 'token-xyz-123' } ]
            ```
        """
        query = query or {}

        orderBy = "created_at,desc"
        if "orderBy" in query:
            orderBy = f"{query['orderBy'][0]},{query['orderBy'][1]}"

        result = self.doRequest(
            {
                "path": "/serviceauth",
                "method": "GET",
                "params": {
                    "page": query.get("page", 1),
                    "fields": query.get("fields", ["name", "token"]),
                    "filter": query.get("filter", {}),
                    "amount": query.get("amount", 20),
                    "orderBy": orderBy,
                },
            }
        )

        result = dateParserList(result, ["created_at", "last_authorization", "expire_time"])

        return result

    def tokenCreate(self, tokenParams: TokenData) -> TokenCreateResponse:
        """
        @description:
            Generates and retrieves a new service authorization token with specified permissions.

        @see:
            https://help.tago.io/portal/en/kb/articles/218-authorization Authorization

        @example:
            If receive an error "Authorization Denied", check policy **Service Authorization** / **Create** in Access Management.
            ```python
            resources = Resources()
            result = resources.serviceAuthorization.tokenCreate({
                "name": "Service Token",
                "verification_code": "additional parameter"
            })
            print(result)  # { 'token': 'token-xyz-123', 'name': 'Service Token', ... }
            ```
        """
        result = self.doRequest(
            {
                "path": "/serviceauth",
                "method": "POST",
                "body": tokenParams,
            }
        )

        return result

    def tokenDelete(self, token: GenericToken) -> str:
        """
        @description:
            Permanently removes a service authorization token.

        @see:
            https://help.tago.io/portal/en/kb/articles/218-authorization Authorization

        @example:
            If receive an error "Authorization Denied", check policy **Service Authorization** / **Delete** in Access Management.
            ```python
            resources = Resources()
            result = resources.serviceAuthorization.tokenDelete("token-xyz-123")
            print(result)  # Token Successfully Removed
            ```
        """
        result = self.doRequest(
            {
                "path": f"/serviceauth/{token}",
                "method": "DELETE",
            }
        )

        return result

    def tokenEdit(self, token: GenericToken, verificationCode: Optional[str] = None) -> str:
        """
        @description:
            Updates a service authorization token with an optional verification code.

        @see:
            https://help.tago.io/portal/en/kb/articles/218-authorization Authorization

        @example:
            If receive an error "Authorization Denied", check policy **Service Authorization** / **Edit** in Access Management.
            ```python
            resources = Resources()
            result = resources.serviceAuthorization.tokenEdit("token-xyz-123", "verification-code")
            print(result)  # Authorization Code Successfully Updated
            ```
        """
        result = self.doRequest(
            {
                "path": f"/serviceauth/{token}",
                "method": "PUT",
                "body": {
                    "verification_code": verificationCode,
                },
            }
        )

        return result
