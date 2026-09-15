**Devices**
============

Manage devices in account.

======
amount
======

Gets the amount of data stored in a device.

    **See:**

        https://help.tago.io/portal/en/kb/articles/device-data Device Data Management

    **Parameters:**

        | **deviceID**: :ref:`GenericID`
        | Device ID

    **Returns:**

        Union[int, float]

.. code-block::
    :caption: **Example:**

        resources = Resources()
        amount = resources.devices.amount("device-id-123")
        print(amount)  # 15234


======
create
======

Creates a new device in the account with specified configuration and returns device credentials.

    **See:**

        https://help.tago.io/portal/en/kb/articles/478-devices Devices Overview
        https://help.tago.io/portal/en/kb/articles/481-device-types Device Types

    **Parameters:**

        | **deviceObj**: :ref:`DeviceCreateInfo`
        | Object data to create new device

    **Returns:**

        :ref:`DeviceCreateResponse`

.. code-block::
    :caption: **Example:**

        resources = Resources()
        result = resources.devices.create({
            "name": "Temperature Sensor",
            "network": "network-id-123",
            "connector": "connector-id-456",
            "type": "immutable",
            "chunk_period": "month",
            "chunk_retention": 6,
            "active": True
        })
        print(result)  # {'device_id': '...', 'bucket_id': '...', 'token': '...'}


==========
dataBackup
==========

Schedule to export the device's data to TagoIO Files.
For mutable devices, exports all data. For immutable devices with chunkID, exports specific chunk.

    **See:**

        https://help.tago.io/portal/en/kb/articles/55-data-export Data Export
        https://help.tago.io/portal/en/kb/articles/device-data#Backing_Up_Data Backing Up Data

    **Parameters:**

        | **params**: :ref:`DeviceDataBackup`
        | Parameters for device data backup operation

        | **chunkID**: Optional[:ref:`GenericID`]
        | [Optional] Chunk ID if backup is for a specific chunk

    **Returns:**

        :ref:`DeviceDataBackupResponse`

.. code-block::
    :caption: **Example:**

        resources = Resources()
        import time
        timestamp = int(time.time())
        result = resources.devices.dataBackup({
            "deviceID": "device-id-123",
            "file_address": f"/backups/device-id-123/{timestamp}",
            "headers": True
        })
        print(result)  # {'file_address': 'backups/device-id-123/1736433519380.csv'}


===========
dataRestore
===========

Restores data to a device from a CSV file in TagoIO Files.

    **See:**

        https://help.tago.io/portal/en/kb/articles/device-data#Importing Importing Device Data
        https://api.docs.tago.io/#7ebca255-6c38-43d3-97d0-9b62155f202e Import Data API

    **Parameters:**

        | **params**: :ref:`DeviceDataRestore`
        | Parameters for device data restore operation

    **Returns:**

        str

.. code-block::
    :caption: **Example:**

        resources = Resources()
        result = resources.devices.dataRestore({
            "deviceID": "device-id-123",
            "file_address": "/backups/backup.csv"
        })
        print(result)  # Data import added to the queue successfully!


======
delete
======

Permanently deletes a device from the account along with all its data.

    **See:**

        https://help.tago.io/portal/en/kb/articles/478-devices Devices Overview

    **Parameters:**

        | **deviceID**: :ref:`GenericID`
        | Device ID

    **Returns:**

        str

.. code-block::
    :caption: **Example:**

        resources = Resources()
        result = resources.devices.delete("device-id-123")
        print(result)  # Successfully Removed


===========
deleteChunk
===========

Deletes a chunk from an immutable device.

    **See:**

        https://help.tago.io/portal/en/kb/articles/chunk-management#Delete_chunks Delete Chunks

    **Parameters:**

        | **deviceID**: :ref:`GenericID`
        | Device ID

        | **chunkID**: :ref:`GenericID`
        | Chunk ID

    **Returns:**

        str

.. code-block::
    :caption: **Example:**

        resources = Resources()
        result = resources.devices.deleteChunk("device-id-123", "chunk-id-123")
        print(result)  # Chunk chunk-id-123 deleted


================
deleteDeviceData
================

Deletes data from a device based on specified query parameters.

    **See:**

        https://help.tago.io/portal/en/kb/articles/device-data Device Data Management

    **Parameters:**

        | **deviceID**: :ref:`GenericID`
        | Device ID

        | **queryParam**: Optional[:ref:`DataQuery`]
        | [Optional] Query parameters to filter the results

    **Returns:**

        str

.. code-block::
    :caption: **Example:**

        resources = Resources()
        # Delete specific records by ID
        result = resources.devices.deleteDeviceData("device-id-123", {
            "ids": ["record-id-1", "record-id-2"]
        })
        # Delete by variable
        result = resources.devices.deleteDeviceData("device-id-123", {
            "variables": ["old_sensor"],
            "qty": 100
        })
        print(result)  # Successfully Removed


====
edit
====

Modifies any property of an existing device.

    **See:**

        https://help.tago.io/portal/en/kb/articles/478-devices Devices Overview

    **Parameters:**

        | **deviceID**: :ref:`GenericID`
        | Device ID

        | **deviceObj**: :ref:`DeviceEditInfo`
        | Device object with fields to replace

    **Returns:**

        str

.. code-block::
    :caption: **Example:**

        resources = Resources()
        result = resources.devices.edit("device-id-123", {
            "name": "Updated Sensor Name",
            "active": False,
            "tags": [{"key": "location", "value": "warehouse"}]
        })
        print(result)  # Successfully Updated


==============
editDeviceData
==============

Modifies existing data records in a device. Requires the data record ID.

    **See:**

        https://help.tago.io/portal/en/kb/articles/device-data Device Data Management

    **Parameters:**

        | **deviceID**: :ref:`GenericID`
        | Device ID

        | **updatedData**: Union[DataEdit, List[DataEdit]]
        | An array or one object with data to be updated

    **Returns:**

        str

.. code-block::
    :caption: **Example:**

        resources = Resources()
        result = resources.devices.editDeviceData("device-id-123", {
            "id": "data-record-id",
            "value": 30.0,
            "unit": "°F"
        })
        # Edit multiple records
        result = resources.devices.editDeviceData("device-id-123", [
            {"id": "record-1-id", "value": 25.5},
            {"id": "record-2-id", "value": 65}
        ])
        print(result)  # Device Data Updated


===============
emptyDeviceData
===============

Permanently removes all data from a device. This operation cannot be undone.

    **See:**

        https://help.tago.io/portal/en/kb/articles/device-data Device Data Management

    **Parameters:**

        | **deviceID**: :ref:`GenericID`
        | Device ID

    **Returns:**

        str

.. code-block::
    :caption: **Example:**

        resources = Resources()
        result = resources.devices.emptyDeviceData("device-id-123")
        print(result)  # All data has been removed


========
getChunk
========

Retrieves chunk information from an immutable device.

    **See:**

        https://help.tago.io/portal/en/kb/articles/chunk-management Chunk Management

    **Parameters:**

        | **deviceID**: :ref:`GenericID`
        | Device ID

    **Returns:**

        List[:ref:`DeviceChunkData`]

.. code-block::
    :caption: **Example:**

        resources = Resources()
        chunks = resources.devices.getChunk("device-id-123")
        print(chunks)  # [{'amount': 0, 'id': 'chunk-id-123', 'from_date': '2025-01-09T00:00:00.000+00:00', ...}]


=============
getDeviceData
=============

Retrieves data from all variables in the device with optional query filters.

    **See:**

        https://help.tago.io/portal/en/kb/articles/device-data Device Data Management

    **Parameters:**

        | **deviceID**: :ref:`GenericID`
        | Device ID

        | **queryParams**: Optional[:ref:`DataQuery`]
        | [Optional] Query parameters to filter the results

    **Returns:**

        List[:ref:`CommonData`]

.. code-block::
    :caption: **Example:**

        resources = Resources()
        # Get all data
        data = resources.devices.getDeviceData("device-id-123")
        # Get specific variable data
        temp_data = resources.devices.getDeviceData("device-id-123", {
            "variables": ["temperature"],
            "qty": 10
        })
        print(temp_data)  # [{'variable': 'temperature', 'value': 25.5, 'time': '...', ...}]


====
info
====

Retrieves detailed information about a specific device.

    **See:**

        https://help.tago.io/portal/en/kb/articles/478-devices Devices Overview

    **Parameters:**

        | **deviceID**: :ref:`GenericID`
        | Device ID

    **Returns:**

        :ref:`DeviceInfo`

.. code-block::
    :caption: **Example:**

        resources = Resources()
        device_info = resources.devices.info("device-id-123")
        print(device_info)  # {'id': '...', 'name': '...', 'type': 'mutable', ...}


==========
listDevice
==========

Retrieves a list of all devices from the account with optional filtering and pagination.

    **See:**

        https://help.tago.io/portal/en/kb/articles/478-devices Devices Overview

    **Parameters:**

        | **queryObj**: Optional[:ref:`DeviceQuery`]
        | [Optional] Search query params

    **Returns:**

        List[:ref:`DeviceListItem`]

.. code-block::
    :caption: **Example:**

        resources = Resources()
        devices = resources.devices.listDevice({
            "page": 1,
            "amount": 20,
            "fields": ["id", "name", "active"],
            "filter": {"name": "Temperature*"},
            "orderBy": ["name", "asc"]
        })
        print(devices)  # [{'id': 'device-id-123', 'name': 'Temperature Sensor', ...}]


=========
paramList
=========

Retrieves a list of configuration parameters for a device.

    **See:**

        https://help.tago.io/portal/en/kb/articles/configuration-parameters Configuration Parameters

    **Parameters:**

        | **deviceID**: :ref:`GenericID`
        | Device ID

        | **sentStatus**: Optional[bool]
        | [Optional] True return only sent=true, False return only sent=false

    **Returns:**

        List[:ref:`ConfigurationParams`]

.. code-block::
    :caption: **Example:**

        resources = Resources()
        # Get all parameters
        params = resources.devices.paramList("device-id-123")
        # Get only sent parameters
        sent_params = resources.devices.paramList("device-id-123", sentStatus=True)
        print(params)  # [{'id': '...', 'key': 'threshold', 'value': '25.5', 'sent': False}]


===========
paramRemove
===========

Removes a specific configuration parameter from a device.

    **See:**

        https://help.tago.io/portal/en/kb/articles/configuration-parameters Configuration Parameters

    **Parameters:**

        | **deviceID**: :ref:`GenericID`
        | Device ID

        | **paramID**: :ref:`GenericID`
        | Parameter ID

    **Returns:**

        str

.. code-block::
    :caption: **Example:**

        resources = Resources()
        result = resources.devices.paramRemove("device-id-123", "param-id-456")
        print(result)  # Successfully Removed


========
paramSet
========

Creates new configuration parameters or updates existing ones for a device.

    **See:**

        https://help.tago.io/portal/en/kb/articles/configuration-parameters Configuration Parameters

    **Parameters:**

        | **deviceID**: :ref:`GenericID`
        | Device ID

        | **configObj**: Union[:ref:`ConfigurationParams`, List[:ref:`ConfigurationParams`]]
        | Configuration Data

        | **paramID**: Optional[:ref:`GenericID`]
        | [Optional] Parameter ID

    **Returns:**

        str

.. code-block::
    :caption: **Example:**

        resources = Resources()
        # Create new parameter
        result = resources.devices.paramSet("device-id-123", {
            "key": "threshold",
            "value": "25.5",
            "sent": False
        })
        # Update existing parameter
        result = resources.devices.paramSet("device-id-123", {
            "key": "threshold",
            "value": "30.0",
            "sent": False
        }, "param-id-456")
        print(result)  # Successfully Updated


==============
sendDeviceData
==============

Sends data to a device. Accepts a single data object or an array of data objects.

    **See:**

        https://help.tago.io/portal/en/kb/articles/device-data Device Data Management

    **Parameters:**

        | **deviceID**: :ref:`GenericID`
        | Device ID

        | **data**: Union[DataCreate, List[DataCreate]]
        | An array or one object with data to be sent to TagoIO

    **Returns:**

        str

.. code-block::
    :caption: **Example:**

        resources = Resources()
        result = resources.devices.sendDeviceData("device-id-123", {
            "variable": "temperature",
            "value": 25.5,
            "unit": "°C",
            "time": "2025-01-09 13:44:33",
            "location": {"lat": 42.2974279, "lng": -85.628292}
        })
        # Send multiple data points
        result = resources.devices.sendDeviceData("device-id-123", [
            {"variable": "temperature", "value": 25.5},
            {"variable": "humidity", "value": 60}
        ])
        print(result)  # Successfully Inserted


===========
tokenCreate
===========

Generates and retrieves a new authentication token for a device.

    **See:**

        https://help.tago.io/portal/en/kb/articles/495-access-tokens Device Tokens

    **Parameters:**

        | **deviceID**: :ref:`GenericID`
        | Device ID

        | **tokenParams**: :ref:`CommonTokenData`
        | Params for new token

    **Returns:**

        :ref:`TokenCreateResponse`

.. code-block::
    :caption: **Example:**

        resources = Resources()
        result = resources.devices.tokenCreate("device-id-123", {
            "name": "Production Token",
            "permission": "write",
            "expire_time": "never"
        })
        print(result)  # {'token': 'new-token-value', 'expire_date': None}


===========
tokenDelete
===========

Permanently deletes an authentication token.

    **See:**

        https://help.tago.io/portal/en/kb/articles/495-access-tokens Device Tokens

    **Parameters:**

        | **token**: :ref:`GenericToken`
        | Token to delete

    **Returns:**

        str

.. code-block::
    :caption: **Example:**

        resources = Resources()
        result = resources.devices.tokenDelete("token-to-delete")
        print(result)  # Successfully Removed


=========
tokenList
=========

Retrieves a list of all authentication tokens for a device with optional filtering.

    **See:**

        https://help.tago.io/portal/en/kb/articles/495-access-tokens Device Tokens

    **Parameters:**

        | **deviceID**: :ref:`GenericID`
        | Device ID

        | **queryObj**: Optional[:ref:`ListDeviceTokenQuery`]
        | [Optional] Search query params

    **Returns:**

        List[:ref:`DeviceTokenDataList`]

.. code-block::
    :caption: **Example:**

        resources = Resources()
        tokens = resources.devices.tokenList("device-id-123", {
            "page": 1,
            "amount": 20,
            "fields": ["name", "token", "permission"],
            "orderBy": ["created_at", "desc"]
        })
        print(tokens)  # [{'name': 'Default Token', 'token': '...', 'permission': 'full', ...}]


.. toctree::

    Devices_Type
