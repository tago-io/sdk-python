**Devices Type**
=================


.. _bucket:

bucket
------

    **Attributes:**

        **id**:  :ref:`GenericID`

        **name**: str


.. _DeviceInfo:

DeviceInfo
-----------

    **Attributes:**

        | **id**:  :ref:`GenericID`
        | Device ID.

        | **type**: DataStorageType
        | Device's data storage (bucket) type.

        | **profile**:  :ref:`GenericID`
        | ID of the profile that owns the device.

        | **bucket**: bucket
        | Bucket storing the device's data.

        | **last_output**: datetime or None
        | Date for the device's last output.

        | **last_input**: datetime or None
        | Date for the device's last input.

        | **updated_at**: datetime
        | Date for the device's last update.

        | **created_at**: datetime
        | Date for the device's creation.

        | **inspected_at**: datetime or None
        | Date for the device's last inspection.

        | **last_retention**: datetime or None
        | Date for the device's last data retention.



.. _DeviceInfoList:

DeviceInfoList
---------------

    **Attributes:**

        | **id**:  :ref:`GenericID`
        | Device ID.

        | **type**: DataStorageType
        | Device's data storage (bucket) type.

        | **profile**:  :ref:`GenericID`
        | ID of the profile that owns the device.

        | **last_output**: datetime or None
        | Date for the device's last output.

        | **last_input**: datetime or None
        | Date for the device's last input.

        | **updated_at**: datetime
        | Date for the device's last update.

        | **created_at**: datetime
        | Date for the device's creation.

        | **inspected_at**: datetime or None
        | Date for the device's last inspection.

        | **last_retention**: datetime or None
        | Date for the device's last data retention.

        | **bucket**:  :ref:`GenericID`


.. _DeviceQuery:

DeviceQuery
------------

    **Attributes:**

        | **page**: int or float
        | Page of list starting from 1

        | **amount**: int or float
        | Amount of items will return.

        | **fields**: list[
                "id" or
                "type" or
                "profile" or
                "last_output" or
                "last_input" or
                "updated_at" or
                "created_at" or
                "inspected_at" or
                "last_retention"
            ]
        | Array of field names.

        | **filter**: DeviceInfo
        | Filter object.

        | orderBy: list[
                "name" or
                "visible" or
                "active" or
                "last_input" or
                "last_output" or
                "created_at" or
                "updated_at" or
                "asc" or
                "desc"
            ]
        | Tuple with a field and an order

        | **resolveBucketName**: Optional[bool]


.. _DeviceListItem:

DeviceListItem
---------------

    **DeviceListItem** = DeviceInfoList


.. _ConfigurationParams:

ConfigurationParams
-------------------

    **Attributes:**

        **sent**: bool

        **key**: str

        **value**: str

        **id**: Optional[str]


.. _DeviceCreateResponse:

DeviceCreateResponse
----------------------

    **Attributes:**

        **device_id**: :ref:`GenericID`

        **bucket_id**:  :ref:`GenericID`

        **token**:  :ref:`GenericToken`


.. _DeviceCreateInfoBasic:

DeviceCreateInfoBasic
----------------------

    **Attributes:**

        | **name**: str
        | Device name.

        | **connector**:  :ref:`GenericID`
        | Connector ID.

        | **network**:  :ref:`GenericID`
        | Network ID.

        | **type**: Optional[str]
        | [Optional] Device's data storage (bucket) type.
        | :default: "legacy"

        | **description**: Optional[str or None]
        | [Optional] Description of the device.

        | **active**: Optional[bool]
        | [Optional] Set if the device will be active.

        | **visible**: Optional[bool]
        | [Optional] Set if the device will be visible.

        | **configuration_params**: Optional[list[ConfigurationParams]]
        | [Optional] An array of configuration params

        | **tags**: Optional[list[:ref:`TagsObj`]]
        | [Optional] An array of tags

        | **serie_number**: Optional[str]
        | [Optional] Device serial number.

        | **connector_parse**: Optional[bool]
        | [Optional] If device will use connector parser

        | **parse_function**: Optional[str]
        | [Optional] Javascript code for use as payload parser



.. _DeviceCreateInfoBasicMutable:

DeviceCreateInfoBasicMutable
-----------------------------

    **Attributes:**

        | **name**: str
        | Device name.

        | **connector**:  :ref:`GenericID`
        | Connector ID.

        | **network**:  :ref:`GenericID`
        | Network ID.

        | **type**: "mutable"
        | Device's data storage (bucket) type.
        | :default: "legacy"

        | **description**: str or None
        | Description of the device.

        | **active**: bool
        | Set if the device will be active.

        | **visible**: bool
        | Set if the device will be visible.

        | **configuration_params**: list[:ref:`ConfigurationParams`]
        | An array of configuration params

        | **tags**: list[:ref:`TagsObj`]
        | An array of tags

        | **serie_number**: str
        | Device serial number.

        | **connector_parse**: bool
        | If device will use connector parser

        | **parse_function**: str
        | Javascript code for use as payload parser



.. _DeviceCreateInfoBasicImutable:

DeviceCreateInfoBasicImutable
--------------------------------

    **Attributes:**

        | **name**: str
        | Device name.

        | **connector**:  :ref:`GenericID`
        | Connector ID.

        | **network**:  :ref:`GenericID`
        | Network ID.

        | **type**: "imutable"
        | Device's data storage (bucket) type.
        | :default: "legacy"

        | **description**: str or None
        | Description of the device.

        | **active**: bool
        | Set if the device will be active.

        | **visible**: bool
        | Set if the device will be visible.

        | **configuration_params**: list[:ref:`ConfigurationParams`]
        | An array of configuration params

        | **tags**: list[:ref:`TagsObj`]
        | An array of tags

        | **serie_number**: str
        | Device serial number.

        | **connector_parse**: bool
        | If device will use connector parser

        | **parse_function**: str
        | Javascript code for use as payload parser

        | **chunk_period**: "day" or "week" or "month" or "quarter"
        | Chunk division to retain data in the device.
        | Required for Immutable devices.

        | **chunk_retention**: int or float
        | Amount of chunks to retain data according to the `chunk_period`.
        | Integer between in the range of 0 to 36 (inclusive).
        | Required for Immutable devices.


.. _DeviceCreateInfoMutable:

DeviceCreateInfoMutable
------------------------

    **DeviceCreateInfoMutable** = DeviceCreateInfoBasicMutable


.. _DeviceCreateInfoImmutable:

DeviceCreateInfoImmutable
--------------------------

    **DeviceCreateInfoImmutable** = DeviceCreateInfoBasicImutable


.. _DeviceCreateInfo:

DeviceCreateInfo
-----------------

    **DeviceCreateInfo** = DeviceCreateInfoMutable or DeviceCreateInfoImmutable


.. _DeviceEditInfo:

DeviceEditInfo
---------------

    **Attributes:**

        | **name**: str
        | Device name.

        | **connector**:  :ref:`GenericID`
        | Connector ID.

        | **network**:  :ref:`GenericID`
        | Network ID.

        | **description**: str or None
        | Description of the device.

        | **active**: bool
        | Set if the device will be active.

        | **visible**: bool
        | Set if the device will be visible.

        | **configuration_params**: list[:ref:`ConfigurationParams`]
        | An array of configuration params

        | **tags**: list[:ref:`TagsObj`]
        | An array of tags

        | **serie_number**: str
        | Device serial number.

        | **connector_parse**: bool
        | If device will use connector parser

        | **parse_function**: str
        | Javascript code for use as payload parser

        | **chunk_retention**: int or float
        | Amount of chunks to retain data according to the `chunk_period`.
        | Integer between in the range of 0 to 36 (inclusive).
        | Required for Immutable devices.



.. _DevicesTokenData:

TokenData
----------

    **Attributes:**

        | **name**: str
        | A name for the token.

        | **expire_time**: :ref:`ExpireTimeOption`
        | The time for when the token should expire.
        | It will be randomly generated if not included.
        | Accepts “never” as value.

        | **permission**: :ref:`PermissionOption`
        | Token permission should be 'write', 'read' or 'full'.

        | **serie_number**: Optional[str]
        | [optional] The serial number of the device.

        | **verification_code**: Optional[str]
        | [optional] Verification code to validate middleware requests.

        | **middleware**: Optional[str]
        | [optional] Middleware or type of the device that will be added.



.. _DeviceTokenDataList:

DeviceTokenDataList
--------------------

    **Attributes:**

        **token**:  :ref:`GenericToken`

        **device_id**:  :ref:`GenericID`

        **network_id**:  :ref:`GenericID`

        **name**: str

        **permission**: :ref:`PermissionOption`

        **serie_number**: str or None

        **last_authorization**: str or None

        **expire_time**: :ref:`ExpireTimeOption`

        **created_at**: str


.. _ListDeviceTokenQuery:

ListDeviceTokenQuery
----------------------

    **Attributes:**

        | **page**: int or float
        | Page of list starting from 1

        | **amount**: int or float
        | Amount of items will return.

        | **fields**: list[
                "token" or
                "device_id" or
                "network_id" or
                "name" or
                "permission" or
                "serie_number" or
                "last_authorization" or
                "expire_time"
            ]
        | Array of field names.

        | **filter**: :ref:`DeviceTokenDataList`
        | Filter object.

        | **orderBy**: Optional[
            list[
                "name" or
                "permission" or
                "serie_number" or
                "last_authorization" or
                "created_at" or
                "asc" or
                "desc"
            ]]
        | [Optional] Tuple with a field and an order

