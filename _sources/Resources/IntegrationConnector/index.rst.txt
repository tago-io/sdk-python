**Integration Connector**
=========================

Manage connectors in your application.

========
list
========

Lists all connectors from the application with pagination support.

See: `Connector Overview <https://help.tago.io/portal/en/kb/articles/466-connector-overview>`_

    **Parameters:**

        | *Optional* **queryObj**: :ref:`ConnectorQuery`
        | Query parameters to filter the results.

    **Returns:**

        | list[:ref:`ConnectorInfo`]

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.integration.connectors.list({
          "page": 1,
          "fields": ["id", "name"],
          "amount": 10,
          "orderBy": ["name", "asc"]
        })
        print(result)  # [{'id': 'connector-id-123', 'name': 'My Connector'}, ...]


========
info
========

Retrieves detailed information about a specific connector.

See: `Connector Overview <https://help.tago.io/portal/en/kb/articles/466-connector-overview>`_

    **Parameters:**

        | **connectorID**: GenericID: str
        | Connector ID

        | *Optional* **fields**: List[str]
        | List of fields to retrieve

    **Returns:**

        | :ref:`ConnectorInfo`

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.integration.connectors.info("connector-id-123", ["id", "name"])
        print(result)  # {'id': 'connector-id-123', 'name': 'My Connector', 'profile': 'profile-id-123'}


========
create
========

Creates a new connector in the application.

See: `Creating a connector <https://help.tago.io/portal/en/kb/articles/466-connector-overview#Creating_a_connector>`_

    **Parameters:**

        | **connectorObj**: :ref:`ConnectorCreateInfo`
        | Object with connector properties

    **Returns:**

        | dict[str, GenericID]

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.integration.connectors.create({
          "name": "My Connector",
          "type": "custom",
          "networks": ["network-id-123"],
          "enabled": True
        })
        print(result["connector"])  # 'connector-id-123'


========
edit
========

Modifies an existing connector's properties.

See: `Connector Overview <https://help.tago.io/portal/en/kb/articles/466-connector-overview>`_

    **Parameters:**

        | **connectorID**: GenericID: str
        | Connector ID

        | **connectorObj**: Dict
        | Object with properties to update

    **Returns:**

        | str

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.integration.connectors.edit("connector-id-123", {"name": "Updated Connector"})
        print(result)  # Connector Successfully Updated


========
delete
========

Deletes a connector from the application.

See: `Connector Overview <https://help.tago.io/portal/en/kb/articles/466-connector-overview>`_

    **Parameters:**

        | **connectorID**: str
        | Connector ID

    **Returns:**

        | str

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.integration.connectors.delete("connector-id-123")
        print(result)  # Connector Successfully Deleted

.. toctree::


.. toctree::

    IntegrationConnector_Type
