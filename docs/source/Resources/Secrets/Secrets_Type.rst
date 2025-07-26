**Secrets Type**
================


.. _SecretsInfo:

SecretsInfo
-----------

    **Attributes:**

        | id: :ref:`GenericID`
        | Unique identifier for the secret.

        | key: str
        | Key name of the secret.

        | tags: Optional[List[:ref:`TagsObj`]]
        | List of tags associated with the secret.

        | value_length: int
        | Length of the secret value.

        | created_at: datetime
        | Date and time when the secret was created.

        | updated_at: datetime
        | Date and time when the secret was last updated.


.. _SecretsCreate:

SecretsCreate
-------------

    **Attributes:**

        | key: str
        | Key name for the new secret.

        | value: str
        | Value of the secret.

        | tags: Optional[List[:ref:`TagsObj`]]
        | List of tags to associate with the secret.


.. _SecretsEdit:

SecretsEdit
-----------

    **Attributes:**

        | value: Optional[str]
        | New value for the secret.

        | tags: Optional[List[:ref:`TagsObj`]]
        | Updated list of tags for the secret.


.. _SecretsFilter:

SecretsFilter
-------------

    **Attributes:**

        | key: str
        | Key name to filter secrets by.

        | tags: Optional[List[:ref:`TagsObj`]]
        | Tags to filter secrets by.


.. _SecretsQuery:

SecretsQuery(:ref:`Query`)
--------------------------

    **Attributes:**

        | fields: Optional[List[Literal["id", "key", "tags", "created_at", "updated_at"]]]
        | List of fields to include in the query results.

        | filter: Optional[:ref:`SecretsFilter`]
        | Filter criteria for the query.
