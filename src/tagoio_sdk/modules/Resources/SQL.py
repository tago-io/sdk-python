from typing import Dict
from typing import List
from typing import Optional
from urllib.parse import quote

from tagoio_sdk.common import Cache
from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Resources.SQL_Types import SQLCreateInfo
from tagoio_sdk.modules.Resources.SQL_Types import SQLExecuteObj
from tagoio_sdk.modules.Resources.SQL_Types import SQLExecuteResult
from tagoio_sdk.modules.Resources.SQL_Types import SQLInfo
from tagoio_sdk.modules.Resources.SQL_Types import SQLParam
from tagoio_sdk.modules.Resources.SQL_Types import SQLQuery
from tagoio_sdk.modules.Resources.SQL_Types import SQLTablesQuery
from tagoio_sdk.modules.Resources.SQL_Types import SQLTablesResult
from tagoio_sdk.modules.Resources.SQL_Types import SQLVersionInfo
from tagoio_sdk.modules.Utils.dateParser import dateParser
from tagoio_sdk.modules.Utils.dateParser import dateParserList


class SQL(TagoIOModule):
    def list(self, queryObj: Optional[SQLQuery] = None) -> List[SQLInfo]:
        """
        @description:
            Retrieves a list with all TagoSQL queries from the profile.

        @see:
            https://docs.tago.io/docs/tagoio/tagosql/queries TagoSQL Queries

        @example:
            If receive an error "Authorization Denied", check policy **SQL Query** / **Access** in Access Management.
            ```python
            resources = Resources()
            result = resources.sql.list({
                "page": 1,
                "fields": ["id", "name", "tags"],
                "amount": 20,
            })
            print(result)  # [{'id': 'query-id-123', 'name': 'My query', ...}]
            ```
        """
        queryObj = queryObj or {}
        params = {
            "page": queryObj.get("page", 1),
            "fields": queryObj.get("fields", ["id", "name", "tags"]),
            "filter": queryObj.get("filter", {}),
            "amount": queryObj.get("amount", 20),
        }
        if "orderBy" in queryObj:
            params["orderBy"] = f"{queryObj['orderBy'][0]},{queryObj['orderBy'][1]}"

        result = self.doRequest(
            {
                "path": "/sql",
                "method": "GET",
                "params": params,
            }
        )
        return dateParserList(result, ["created_at", "updated_at"])

    def create(self, sqlObj: SQLCreateInfo) -> SQLInfo:
        """
        @description:
            Creates a new TagoSQL query on the profile. Requires a profile token
            (or an analysis token granted **Create** in Access Management).

        @see:
            https://docs.tago.io/docs/tagoio/tagosql/queries TagoSQL Queries

        @example:
            ```python
            resources = Resources()
            result = resources.sql.create({
                "name": "Latest temperature",
                "query": "SELECT variable, value, time FROM device($1) AS d WHERE variable = 'temperature' ORDER BY time DESC LIMIT 10",
                "params": [{"key": "$1", "value": "my-device-id"}],
            })
            print(result)  # {'id': 'query-id-123', 'name': 'Latest temperature', ...}
            ```
        """
        result = self.doRequest(
            {
                "path": "/sql",
                "method": "POST",
                "body": sqlObj,
            }
        )
        Cache.clear_cache()
        return dateParser(result, ["created_at", "updated_at"])

    def info(self, sqlID: GenericID) -> SQLInfo:
        """
        @description:
            Retrieves detailed information about a specific TagoSQL query.

        @see:
            https://docs.tago.io/docs/tagoio/tagosql/queries TagoSQL Queries

        @example:
            If receive an error "Authorization Denied", check policy **SQL Query** / **Access** in Access Management.
            ```python
            resources = Resources()
            result = resources.sql.info("query-id-123")
            print(result)  # {'id': 'query-id-123', 'name': 'My query', 'query': 'SELECT ...', ...}
            ```
        """
        result = self.doRequest(
            {
                "path": f"/sql/{sqlID}",
                "method": "GET",
            }
        )
        return dateParser(result, ["created_at", "updated_at"])

    def edit(self, sqlID: GenericID, sqlObj: SQLCreateInfo) -> SQLInfo:
        """
        @description:
            Replaces a TagoSQL query. The query is re-validated and its cached
            results are dropped; a new version is stored when the query or the
            params change.

        @see:
            https://docs.tago.io/docs/tagoio/tagosql/queries TagoSQL Queries

        @example:
            ```python
            resources = Resources()
            result = resources.sql.edit("query-id-123", {
                "name": "Latest temperature",
                "query": "SELECT variable, value, time FROM device($1) AS d ORDER BY time DESC LIMIT 20",
                "params": [{"key": "$1", "value": "my-device-id"}],
            })
            print(result)  # {'id': 'query-id-123', 'version': 2, ...}
            ```
        """
        result = self.doRequest(
            {
                "path": f"/sql/{sqlID}",
                "method": "PUT",
                "body": sqlObj,
            }
        )
        Cache.clear_cache()
        return dateParser(result, ["created_at", "updated_at"])

    def delete(self, sqlID: GenericID) -> Dict[str, str]:
        """
        @description:
            Deletes a TagoSQL query from the profile.

        @see:
            https://docs.tago.io/docs/tagoio/tagosql/queries TagoSQL Queries

        @example:
            ```python
            resources = Resources()
            result = resources.sql.delete("query-id-123")
            print(result)  # {'id': 'query-id-123'}
            ```
        """
        result = self.doRequest(
            {
                "path": f"/sql/{sqlID}",
                "method": "DELETE",
            }
        )
        Cache.clear_cache()
        return result

    def getVersion(self, sqlID: GenericID, version: int) -> SQLVersionInfo:
        """
        @description:
            Retrieves a historical snapshot (query and params) of a TagoSQL query.
            To restore it, send the snapshot's query and params back with `edit`.

        @see:
            https://docs.tago.io/docs/tagoio/tagosql/queries TagoSQL Queries

        @example:
            ```python
            resources = Resources()
            result = resources.sql.getVersion("query-id-123", 1)
            print(result)  # {'query': 'SELECT ...', 'params': [], 'created_at': ...}
            ```
        """
        result = self.doRequest(
            {
                "path": f"/sql/{sqlID}/version/{version}",
                "method": "GET",
            }
        )
        return dateParser(result, ["created_at"])

    def execute(
        self, sqlID: GenericID, executeObj: Optional[SQLExecuteObj] = None
    ) -> SQLExecuteResult:
        """
        @description:
            Executes a TagoSQL query. Params sent here override the saved
            defaults per key; `test: True` skips the result cache entirely.

        @see:
            https://docs.tago.io/docs/tagoio/tagosql/executing-queries Executing Queries

        @example:
            If receive an error "Authorization Denied", check policy **SQL Query** / **Execute** in Access Management.
            ```python
            resources = Resources()
            result = resources.sql.execute("query-id-123", {
                "params": [{"key": "$1", "value": "my-device-id"}],
            })
            print(result)  # {'columns': [...], 'rows': [...], 'row_count': 1, ...}
            ```
        """
        return self.doRequest(
            {
                "path": f"/sql/{sqlID}/execute",
                "method": "POST",
                "body": executeObj or {},
            }
        )

    def executeAdhoc(
        self, query: str, params: Optional[List[SQLParam]] = None
    ) -> SQLExecuteResult:
        """
        @description:
            Runs a one-off TagoSQL query without storing it. Profile token only;
            results are never cached. Store queries you run regularly with `create`.

        @see:
            https://docs.tago.io/docs/tagoio/tagosql/executing-queries Executing Queries

        @example:
            ```python
            resources = Resources()
            result = resources.sql.executeAdhoc(
                "SELECT variable, value FROM device($1) AS d WHERE value > $2 LIMIT 10",
                [{"key": "$1", "value": "my-device-id"}, {"key": "$2", "value": "25"}],
            )
            print(result)  # {'columns': [...], 'rows': [...], 'row_count': 3, ...}
            ```
        """
        return self.doRequest(
            {
                "path": "/sql/execute",
                "method": "POST",
                "body": {"query": query, "params": params or []},
            }
        )

    def tables(self, queryObj: Optional[SQLTablesQuery] = None) -> SQLTablesResult:
        """
        @description:
            Retrieves the TagoSQL schema discovery catalog: the virtual table
            families with their typed columns, plus the profile's devices and
            entities. Pass `entity_id` to resolve one entity's columns.

        @see:
            https://docs.tago.io/docs/tagoio/tagosql/tables Available Tables

        @example:
            ```python
            resources = Resources()
            result = resources.sql.tables({"filter": "sensor", "amount": 20})
            print(result)  # {'tables': [...], 'resources': {'devices': [...], 'entities': [...]}}
            ```
        """
        queryObj = queryObj or {}
        # ? doRequest expands object filters into filter[...] pairs; this
        # ? endpoint's filter is a plain substring, so it goes on the path.
        params = {key: value for key, value in queryObj.items() if key != "filter"}
        path = "/sql/tables"
        if "filter" in queryObj:
            path = f"/sql/tables?filter={quote(str(queryObj['filter']))}"
        return self.doRequest(
            {
                "path": path,
                "method": "GET",
                "params": params,
            }
        )
