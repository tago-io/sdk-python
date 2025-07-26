from typing import Dict
from typing import List
from typing import Optional

from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Resources.IntegrationConnectorType import ConnectorCreateInfo
from tagoio_sdk.modules.Resources.IntegrationConnectorType import ConnectorInfo
from tagoio_sdk.modules.Resources.IntegrationConnectorType import ConnectorQuery
from tagoio_sdk.modules.Utils.dateParser import dateParser
from tagoio_sdk.modules.Utils.dateParser import dateParserList


class Connectors(TagoIOModule):
    def list(self, queryObj: Optional[ConnectorQuery] = None) -> List[ConnectorInfo]:
        """
        @description:
            Lists all connectors from the application with pagination support.

        @see:
            https://help.tago.io/portal/en/kb/articles/466-connector-overview Connector Overview

        @example:
            If receive an error "Authorization Denied", check policy **Connector** / **Access** in Access Management.
            ```python
            resources = Resources()
            result = resources.integration.connectors.list({
              "page": 1,
              "fields": ["id", "name"],
              "amount": 10,
              "orderBy": ["name", "asc"]
            })
            print(result)  # [{'id': 'connector-id-123', 'name': 'My Connector'}, ...]
            ```
        """
        queryObj = queryObj or {}

        orderBy = "name,asc"
        if "orderBy" in queryObj:
            orderBy = f"{queryObj['orderBy'][0]},{queryObj['orderBy'][1]}"

        result = self.doRequest(
            {
                "path": "/integration/connector/",
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

        result = dateParserList(result, ["created_at", "updated_at"])

        return result

    def info(self, connectorID: GenericID, fields: Optional[List[str]] = None) -> ConnectorInfo:
        """
        @description:
            Retrieves detailed information about a specific connector.

        @see:
            https://help.tago.io/portal/en/kb/articles/466-connector-overview Connector Overview

        @example:
            If receive an error "Authorization Denied", check policy **Connector** / **Access** in Access Management.
            ```python
            resources = Resources()
            result = resources.integration.connectors.info("connector-id-123", ["id", "name"])
            print(result)  # {'id': 'connector-id-123', 'name': 'My Connector', 'profile': 'profile-id-123'}
            ```
        """
        result = self.doRequest(
            {
                "path": f"/integration/connector/{connectorID}",
                "method": "GET",
                "params": {
                    "fields": fields,
                },
            }
        )

        result = dateParser(result, ["created_at", "updated_at"])

        return result

    def create(self, connectorObj: ConnectorCreateInfo) -> Dict[str, GenericID]:
        """
        @description:
            Creates a new connector in the application.

        @see:
            https://help.tago.io/portal/en/kb/articles/466-connector-overview#Creating_a_connector Creating a connector

        @example:
            ```python
            resources = Resources()
            result = resources.integration.connectors.create({
              "name": "My Connector",
              "type": "custom",
              "networks": ["network-id-123"],
              "enabled": True
            })
            print(result["connector"])  # 'connector-id-123'
            ```
        """
        result = self.doRequest(
            {
                "path": "/integration/connector/",
                "method": "POST",
                "body": connectorObj,
            }
        )

        return result

    def edit(self, connectorID: GenericID, connectorObj: Dict) -> str:
        """
        @description:
            Modifies an existing connector's properties.

        @see:
            https://help.tago.io/portal/en/kb/articles/466-connector-overview Connector Overview

        @example:
            ```python
            resources = Resources()
            result = resources.integration.connectors.edit("connector-id-123", {"name": "Updated Connector"})
            print(result)  # Connector Successfully Updated
            ```
        """
        result = self.doRequest(
            {
                "path": f"/integration/connector/{connectorID}",
                "method": "PUT",
                "body": connectorObj,
            }
        )

        return result

    def delete(self, connectorID: str) -> str:
        """
        @description:
            Deletes a connector from the application.

        @see:
            https://help.tago.io/portal/en/kb/articles/466-connector-overview Connector Overview

        @example:
            ```python
            resources = Resources()
            result = resources.integration.connectors.delete("connector-id-123")
            print(result)  # Connector Successfully Deleted
            ```
        """
        result = self.doRequest(
            {
                "path": f"/integration/connector/{connectorID}",
                "method": "DELETE",
            }
        )

        return result
