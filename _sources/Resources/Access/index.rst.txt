**Access**
==========

Manage access policies in your application.

=======
list
=======

Lists all access rules from the application with pagination support.
Use this to retrieve and manage access policies for your application.

See: `Access Management <https://help.tago.io/portal/en/kb/articles/183-access-management>`_

    **Parameters:**

        | *Optional* **queryObj**: :ref:`AccessQuery`
        | Query parameters to filter the results.

        .. code-block::
            :caption: **Default queryObj:**

            queryObj = {
                "page": 1,
                "fields": ["id", "name", "tags"],
                "filter": {},
                "amount": 20,
                "orderBy": ["name", "asc"]
            }

    **Returns:**

        | list[:ref:`AccessInfo`]

    .. code-block:: python

        # If you receive an error "Authorization Denied", check policy "Access Management" / "Access" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.access.list({
            "page": 1,
            "fields": ["id", "name"],
            "amount": 10,
            "orderBy": ["name", "asc"]
        })
        print(result)  # [{'id': 'access-id-123', 'name': '[Analysis] - Test'}, ...]


=======
create
=======

Creates a new access policy in your application.

See: `Access Management <https://help.tago.io/portal/en/kb/articles/183-access-management>`_

    **Parameters:**

        | **accessObj**: :ref:`AccessCreateInfo`
        | Access policy information

    **Returns:**

        | dict

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Access Management" / "Create" in Access Management.
        from tagoio_sdk import Resources

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


=======
edit
=======

Modifies an existing access policy.

See: `Access Management <https://help.tago.io/portal/en/kb/articles/183-access-management>`_

    **Parameters:**

        | **accessID**: str
        | Access policy ID

        | **accessObj**: dict
        | Access policy information to update

    **Returns:**

        | string

    .. code-block:: python

        # If you receive an error "Authorization Denied", check policy "Access Management" / "Edit" in Access Management.
        from tagoio_sdk import Resources

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


=======
delete
=======

Removes an access policy from your application.

See: `Access Management <https://help.tago.io/portal/en/kb/articles/183-access-management>`_

    **Parameters:**

        | **accessID**: str
        | Access policy ID

    **Returns:**

        | string

    .. code-block:: python

        # If you receive an error "Authorization Denied", check policy "Access Management" / "Delete" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.access.delete("access-id-123")
        print(result)  # Successfully Removed


=======
info
=======

Retrieves detailed information about a specific access policy.

See: `Access Management <https://help.tago.io/portal/en/kb/articles/183-access-management>`_

    **Parameters:**

        | **accessID**: str
        | Access policy ID

    **Returns:**

        | :ref:`AccessInfo`

    .. code-block:: python

        # If you receive an error "Authorization Denied", check policy "Access Management" / "Access" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        access_info = resources.access.info("access-id-123")
        print(access_info)  # {'id': 'access-id-123', 'name': '[Analysis] - Test', ...}

.. toctree::

    Access_Type
