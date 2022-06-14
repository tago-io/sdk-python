**Devices**
============

Manage devices in account Be sure to use an account token with “write” permissions when using functions like create, edit and delete.

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

        from tagoio_sdk import Account

        myDevice = Account({ "token": "my_account_token" }).devices
        myDevice.getVariablesData("myDeviceId");

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

        | **queryObj**: :ref:`DeviceQuery`
        | Search query params

.. code-block::
    :caption: **Default queryObj:**

        queryObj: {
            "page": 1,
            "fields": ["id", "name"],
            "filter": {},
            "amount": 20,
            "orderBy": "name,asc",
            "resolveBucketName": false
        }


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

        | **tokenParams**: :ref:`TokenData`
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
            "orderBy": "created_at,desc",
        }
