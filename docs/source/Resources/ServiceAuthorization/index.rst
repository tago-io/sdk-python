**Service Authorization**
=========================

Manage service authorization tokens.

===========
tokenList
===========

Retrieves a paginated list of all service authorization tokens with filtering and sorting options.

See: `Authorization <https://help.tago.io/portal/en/kb/articles/218-authorization>`_

    **Parameters:**

        | *Optional* **query**: :ref:`ServiceAuthorizationQuery`
        | Query parameters to filter the results.

        .. code-block::
            :caption: **Default query:**

            query = {
                "page": 1,
                "fields": ["name", "token"],
                "filter": {},
                "amount": 20,
                "orderBy": ["created_at", "desc"]
            }

    **Returns:**

        | list[:ref:`TokenDataList`]

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Service Authorization" / "Access" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.serviceAuthorization.tokenList({
            "page": 1,
            "fields": ["name", "token", "verification_code"],
            "amount": 20
        })
        print(result)  # [ { 'name': 'API Service Token', 'token': 'token-xyz-123' } ]


============
tokenCreate
============

Generates and retrieves a new service authorization token with specified permissions.

See: `Authorization <https://help.tago.io/portal/en/kb/articles/218-authorization>`_

    **Parameters:**

        | **tokenParams**: :ref:`TokenCreateResponseAuthorization`
        | Parameters for the new token

    **Returns:**

        | :ref:`TokenCreateResponseAuthorization`

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Service Authorization" / "Create" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.serviceAuthorization.tokenCreate({
            "name": "Service Token",
            "verification_code": "additional parameter"
        })
        print(result)  # { 'token': 'token-xyz-123', 'name': 'Service Token', ... }


============
tokenDelete
============

Permanently removes a service authorization token.

See: `Authorization <https://help.tago.io/portal/en/kb/articles/218-authorization>`_

    **Parameters:**

        | **token**: :ref:`GenericTokenAuthorization`
        | Token to be deleted

    **Returns:**

        | str

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Service Authorization" / "Delete" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.serviceAuthorization.tokenDelete("token-xyz-123")
        print(result)  # Token Successfully Removed


===========
tokenEdit
===========

Updates a service authorization token with an optional verification code.

See: `Authorization <https://help.tago.io/portal/en/kb/articles/218-authorization>`_

    **Parameters:**

        | **token**: :ref:`GenericTokenAuthorization`
        | Token to be updated

        | *Optional* **verificationCode**: str
        | New verification code for the token

    **Returns:**

        | str

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Service Authorization" / "Edit" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.serviceAuthorization.tokenEdit("token-xyz-123", "verification-code")
        print(result)  # Authorization Code Successfully Updated

.. toctree::


.. toctree::

    Service_Authorization_Types
