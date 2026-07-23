**SQL**
=======

Manage and run TagoSQL queries on your profile.

=======
list
=======

Retrieves a list with all TagoSQL queries from the profile.

See: `TagoSQL Queries <https://docs.tago.io/docs/tagoio/tagosql/queries>`_

    **Parameters:**

        | *Optional* **queryObj**: :ref:`SQLQuery`
        | Query parameters to filter the results.

        .. code-block::
            :caption: **Default queryObj:**

            queryObj = {
                "page": 1,
                "fields": ["id", "name", "tags"],
                "filter": {},
                "amount": 20
            }

    **Returns:**

        | list[:ref:`SQLInfo`]

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "SQL Query" / "Access" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.sql.list({
            "page": 1,
            "fields": ["id", "name", "tags"],
            "amount": 20
        })
        print(result)  # [ { 'id': 'query-id-123', 'name': 'My query', ... } ]


=======
create
=======

Creates a new TagoSQL query on the profile.

See: `TagoSQL Queries <https://docs.tago.io/docs/tagoio/tagosql/queries>`_

    **Parameters:**

        | **sqlObj**: :ref:`SQLCreateInfo`
        | Query definition.

    **Returns:**

        | :ref:`SQLInfo`

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.sql.create({
            "name": "Latest temperature",
            "query": "SELECT variable, value, time FROM device($1) AS d WHERE variable = 'temperature' ORDER BY time DESC LIMIT 10",
            "params": [{"key": "$1", "value": "my-device-id"}]
        })
        print(result)  # { 'id': 'query-id-123', 'name': 'Latest temperature', ... }


=======
info
=======

Retrieves detailed information about a specific TagoSQL query.

See: `TagoSQL Queries <https://docs.tago.io/docs/tagoio/tagosql/queries>`_

    **Parameters:**

        | **sqlID**: str
        | Query ID.

    **Returns:**

        | :ref:`SQLInfo`

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "SQL Query" / "Access" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.sql.info("query-id-123")
        print(result)  # { 'id': 'query-id-123', 'name': 'My query', 'query': 'SELECT ...', ... }


=======
edit
=======

Replaces a TagoSQL query. The query is re-validated and its cached results are dropped; a new version is stored when the query or the params change.

See: `TagoSQL Queries <https://docs.tago.io/docs/tagoio/tagosql/queries>`_

    **Parameters:**

        | **sqlID**: str
        | Query ID.

        | **sqlObj**: :ref:`SQLCreateInfo`
        | New query definition.

    **Returns:**

        | :ref:`SQLInfo`

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.sql.edit("query-id-123", {
            "name": "Latest temperature",
            "query": "SELECT variable, value, time FROM device($1) AS d ORDER BY time DESC LIMIT 20",
            "params": [{"key": "$1", "value": "my-device-id"}]
        })
        print(result)  # { 'id': 'query-id-123', 'version': 2, ... }


=======
delete
=======

Deletes a TagoSQL query from the profile.

See: `TagoSQL Queries <https://docs.tago.io/docs/tagoio/tagosql/queries>`_

    **Parameters:**

        | **sqlID**: str
        | Query ID.

    **Returns:**

        | dict[str, str]

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.sql.delete("query-id-123")
        print(result)  # { 'id': 'query-id-123' }


==========
getVersion
==========

Retrieves a historical snapshot (query and params) of a TagoSQL query. To restore it, send the snapshot's query and params back with ``edit``.

See: `TagoSQL Queries <https://docs.tago.io/docs/tagoio/tagosql/queries>`_

    **Parameters:**

        | **sqlID**: str
        | Query ID.

        | **version**: int
        | Version number to retrieve.

    **Returns:**

        | :ref:`SQLVersionInfo`

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.sql.getVersion("query-id-123", 1)
        print(result)  # { 'query': 'SELECT ...', 'params': [], 'created_at': ... }


=======
execute
=======

Executes a TagoSQL query. Params sent here override the saved defaults per key; ``test: True`` skips the result cache entirely.

See: `Executing Queries <https://docs.tago.io/docs/tagoio/tagosql/executing-queries>`_

    **Parameters:**

        | **sqlID**: str
        | Query ID.

        | *Optional* **executeObj**: :ref:`SQLExecuteObj`
        | Execution options.

    **Returns:**

        | :ref:`SQLExecuteResult`

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "SQL Query" / "Execute" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.sql.execute("query-id-123", {
            "params": [{"key": "$1", "value": "my-device-id"}]
        })
        print(result)  # { 'columns': [...], 'rows': [...], 'row_count': 1, ... }


=======
tables
=======

Retrieves the TagoSQL schema discovery catalog: the virtual table families with their typed columns, plus the profile's devices and entities. Pass ``entity_id`` to resolve one entity's columns.

See: `Available Tables <https://docs.tago.io/docs/tagoio/tagosql/tables>`_

    **Parameters:**

        | *Optional* **queryObj**: :ref:`SQLTablesQuery`
        | Query parameters to filter the catalog.

    **Returns:**

        | :ref:`SQLTablesResult`

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.sql.tables({"filter": "sensor", "amount": 20})
        print(result)  # { 'tables': [...], 'resources': { 'devices': [...], 'entities': [...] } }

.. toctree::


.. toctree::

    SQL_Type
