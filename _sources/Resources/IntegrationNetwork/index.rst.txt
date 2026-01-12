**Integration Network**
=======================

Manage integration networks in the account.

============
listNetwork
============

Retrieves a list of all networks from the account with pagination support.
Use this to retrieve and manage networks in your application.

See: `Network Integration <https://docs.tago.io/docs/tagoio/integrations/general/creating-a-network-integration>`_

    **Parameters:**

        | *Optional* **queryObj**: :ref:`NetworkQuery`
        | Query parameters to filter the results.

        .. code-block::
            :caption: **Default queryObj:**

            queryObj = {
                "page": 1,
                "fields": ["id", "name"],
                "filter": {},
                "amount": 20,
                "orderBy": ["name", "asc"]
            }

    **Returns:**

        | List[:ref:`NetworkInfo`]

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Integration Network" / "Access" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        networks = resources.integration.networks.listNetwork({
            "page": 1,
            "fields": ["id", "name"],
            "amount": 20,
            "orderBy": ["name", "asc"]
        })
        print(networks)  # [{'id': 'network-id-123', 'name': 'My Network', ...}]


======
info
======

Retrieves detailed information about a specific network.

See: `Network Integration <https://docs.tago.io/docs/tagoio/integrations/general/creating-a-network-integration>`_

    **Parameters:**

        | **networkID**: :ref:`GenericID`
        | Network ID

        | *Optional* **fields**: List[str]
        | Fields to retrieve (default: ["id", "name"])

    **Returns:**

        | :ref:`NetworkInfo`

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Integration Network" / "Access" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        network_info = resources.integration.networks.info("network-id-123")
        print(network_info)  # {'id': '...', 'name': 'My Network', ...}


======
create
======

Creates a new integration network in the account.

See: `Creating a Network Integration <https://docs.tago.io/docs/tagoio/integrations/general/creating-a-network-integration#create-a-new-integration>`_

    **Parameters:**

        | **networkObj**: :ref:`NetworkCreateInfo`
        | Network information

    **Returns:**

        | Dict[str, str]

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Integration Network" / "Create" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        new_network = resources.integration.networks.create({
            "name": "My Custom Network",
            "description": "Custom integration network",
            "middleware_endpoint": "https://my-middleware.com/endpoint",
            "public": False
        })
        print(new_network)  # {'network': 'network-id-123'}


======
edit
======

Modifies any property of an existing network.

    **Parameters:**

        | **networkID**: :ref:`GenericID`
        | Network ID

        | **networkObj**: :ref:`NetworkCreateInfo`
        | Network information to update

    **Returns:**

        | str

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Integration Network" / "Edit" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.integration.networks.edit("network-id-123", {
            "name": "Updated Network Name",
            "description": "Updated description",
            "public": True
        })
        print(result)  # Successfully Updated


======
delete
======

Permanently deletes a network from the account.

    **Parameters:**

        | **networkID**: :ref:`GenericID`
        | Network ID

    **Returns:**

        | str

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Integration Network" / "Delete" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.integration.networks.delete("network-id-123")
        print(result)  # Successfully Removed


==========
tokenList
==========

Retrieves a list of all authentication tokens for a network with optional filtering.

See: `Tokens and Getting Devices <https://docs.tago.io/docs/tagoio/integrations/general/creating-a-network-integration#tokens-and-getting-devices>`_

    **Parameters:**

        | **networkID**: :ref:`GenericID`
        | Network ID

        | *Optional* **queryObj**: :ref:`ListTokenQuery`
        | Query parameters to filter the results.

        .. code-block::
            :caption: **Default queryObj:**

            queryObj = {
                "page": 1,
                "fields": ["name", "token", "permission"],
                "filter": {},
                "amount": 20,
                "orderBy": ["created_at", "desc"]
            }

    **Returns:**

        | List[:ref:`NetworkTokenInfo`]

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Integration Network" / "Access" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        tokens = resources.integration.networks.tokenList("network-id-123", {
            "page": 1,
            "amount": 20,
            "fields": ["name", "token", "permission"],
            "orderBy": ["created_at", "desc"]
        })
        print(tokens)  # [{'name': 'Default Token', 'token': '...', 'permission': 'full', ...}]


===========
tokenCreate
===========

Generates and retrieves a new authentication token for a network.

See: `Tokens and Getting Devices <https://docs.tago.io/docs/tagoio/integrations/general/creating-a-network-integration#tokens-and-getting-devices>`_

    **Parameters:**

        | **networkID**: :ref:`GenericID`
        | Network ID

        | **tokenParams**: :ref:`IntegrationTokenData`
        | Parameters for the new token

    **Returns:**

        | :ref:`TokenCreateResponse`

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Integration Network" / "Create Token" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.integration.networks.tokenCreate("network-id-123", {
            "name": "Production Token",
            "permission": "write",
            "expire_time": "never"
        })
        print(result)  # {'token': 'new-token-value', 'expire_date': None}


===========
tokenDelete
===========

Permanently deletes an authentication token.

See: `Tokens and Getting Devices <https://docs.tago.io/docs/tagoio/integrations/general/creating-a-network-integration#tokens-and-getting-devices>`_

    **Parameters:**

        | **token**: :ref:`GenericToken`
        | Token to delete

    **Returns:**

        | str

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Integration Network" / "Delete Token" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.integration.networks.tokenDelete("token-to-delete")
        print(result)  # Successfully Removed


.. toctree::

    IntegrationNetwork_Type
