from typing import Dict
from typing import List
from typing import Optional

from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Resources.Secrets_Type import SecretsCreate
from tagoio_sdk.modules.Resources.Secrets_Type import SecretsEdit
from tagoio_sdk.modules.Resources.Secrets_Type import SecretsInfo
from tagoio_sdk.modules.Resources.Secrets_Type import SecretsQuery
from tagoio_sdk.modules.Utils.dateParser import dateParser


class Secrets(TagoIOModule):
    def list(self, queryObj: Optional[SecretsQuery] = None) -> List[SecretsInfo]:
        """
        @description:
            Retrieves a paginated list of all secrets stored in the profile with filtering and sorting options.

        @see:
            https://help.tago.io/portal/en/kb/articles/secrets Secrets

        @example:
            If receive an error "Authorization Denied", check policy **Secrets** / **Access** in Access Management.
            ```python
            resources = Resources()
            result = resources.secrets.list({
                "page": 1,
                "fields": ["id", "key"],
                "amount": 20
            })
            print(result)  # [ { 'id': 'secret-id-123', 'key': 'API_KEY' } ]
            ```
        """
        queryObj = queryObj or {}

        orderBy = "key,asc"
        if "orderBy" in queryObj:
            orderBy = f"{queryObj['orderBy'][0]},{queryObj['orderBy'][1]}"

        result = self.doRequest(
            {
                "path": "/secrets",
                "method": "GET",
                "params": {
                    "page": queryObj.get("page", 1),
                    "fields": queryObj.get("fields", ["id", "key"]),
                    "filter": queryObj.get("filter", {}),
                    "amount": queryObj.get("amount", 20),
                    "orderBy": orderBy,
                },
            }
        )

        return result

    def info(self, secretID: GenericID) -> SecretsInfo:
        """
        @description:
            Retrieves detailed information about a specific secret using its ID.

        @see:
            https://help.tago.io/portal/en/kb/articles/secrets Secrets

        @example:
            If receive an error "Authorization Denied", check policy **Secrets** / **Access** in Access Management.
            ```python
            resources = Resources()
            secret_info = resources.secrets.info("secret-id-123")
            print(secret_info)  # { 'id': 'secret-id-123', 'key': 'API_KEY' }
            ```
        """
        result = self.doRequest(
            {
                "path": f"/secrets/{secretID}",
                "method": "GET",
            }
        )

        result = dateParser(result, ["created_at", "updated_at"])

        return result

    def create(self, secretObj: SecretsCreate) -> Dict[str, GenericID]:
        """
        @description:
            Creates a new secret in the profile with the specified key and value.

        @see:
            https://help.tago.io/portal/en/kb/articles/secrets#Creating_a_Secret Creating a Secret

        @example:
            If receive an error "Authorization Denied", check policy **Secrets** / **Create** in Access Management.
            ```python
            resources = Resources()
            result = resources.secrets.create({
                "key": "API_KEY",
                "value": "my-secret-value"
            })
            print(result)  # { 'id': 'secret-id-132' }
            ```
        """
        result = self.doRequest(
            {
                "path": "/secrets",
                "method": "POST",
                "body": {**secretObj},
            }
        )

        return result

    def edit(self, secretID: GenericID, secretObj: SecretsEdit) -> str:
        """
        @description:
            Modifies the properties of an existing secret.

        @see:
            https://help.tago.io/portal/en/kb/articles/secrets Secrets

        @example:
            If receive an error "Authorization Denied", check policy **Secrets** / **Edit** in Access Management.
            ```python
            resources = Resources()
            result = resources.secrets.edit("secret-id-123", {
                "value": "new-secret-value",
                "tags": [{"key": "type", "value": "user"}]
            })
            print(result)  # Successfully Updated
            ```
        """
        result = self.doRequest(
            {
                "path": f"/secrets/{secretID}",
                "method": "PUT",
                "body": {**secretObj},
            }
        )

        return result

    def delete(self, secretID: GenericID) -> str:
        """
        @description:
            Permanently removes a secret from the profile.

        @see:
            https://help.tago.io/portal/en/kb/articles/secrets Secrets

        @example:
            If receive an error "Authorization Denied", check policy **Secrets** / **delete** in Access Management.
            ```python
            resources = Resources()
            result = resources.secrets.delete("secret-id-123")
            print(result)  # Successfully Removed
            ```
        """
        result = self.doRequest(
            {
                "path": f"/secrets/{secretID}",
                "method": "DELETE",
            }
        )

        return result
