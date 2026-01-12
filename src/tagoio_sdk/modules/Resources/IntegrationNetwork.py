from typing import Dict
from typing import List
from typing import Optional

from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.Common_Type import GenericToken
from tagoio_sdk.common.Common_Type import TokenCreateResponse
from tagoio_sdk.common.Common_Type import TokenData
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Resources.IntegrationNetworkType import ListTokenQuery
from tagoio_sdk.modules.Resources.IntegrationNetworkType import NetworkCreateInfo
from tagoio_sdk.modules.Resources.IntegrationNetworkType import NetworkInfo
from tagoio_sdk.modules.Resources.IntegrationNetworkType import NetworkQuery
from tagoio_sdk.modules.Resources.IntegrationNetworkType import NetworkTokenInfo
from tagoio_sdk.modules.Utils.dateParser import dateParser
from tagoio_sdk.modules.Utils.dateParser import dateParserList


class Networks(TagoIOModule):
    def listNetwork(self, queryObj: Optional[NetworkQuery] = None) -> List[NetworkInfo]:
        """
        @description:
            Retrieves a list of all networks from the account with pagination support.
            Use this to retrieve and manage networks in your application.

        @see:
            https://docs.tago.io/docs/tagoio/integrations/general/creating-a-network-integration Network Integration

        @example:
            If receive an error "Authorization Denied", check policy **Integration Network** / **Access** in Access Management.
            ```python
            resources = Resources()
            networks = resources.integration.networks.listNetwork({
                "page": 1,
                "fields": ["id", "name"],
                "amount": 20,
                "orderBy": ["name", "asc"]
            })
            print(networks)  # [{'id': 'network-id-123', 'name': 'My Network', ...}]
            ```
        """
        queryObj = queryObj or {}

        if "orderBy" in queryObj:
            orderBy = f"{queryObj['orderBy'][0]},{queryObj['orderBy'][1]}"
        else:
            orderBy = "name,asc"

        result = self.doRequest(
            {
                "path": "/integration/network",
                "method": "GET",
                "params": {
                    "page": queryObj.get("page", 1),
                    "fields": queryObj.get("fields", ["id", "name"]),
                    "filter": queryObj.get("filter", {}),
                    "amount": queryObj.get("amount", 20),
                    "orderBy": orderBy,
                },
            }
        )

        return result

    def info(self, networkID: GenericID, fields: Optional[List[str]] = None) -> NetworkInfo:
        """
        @description:
            Retrieves detailed information about a specific network.

        @see:
            https://docs.tago.io/docs/tagoio/integrations/general/creating-a-network-integration Network Integration

        @example:
            If receive an error "Authorization Denied", check policy **Integration Network** / **Access** in Access Management.
            ```python
            resources = Resources()
            network_info = resources.integration.networks.info("network-id-123")
            print(network_info)  # {'id': '...', 'name': 'My Network', ...}
            ```
        """
        if fields is None:
            fields = ["id", "name"]

        result = self.doRequest(
            {
                "path": f"/integration/network/{networkID}",
                "method": "GET",
                "params": {
                    "fields": fields,
                },
            }
        )

        return result

    def create(self, networkObj: NetworkCreateInfo) -> Dict[str, str]:
        """
        @description:
            Creates a new integration network in the account.

        @see:
            https://docs.tago.io/docs/tagoio/integrations/general/creating-a-network-integration#create-a-new-integration Creating a Network Integration

        @example:
            If receive an error "Authorization Denied", check policy **Integration Network** / **Create** in Access Management.
            ```python
            resources = Resources()
            new_network = resources.integration.networks.create({
                "name": "My Custom Network",
                "description": "Custom integration network",
                "middleware_endpoint": "https://my-middleware.com/endpoint",
                "public": False
            })
            print(new_network)  # {'network': 'network-id-123'}
            ```
        """
        result = self.doRequest(
            {
                "path": "/integration/network",
                "method": "POST",
                "body": networkObj,
            }
        )

        return result

    def edit(self, networkID: GenericID, networkObj: NetworkCreateInfo) -> str:
        """
        @description:
            Modifies any property of an existing network.

        @example:
            If receive an error "Authorization Denied", check policy **Integration Network** / **Edit** in Access Management.
            ```python
            resources = Resources()
            result = resources.integration.networks.edit("network-id-123", {
                "name": "Updated Network Name",
                "description": "Updated description",
                "public": True
            })
            print(result)  # Successfully Updated
            ```
        """
        result = self.doRequest(
            {
                "path": f"/integration/network/{networkID}",
                "method": "PUT",
                "body": networkObj,
            }
        )

        return result

    def delete(self, networkID: GenericID) -> str:
        """
        @description:
            Permanently deletes a network from the account.

        @example:
            If receive an error "Authorization Denied", check policy **Integration Network** / **Delete** in Access Management.
            ```python
            resources = Resources()
            result = resources.integration.networks.delete("network-id-123")
            print(result)  # Successfully Removed
            ```
        """
        result = self.doRequest(
            {
                "path": f"/integration/network/{networkID}",
                "method": "DELETE",
            }
        )

        return result

    def tokenList(self, networkID: GenericID, queryObj: Optional[ListTokenQuery] = None) -> List[NetworkTokenInfo]:
        """
        @description:
            Retrieves a list of all authentication tokens for a network with optional filtering.

        @see:
            https://docs.tago.io/docs/tagoio/integrations/general/creating-a-network-integration#tokens-and-getting-devices Tokens and Getting Devices

        @example:
            If receive an error "Authorization Denied", check policy **Integration Network** / **Access** in Access Management.
            ```python
            resources = Resources()
            tokens = resources.integration.networks.tokenList("network-id-123", {
                "page": 1,
                "amount": 20,
                "fields": ["name", "token", "permission"],
                "orderBy": ["created_at", "desc"]
            })
            print(tokens)  # [{'name': 'Default Token', 'token': '...', 'permission': 'full', ...}]
            ```
        """
        queryObj = queryObj or {}

        if "orderBy" in queryObj:
            orderBy = f"{queryObj['orderBy'][0]},{queryObj['orderBy'][1]}"
        else:
            orderBy = "created_at,desc"

        result = self.doRequest(
            {
                "path": f"/integration/network/token/{networkID}",
                "method": "GET",
                "params": {
                    "page": queryObj.get("page", 1),
                    "fields": queryObj.get("fields", ["name", "token", "permission"]),
                    "filter": queryObj.get("filter", {}),
                    "amount": queryObj.get("amount", 20),
                    "orderBy": orderBy,
                },
            }
        )

        result = dateParserList(result, ["created_at", "updated_at"])

        return result

    def tokenCreate(self, networkID: GenericID, tokenParams: TokenData) -> TokenCreateResponse:
        """
        @description:
            Generates and retrieves a new authentication token for a network.

        @see:
            https://docs.tago.io/docs/tagoio/integrations/general/creating-a-network-integration#tokens-and-getting-devices Tokens and Getting Devices

        @example:
            If receive an error "Authorization Denied", check policy **Integration Network** / **Create Token** in Access Management.
            ```python
            resources = Resources()
            result = resources.integration.networks.tokenCreate("network-id-123", {
                "name": "Production Token",
                "permission": "write",
                "expire_time": "never"
            })
            print(result)  # {'token': 'new-token-value', 'expire_date': None}
            ```
        """
        result = self.doRequest(
            {
                "path": "/integration/network/token",
                "method": "POST",
                "body": {"network": networkID, **tokenParams},
            }
        )

        result = dateParser(result, ["expire_date"])

        return result

    def tokenDelete(self, token: GenericToken) -> str:
        """
        @description:
            Permanently deletes an authentication token.

        @see:
            https://docs.tago.io/docs/tagoio/integrations/general/creating-a-network-integration#tokens-and-getting-devices Tokens and Getting Devices

        @example:
            If receive an error "Authorization Denied", check policy **Integration Network** / **Delete Token** in Access Management.
            ```python
            resources = Resources()
            result = resources.integration.networks.tokenDelete("token-to-delete")
            print(result)  # Successfully Removed
            ```
        """
        result = self.doRequest(
            {
                "path": f"/integration/network/token/{token}",
                "method": "DELETE",
            }
        )

        return result
