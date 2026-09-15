**Access Type**
===============

.. _Permissions:

Permissions
-----------

    **Attributes:**

        | effect: "allow" or "deny"
        | Indicates whether the permission allows or denies the specified actions.

        | action: List[str]
        | List of actions that are allowed or denied.

        | resource: List[str]
        | List of resources to which the actions apply.


.. _AccessCreateInfo:

AccessCreateInfo
----------------

    **Attributes:**

        | name: str
        | Name of the access policy.

        | permissions: List[:ref:`Permissions`]
        | List of permissions assigned to this access policy.

        | targets: List[Any]
        | List of targets (users, devices, etc.) that this access policy applies to.

        | profile: Optional[:ref:`GenericID`]
        | Profile ID associated with this access policy.

        | tags: Optional[List[:ref:`TagsObj`]]
        | List of tags for categorization or filtering.

        | active: Optional[bool]
        | Indicates if the access policy is active.


.. _AccessInfo:

AccessInfo(:ref:`AccessCreateInfo`)
-----------------------------------

    **Attributes:**

        | id: :ref:`GenericID`
        | Unique identifier for the access policy.

        | created_at: datetime
        | Date and time when the access policy was created.

        | updated_at: datetime
        | Date and time when the access policy was last updated.


.. _AccessQuery:

AccessQuery(:ref:`Query`)
-------------------------

    **Attributes:**

        | fields: Optional[List["name" or "active" or "created_at" or "updated_at"]]
        | List of fields to include in the query results.
