**Devices**
============

Manage devices in account.

=======
create
=======

Generates and retrieves a new action from the Device

    **Parameters:**

        | **deviceObj**: :ref:`DeviceCreateInfo`
        | Object data to create new device

======
delete
======

Deletes an device from the account

    **Parameters:**

        | **deviceID**: GenericID: str
        | Device ID


======
edit
======

Modify any property of the device

    **Parameters:**

        | **deviceID**: GenericID: str
        | Device ID

        | **deviceObj**: :ref:`DeviceEditInfo`
        | Device object with fields to replace


================
emptyDeviceData
================

Empty all data in a device.

    **Parameters:**

        | **deviceID**: GenericID: str
        | Device ID


================
getDeviceData
================

Get data from all variables in the device.

    **Parameters:**

        | **deviceID**: GenericID: str
        | Device ID

        | *Optional* **queryParams**: :ref:`DataQuery`
        | Query parameters to filter the results.

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Resources

        resources = Resources()
        resources.devices.getDeviceData("myDeviceId");

=====
info
=====

Get Info of the Device

    **Parameters:**

        | **deviceID**: GenericID: str
        | Device ID


==========
listDevice
==========

Retrieves a list with all devices from the account

    **Parameters:**

        | *Optional* **queryObj**: :ref:`DeviceQuery`
        | Search query params

.. code-block::
    :caption: **Default queryObj:**

        queryObj: {
            "page": 1,
            "fields": ["id", "name"],
            "filter": {},
            "amount": 20,
            "orderBy": ["name", "asc"],
            "resolveBucketName": False
        }

=========
paramSet
=========

Create or edit param for the Device

    **Parameters:**

        | **deviceID**: GenericID: str
        | Device ID

        | **configObj**: :ref:`ConfigurationParams` or list[:ref:`ConfigurationParams`]
        | Configuration Data

        | **paramID**: Optional[GenericID: str]
        | Parameter ID


==========
paramList
==========

List Params for the Device

    **Parameters:**

        | **deviceID**: GenericID: str
        | Device ID

        | *Optional* **sentStatus**: bool
        | True return only sent=true, False return only sent=false

============
paramRemove
============

Remove param for the Device

    **Parameters:**

        | **deviceID**: GenericID: str
        | Device ID

        | **paramID**: GenericID: str
        | Parameter ID


============
tokenCreate
============

Generates and retrieves a new token

    **Parameters:**

        | **deviceID**: GenericID: str
        | Device ID

        | **tokenParams**: :ref:`DevicesTokenData`
        | Params for new token

============
tokenDelete
============

Delete a token

    **Parameters:**

        | **token**: GenericToken: str
        | Device ID

==========
tokenList
==========

Retrieves a list of all tokens

    **Parameters:**

        | **token**: GenericToken: str
        | Device ID

        | *Optional* **queryObj**: :ref:`ListDeviceTokenQuery`
        | Search query params

.. code-block::
    :caption: **Default queryObj:**

        queryObj: {
            "page": 1,
            "fields": ["name", "token", "permission"],
            "filter": {},
            "amount": 20,
            "orderBy": ["created_at", "desc"],
        }

==============
sendDeviceData
==============

Send data to a device.

    **Parameters:**

        | **deviceID**: GenericID: str
        | Device ID

        | **data**: Union[:ref:`CommonData`, list[:ref:`CommonData`]]
        | An array or one object with data to be send to TagoIO.

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Resources

        resources = Resources()
        resource.devices.sendDeviceData("myDeviceID", {
            "variable": "temperature",
            "unit": "F",
            "value": 55,
            "time": "2015-11-03 13:44:33",
            "location": { "lat": 42.2974279, "lng": -85.628292 },
        })

==============
editDeviceData
==============

Edit data in a device.

    **Parameters:**

        | **deviceID**: GenericID: str
        | Device ID

        | **updatedData**: Union[:ref:`CommonData`, list[:ref:`CommonData`]]
        | An array or one object with data to be send to TagoIO.

.. code-block::
    :caption: **Example:**

    resources = Resource()
    resource.devices.editDeviceData("myDeviceID", {
        "id": "idOfTheRecord",
        "value": "new value",
        "unit": "new unit"
    })

================
deleteDeviceData
================

Delete data from a device.

    **Parameters:**

        | **deviceID**: GenericID: str
        | Device ID

        | *Optional* **queryParams**: :ref:`DataQuery`
        | Query parameters to filter the results.

.. code-block::
    :caption: **Example:**

    resources = Resource()
    resource.devices.deleteDeviceData("myDeviceID", {
        "ids": ["recordIdToDelete", "anotherRecordIdToDelete" ]
    })

.. toctree::

    Devices_Type
