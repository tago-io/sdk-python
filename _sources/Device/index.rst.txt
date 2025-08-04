**Device**
==========

In order to modify, add, delete or do anything else with the data inside buckets, it is necessary to use the device function.

========
Instance
========

    **Parameters:**

        | **token**: str
        | Device Token

        | *Optional* **region**: Regions: "usa-1" or "env"
        | Region is a optional parameter

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Device

        myDevice = Device({"token": "my_device_token", "region": "usa-1"})



====
info
====

Get information about the current device.

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Device

        myDevice = Device({ "token": "my_device_token" })
        result = myDevice.info()

========
sendData
========

Send data to device.

    **Parameters:**

        | **data**: :ref:`DeviceData` or list[:ref:`DeviceData`]
        | An array or one object with data to be send to TagoIO using device token

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Device

        myDevice = Device({ "token": "my_device_token" })
        result = myDevice.sendData({
            "variable": "temperature",
            "unit": "F",
            "value": 55,
            "time": "2015-11-03 13:44:33",
            "location": { "lat": 42.2974279, "lng": -85.628292 },
        })

=======
getData
=======

Get data from TagoIO Device.

    **Parameters:**

        | **queryParams**: :ref:`DataQuery`
        | Object with query params

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Device

        myDevice = Device({ "token": "my_device_token" })
        result = myDevice.getData({
            "query": "last_item",
            "variable": "humidity",
        })

========
editData
========

Edit data in a Mutable-type device.

    **Parameters:**

        | **data**: :ref:`DeviceData` or list[:ref:`DeviceData`]
        | Array or object with the data to be edited, each object with the data's ID.

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Device

        myDevice = Device({"token": "my_device_token"})
        result = myDevice.editData(
            {
                "id": "id_of_the_data_item",
                "value": "123",
                "time": "2022-04-01 12:34:56",
                "location": {"lat": 42.2974279, "lng": -85.628292},
            }
        )

==========
deleteData
==========

Delete data from device.

    **Parameters:**

        | **queryParams**: :ref:`DataQuery`
        | Object with query params
        | If not pass any query param, it will delete the last item

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Device

        myDevice = Device({ "token": "my_device_token" });
        result = myDevice.deleteData({
            "query": "last_item",
            "variable": "humidity",
            "value": 10
        });

=============
getParameters
=============

Get parameters from device.

    **Parameters:**

        | **onlyUnRead**: bool
        | set true to get only unread parameters

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Device

        myDevice = Device({ "token": "my_device_token" })
        result = myDevice.getParameters()

==================
setParameterAsRead
==================

Mark parameter as read.

    **Parameters:**

        | **parameterID**: GenericID: str
        | Parameter identification

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Device

        myDevice = Device({ "token": "my_device_token" })
        result = myDevice.setParameterAsRead(parameterID="parameter_id")


.. toctree::

    Device_Type



