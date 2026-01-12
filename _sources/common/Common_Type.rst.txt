
.. _GenericID:

GenericID
---------

    | **GenericID**: str
    | ID used on TagoIO, string with 24 character

.. _Base64:

Base64
------

    | **Base64**: str

.. _GenericToken:

GenericToken
------------

    | **GenericToken**: str
    | Token used on TagoIO, string with 36 characters

.. _ExpireTimeOption:

ExpireTimeOption
----------------

    | **ExpireTimeOption**: "never" or datetime

.. _PermissionOption:

PermissionOption
----------------

    | **PermissionOption**: Literal["write", "read", "full", "deny"]

.. _Conditionals:

Conditionals
------------

    | **Conditionals**: Literal["<", ">", "=", "!", "><", "*"]

.. _TokenCreateResponse:

TokenCreateResponse
-------------------

    **Attributes:**

        | **token**: GenericToken
        | **expire_date**: :ref:`ExpireTimeOption`
        | **permission**: :ref:`PermissionOption`

.. _TagsObj:

TagsObj
-------

    **Attributes:**

        | **key**: str
        | **value**: str

.. _File:

File
----

    **Attributes:**

        | **url**: str
        | **md5**: str
        | **path**: str

.. _FixedPositionValue:

FixedPositionValue
------------------

    **Attributes:**

        | **color**: str
        | **icon**: str
        | **value**: str
        | **x**: str
        | **y**: str

.. _SentValue:

SentValue
---------

    **Attributes:**

        | **label**: str
        | **value**: Union[str, int, float, bool]

.. _Metadata:

Metadata
--------

    **Attributes:**

        | **color**: Optional[str]
        | **x**: Optional[Union[str, int, float]]
        | **y**: Optional[Union[str, int, float]]
        | **label**: Optional[str]
        | **file**: Optional[:ref:`File`]
        | **icon**: Optional[str]
        | **fixed_position**: Optional[dict[str, :ref:`FixedPositionValue`]]
        | **sentValues**: Optional[list[:ref:`SentValue`]]
        | **old_value**: Optional[Union[str, int, float, bool]]

.. _CommonLocationGeoJSON:

LocationGeoJSON
---------------

    **Attributes:**

        | **type**: Literal["Point"]
        | **coordinates**: list[Union[Longitude, Latitude]]

.. _LocationLatLng:

LocationLatLng
--------------

    **Attributes:**

        | **lat**: float
        | **lng**: float

.. _CommonData:

Data
----

    **Attributes:**

        | **id**: str
        | **device**: str
        | **variable**: str
        | **value**: Union[str, float, int, bool]
        | **group**: str
        | **unit**: str
        | **time**: Optional[Union[str, datetime]]
        | **location**: Optional[Union[:ref:`CommonLocationGeoJSON`, :ref:`LocationLatLng`, None]]

.. _TokenDataList:

TokenDataList
-------------

    **Attributes:**

        | **token**: GenericToken
        | **name**: str
        | **type**: str
        | **permission**: PermissionOption
        | **serie_number**: Optional[str]
        | **last_authorization**: Optional[datetime]
        | **verification_code**: Optional[str]
        | **expire_time**: ExpireTimeOption
        | **ref_id**: str
        | **created_at**: datetime
        | **created_by**: Optional[str]

.. _CommonTokenData:

TokenData
---------

    **Attributes:**

        | **name**: str
        | **expire_time**: Optional[:ref:`ExpireTimeOption`]
        | **permission**: :ref:`PermissionOption`
        | **serie_number**: Optional[str]
        | **verification_code**: Optional[str]
        | **middleware**: Optional[str]

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
                "orderBy": ["name", "asc"]
            }
