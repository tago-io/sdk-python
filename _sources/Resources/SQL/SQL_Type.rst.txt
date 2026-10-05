**SQL Type**
============


.. _SQLParam:

SQLParam
--------

    **Attributes:**

        | key: str
        | Positional parameter placeholder, such as ``$1``.

        | value: str
        | Value bound to the placeholder.


.. _SQLCreateInfo:

SQLCreateInfo
-------------

    **Attributes:**

        | name: str
        | Name of the query. Required on create and replace.

        | query: str
        | TagoSQL query text. Required on create and replace.

        | description: Optional[str]
        | Human-readable description of the query.

        | params: Optional[List[:ref:`SQLParam`]]
        | Default positional parameters.

        | cache_enabled: Optional[bool]
        | Whether execution results are cached.

        | cache_ttl_seconds: Optional[int]
        | Cache time-to-live in seconds.

        | rate_limit_rpm: Optional[int]
        | Execution rate limit in requests per minute.

        | active: Optional[bool]
        | Whether the query is active.

        | tags: Optional[List[:ref:`TagsObj`]]
        | List of tags associated with the query.


.. _SQLInfo:

SQLInfo
-------

    **Attributes:**

        | id: :ref:`GenericID`
        | Unique identifier for the query.

        | name: str
        | Name of the query.

        | description: Optional[str]
        | Human-readable description of the query.

        | query: str
        | TagoSQL query text.

        | params: Optional[List[:ref:`SQLParam`]]
        | Default positional parameters.

        | cache_enabled: Optional[bool]
        | Whether execution results are cached.

        | cache_ttl_seconds: Optional[int]
        | Cache time-to-live in seconds.

        | rate_limit_rpm: Optional[int]
        | Execution rate limit in requests per minute.

        | active: Optional[bool]
        | Whether the query is active.

        | tags: Optional[List[:ref:`TagsObj`]]
        | List of tags associated with the query.

        | version: int
        | Current stored version number.

        | cache_version: int
        | Cache generation counter, bumped when cached results are invalidated.

        | versions: Dict[str, Any]
        | Mapping of version number to stored snapshot metadata.

        | created_at: datetime
        | Date and time when the query was created.

        | updated_at: datetime
        | Date and time when the query was last updated.

        | session_context: bool
        | Read-only. True when the query text uses session functions. Never accepted as input.


.. _SQLFilter:

SQLFilter
---------

    **Attributes:**

        | name: str
        | Name to filter queries by.

        | active: bool
        | Active state to filter queries by.

        | tags: Optional[List[:ref:`TagsObj`]]
        | Tags to filter queries by.


.. _SQLQuery:

SQLQuery(:ref:`Query`)
----------------------

    **Attributes:**

        | fields: Optional[List[Literal["id", "name", "description", "query", "params", "cache_enabled", "cache_ttl_seconds", "rate_limit_rpm", "active", "tags", "version", "created_at", "updated_at"]]]
        | List of fields to include in the query results.

        | filter: Optional[:ref:`SQLFilter`]
        | Filter criteria for the query.


.. _SQLExecuteObj:

SQLExecuteObj
-------------

    **Attributes:**

        | params: Optional[List[:ref:`SQLParam`]]
        | Positional parameters overriding the saved defaults per key.

        | test: Optional[bool]
        | When True, skips the result cache entirely.

        | after_device: Optional[:ref:`GenericID`]
        | Device ID used to resolve session context for the execution.


.. _SQLColumn:

SQLColumn
---------

    **Attributes:**

        | name: str
        | Column name.

        | type: Literal["string", "number", "timestamp", "boolean", "json"]
        | Column data type.


.. _SQLExecuteResult:

SQLExecuteResult
----------------

    **Attributes:**

        | columns: List[:ref:`SQLColumn`]
        | Result columns with their types.

        | rows: List[dict]
        | Result rows keyed by column name.

        | row_count: int
        | Number of rows returned.

        | execution_ms: int
        | Server-side execution time in milliseconds.

        | served_from_cache: bool
        | True when the result was served from the cache.


.. _SQLVersionInfo:

SQLVersionInfo
--------------

    **Attributes:**

        | query: str
        | Query text stored in this version.

        | params: List[:ref:`SQLParam`]
        | Parameters stored in this version.

        | created_at: Optional[datetime]
        | Date and time when this version was stored.


.. _SQLTableInfo:

SQLTableInfo
------------

    **Attributes:**

        | function: str
        | Virtual table family function name.

        | label: str
        | Human-readable label.

        | tag_form: Optional[str]
        | Tag form used to resolve the table.

        | columns: List[:ref:`SQLColumn`]
        | Typed columns exposed by the table.

        | dynamic: Optional[bool]
        | Whether the table columns are resolved dynamically.


.. _SQLResourceItem:

SQLResourceItem
---------------

    **Attributes:**

        | id: :ref:`GenericID`
        | Resource identifier.

        | name: str
        | Resource name.


.. _SQLFunctionInfo:

SQLFunctionInfo
---------------

    **Attributes:**

        | name: str
        | Function name.

        | kind: Literal["aggregate", "session"]
        | Function category.

        | args: List[str]
        | Argument names.

        | description: str
        | Human-readable description.

        | example: Optional[str]
        | Present only on session functions; carries the COALESCE authoring idiom.


.. _SQLTablesResources:

SQLTablesResources
------------------

    **Attributes:**

        | devices: List[:ref:`SQLResourceItem`]
        | Profile devices available to queries.

        | entities: List[:ref:`SQLResourceItem`]
        | Profile entities available to queries.


.. _SQLTablesResult:

SQLTablesResult
---------------

    **Attributes:**

        | tables: List[:ref:`SQLTableInfo`]
        | Virtual table families with their typed columns.

        | resources: :ref:`SQLTablesResources`
        | Profile devices and entities.

        | functions: List[:ref:`SQLFunctionInfo`]
        | Aggregate and session functions available to queries.


.. _SQLTablesQuery:

SQLTablesQuery
--------------

    **Attributes:**

        | filter: Optional[str]
        | Substring filter applied to the catalog.

        | amount: Optional[int]
        | Number of items per page.

        | page: Optional[int]
        | Page number.

        | entity_id: Optional[:ref:`GenericID`]
        | Entity ID used to resolve one entity's columns.
