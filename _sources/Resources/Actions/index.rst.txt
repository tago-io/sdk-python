**Actions**
===========

Manage actions in your application.

=======
list
=======

Lists all actions from the application with pagination support.
Use this to retrieve and manage actions in your application.

See: `Actions <https://help.tago.io/portal/en/kb/tagoio/actions>`_

    **Parameters:**

        | *Optional* **queryObj**: :ref:`ActionQuery`
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

        | list[:ref:`ActionInfo`]

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Action" / "Access" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        list_result = resources.actions.list({
            "page": 1,
            "fields": ["id", "name"],
            "amount": 10,
            "orderBy": ["name", "asc"]
        })
        print(list_result)  # [{'id': '66ab7c62e5f0db000998ce42', 'name': 'Action Test', ...}]


=======
create
=======

Creates a new action in your application.

See: `Actions <https://help.tago.io/portal/en/kb/tagoio/actions>`_

    **Parameters:**

        | **actionObj**: :ref:`ActionCreateInfo`
        | Action information

    **Returns:**

        | dict

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Action" / "Create" in Access Management.
        from tagoio_sdk import Resources

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


=======
edit
=======

Modifies an existing action.

See: `Actions <https://help.tago.io/portal/en/kb/tagoio/actions>`_

    **Parameters:**

        | **actionID**: str
        | Action ID

        | **actionObj**: dict
        | Action information to update

    **Returns:**

        | string

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Action" / "Edit" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.actions.edit("action-id-123", {
            "name": "Updated Action",
            "active": False
        })
        print(result)  # Successfully Updated


=======
delete
=======

Deletes an action from your application.

See: `Actions <https://help.tago.io/portal/en/kb/tagoio/actions>`_

    **Parameters:**

        | **actionID**: str
        | Action ID

    **Returns:**

        | string

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Action" / "Delete" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.actions.delete("action-id-123")
        print(result)  # Successfully Removed


=======
info
=======

Retrieves detailed information about a specific action.

See: `Actions <https://help.tago.io/portal/en/kb/tagoio/actions>`_

    **Parameters:**

        | **actionID**: str
        | Action ID

    **Returns:**

        | :ref:`ActionInfo`

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Action" / "Access" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        action_info = resources.actions.info("action-id-123")
        print(action_info)  # {'id': 'action-id-123', 'name': 'My Action', ...}

.. toctree::

    Actions_Type
