**Secrets**
===========

Manage secrets in your application.

=======
list
=======

Retrieves a paginated list of all secrets stored in the profile with filtering and sorting options.

See: `Secrets <https://help.tago.io/portal/en/kb/articles/secrets>`_

    **Parameters:**

        | *Optional* **queryObj**: :ref:`SecretsQuery`
        | Query parameters to filter the results.

        .. code-block::
            :caption: **Default queryObj:**

            queryObj = {
                "page": 1,
                "fields": ["id", "key"],
                "filter": {},
                "amount": 20,
                "orderBy": ["key", "asc"]
            }

    **Returns:**

        | list[:ref:`SecretsInfo`]

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Secrets" / "Access" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.secrets.list({
            "page": 1,
            "fields": ["id", "key"],
            "amount": 20
        })
        print(result)  # [ { 'id': 'secret-id-123', 'key': 'API_KEY' } ]


=======
info
=======

Retrieves detailed information about a specific secret using its ID.

See: `Secrets <https://help.tago.io/portal/en/kb/articles/secrets>`_

    **Parameters:**

        | **secretID**: str
        | Secret ID

    **Returns:**

        | :ref:`SecretsInfo`

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Secrets" / "Access" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        secret_info = resources.secrets.info("secret-id-123")
        print(secret_info)  # { 'id': 'secret-id-123', 'key': 'API_KEY' }


=======
create
=======

Creates a new secret in the profile with the specified key and value.

See: `Creating a Secret <https://help.tago.io/portal/en/kb/articles/secrets#Creating_a_Secret>`_

    **Parameters:**

        | **secretObj**: :ref:`SecretsCreate`
        | Secret information

    **Returns:**

        | dict[str, :ref:`GenericID`]

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Secrets" / "Create" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.secrets.create({
            "key": "API_KEY",
            "value": "my-secret-value"
        })
        print(result)  # { 'id': 'secret-id-132' }


=======
edit
=======

Modifies the properties of an existing secret.

See: `Secrets <https://help.tago.io/portal/en/kb/articles/secrets>`_

    **Parameters:**

        | **secretID**: str
        | Secret ID

        | **secretObj**: :ref:`SecretsEdit`
        | Secret information to update

    **Returns:**

        | string

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Secrets" / "Edit" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.secrets.edit("secret-id-123", {
            "value": "new-secret-value",
            "tags": [{"key": "type", "value": "user"}]
        })
        print(result)  # Successfully Updated


=======
delete
=======

Permanently removes a secret from the profile.

See: `Secrets <https://help.tago.io/portal/en/kb/articles/secrets>`_

    **Parameters:**

        | **secretID**: str
        | Secret ID

    **Returns:**

        | string

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Secrets" / "delete" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.secrets.delete("secret-id-123")
        print(result)  # Successfully Removed

.. toctree::


.. toctree::

    Secrets_Type
