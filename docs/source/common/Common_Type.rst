
.. _ExpireTimeOption:

ExpireTimeOption
------

    | **ExpireTimeOption**: "never" or datetime


.. _PermissionOption:

PermissionOption
------

    | **PermissionOption**: Literal["write", "read", "full", "deny"]


.. _TokenDataList:

TokenDataList
----------

    **Attributes:**

        | **token**: GenericToken
        | **name**: str
        | **type**: str
        | **permission**: :ref:`PermissionOption`
        | **serie_number**: Optional[str]
        | **last_authorization**: Optional[datetime]
        | **verification_code**: Optional[str]
        | **expire_time**: :ref:`ExpireTimeOption`
        | **ref_id**: str
        | **created_at**: datetime
        | **created_by**: Optional[str]


.. _Query:

Query
-----------------
    **Attributes:**

        | **page**: Optional[int]
        | **amount**: Optional[int]
        | **fields**: Optional[list[str]]
        | **filter**: Optional[any]
        | **orderBy**: Optional[list["asc" or "desc"]]

    .. code-block::
        :caption: **Example:**

            orderBy = {
                "page": 1,
                "fields": ["id", "name"],
                "filter": {"name": "test"},
                "amount": 20,
                "orderBy": ["name": "asc"]
            }
