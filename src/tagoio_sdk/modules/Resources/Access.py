from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Resources.Access_Types import AccessCreateInfo
from tagoio_sdk.modules.Resources.Access_Types import AccessInfo
from tagoio_sdk.modules.Resources.Access_Types import AccessQuery
from tagoio_sdk.modules.Utils.dateParser import dateParser
from tagoio_sdk.modules.Utils.dateParser import dateParserList


class Access(TagoIOModule):
    def list(self, queryObj: AccessQuery = None) -> list[AccessInfo]:
        """
        @description:
            Lists all access rules from the application with pagination support.
            Use this to retrieve and manage access policies for your application.

        @see:
            https://help.tago.io/portal/en/kb/articles/183-access-management Access Management

        @example:
            If you receive an error "Authorization Denied", check policy **Access Management** / **Access** in Access Management.
            ```python
            resources = Resources()
            result = resources.access.list({
                "page": 1,
                "fields": ["id", "name"],
                "amount": 10,
                "orderBy": ["name", "asc"]
            })
            print(result)  # [{'id': 'access-id-123', 'name': '[Analysis] - Test'}, ...]
            ```
        """
        if queryObj is None:
            queryObj = {}
        result = self.doRequest(
            {
                "path": "/am",
                "method": "GET",
                "params": {
                    "page": queryObj.get("page") or 1,
                    "fields": queryObj.get("fields") or ["id", "name", "tags"],
                    "filter": queryObj.get("filter") or {},
                    "amount": queryObj.get("amount") or 20,
                    "orderBy": (
                        f"{queryObj['orderBy'][0]},{queryObj['orderBy'][1]}" if queryObj.get("orderBy") else "name,asc"
                    ),
                },
            }
        )
        result = dateParserList(result, ["created_at", "updated_at"])

        return result

    def create(self, accessObj: AccessCreateInfo) -> dict:
        """
        @description:
            Creates a new access policy in your application.

        @see:
            https://help.tago.io/portal/en/kb/articles/183-access-management Access Management

        @example:
            If receive an error "Authorization Denied", check policy **Access Management** / **Create** in Access Management.
            ```python
            resources = Resources()
            new_access = resources.access.create({
                "active": True,
                "name": "My Access Policy",
                "permissions": [
                    {
                        "effect": "allow",
                        "action": ["access"],
                        "resource": ["access_management"],
                    },
                ],
                "targets": [["analysis", "id", "analysis-id-123"]],
                "tags": [{"key": "type", "value": "admin"}],
            })
            print(new_access["am_id"])  # access-id-123
            ```
        """
        result = self.doRequest(
            {
                "path": "/am",
                "method": "POST",
                "body": {**accessObj},
            }
        )
        return result

    def edit(self, accessID: str, accessObj: dict) -> str:
        """
        @description:
            Modifies an existing access policy.

        @see:
            https://help.tago.io/portal/en/kb/articles/183-access-management Access Management

        @example:
            If you receive an error "Authorization Denied", check policy **Access Management** / **Edit** in Access Management.
            ```python
            resources = Resources()
            result = resources.access.edit("access-id-123", {
                "name": "Updated Access Policy",
                "permissions": [
                    {
                        "effect": "allow",
                        "action": ["edit"],
                        "resource": ["access_management"],
                    },
                ],
                "tags": [{"key": "type", "value": "user"}]
            })
            print(result)  # Access Management Successfully Updated
            ```
        """
        result = self.doRequest(
            {
                "path": f"/am/{accessID}",
                "method": "PUT",
                "body": {**accessObj},
            }
        )
        return result

    def delete(self, accessID: str) -> str:
        """
        @description:
            Removes an access policy from your application.

        @see:
            https://help.tago.io/portal/en/kb/articles/183-access-management Access Management

        @example:
            If you receive an error "Authorization Denied", check policy **Access Management** / **Delete** in Access Management.
            ```python
            resources = Resources()
            result = resources.access.delete("access-id-123")
            print(result)  # Successfully Removed
            ```
        """
        result = self.doRequest(
            {
                "path": f"/am/{accessID}",
                "method": "DELETE",
            }
        )
        return result

    def info(self, accessID: str) -> AccessInfo:
        """
        @description:
            Retrieves detailed information about a specific access policy.

        @see:
            https://help.tago.io/portal/en/kb/articles/183-access-management Access Management

        @example:
            If you receive an error "Authorization Denied", check policy **Access Management** / **Access** in Access Management.
            ```python
            resources = Resources()
            access_info = resources.access.info("access-id-123")
            print(access_info)  # {'id': 'access-id-123', 'name': '[Analysis] - Test', ...}
            ```
        """
        result = self.doRequest(
            {
                "path": f"/am/{accessID}",
                "method": "GET",
            }
        )
        result = dateParser(result, ["created_at", "updated_at"])
        return result
