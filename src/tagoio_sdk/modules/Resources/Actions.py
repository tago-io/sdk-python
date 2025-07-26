from typing import Dict
from typing import List
from typing import Optional

from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Resources.Actions_Types import ActionCreateInfo
from tagoio_sdk.modules.Resources.Actions_Types import ActionInfo
from tagoio_sdk.modules.Resources.Actions_Types import ActionQuery
from tagoio_sdk.modules.Utils.dateParser import dateParser
from tagoio_sdk.modules.Utils.dateParser import dateParserList


class Actions(TagoIOModule):
    def list(self, queryObj: Optional[ActionQuery] = None) -> List[ActionInfo]:
        """
        @description:
            Lists all actions from the application with pagination support.
            Use this to retrieve and manage actions in your application.

        @see:
            https://help.tago.io/portal/en/kb/tagoio/actions Actions

        @example:
            If receive an error "Authorization Denied", check policy **Action** / **Access** in Access Management.
            ```python
            resources = Resources()
            list_result = resources.actions.list({
                "page": 1,
                "fields": ["id", "name"],
                "amount": 10,
                "orderBy": ["name", "asc"]
            })
            print(list_result)  # [{'id': '66ab7c62e5f0db000998ce42', 'name': 'Action Test', ...}]
            ```
        """
        queryObj = queryObj or {}

        if "orderBy" in queryObj:
            orderBy = f"{queryObj['orderBy'][0]},{queryObj['orderBy'][1]}"
        else:
            orderBy = "name,asc"

        result = self.doRequest(
            {
                "path": "/action",
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

        result = dateParserList(result, ["created_at", "updated_at", "last_triggered"])

        return result

    def create(self, actionObj: ActionCreateInfo) -> Dict[str, str]:
        """
        @description:
            Creates a new action in your application.

        @see:
            https://help.tago.io/portal/en/kb/tagoio/actions Actions

        @example:
            If receive an error "Authorization Denied", check policy **Action** / **Create** in Access Management.
            ```python
            resources = Resources()
            new_action = resources.actions.create({
                "name": "My Action",
                "type": "condition",
                "action": {
                    "script": ["analysis-id"],
                    "type": "script"
                },
                "tags": [{"key": "type", "value": "notification"}]
            })
            print(new_action["action"])  # action-id-123
            ```
        """
        {("is" if k == "is_" else k): v for k, v in actionObj.items()}
        result = self.doRequest(
            {
                "path": "/action",
                "method": "POST",
                "body": actionObj,
            }
        )

        return result

    def edit(self, actionID: GenericID, actionObj: Dict) -> str:
        """
        @description:
            Modifies an existing action.

        @see:
            https://help.tago.io/portal/en/kb/tagoio/actions Actions

        @example:
            If receive an error "Authorization Denied", check policy **Action** / **Edit** in Access Management.
            ```python
            resources = Resources()
            result = resources.actions.edit("action-id-123", {
                "name": "Updated Action",
                "active": False
            })
            print(result)  # Successfully Updated
            ```
        """
        result = self.doRequest(
            {
                "path": f"/action/{actionID}",
                "method": "PUT",
                "body": actionObj,
            }
        )

        return result

    def delete(self, actionID: GenericID) -> str:
        """
        @description:
            Deletes an action from your application.

        @see:
            https://help.tago.io/portal/en/kb/tagoio/actions Actions

        @example:
            If receive an error "Authorization Denied", check policy **Action** / **Delete** in Access Management.
            ```python
            resources = Resources()
            result = resources.actions.delete("action-id-123")
            print(result)  # Successfully Removed
            ```
        """
        result = self.doRequest(
            {
                "path": f"/action/{actionID}",
                "method": "DELETE",
            }
        )

        return result

    def info(self, actionID: GenericID) -> ActionInfo:
        """
        @description:
            Retrieves detailed information about a specific action.

        @see:
            https://help.tago.io/portal/en/kb/tagoio/actions Actions

        @example:
            If receive an error "Authorization Denied", check policy **Action** / **Access** in Access Management.
            ```python
            resources = Resources()
            action_info = resources.actions.info("action-id-123")
            print(action_info)  # {'id': 'action-id-123', 'name': 'My Action', ...}
            ```
        """
        result = self.doRequest(
            {
                "path": f"/action/{actionID}",
                "method": "GET",
            }
        )

        result = dateParser(result, ["created_at", "updated_at", "last_triggered"])

        return result
