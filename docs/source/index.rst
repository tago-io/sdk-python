TagoIO - Python SDK
===================

**Installation**

.. code-block::

        bash
        poetry install
        poetry run pytest tests/
        poetry run flake8 src

**Quick Example**

Insert Device Data

.. code-block::

        from tagoio_sdk.modules.Device.Device import Device
        myDevice = Device({ "token": "00000000-2ec4-11e6-a77d-991b8f63b767" })
        result = myDevice.sendData({
            "variable": "temperature",
            "unit": "F",
            "value": 55,
            "time": "2015-11-03 13:44:33",
            "location": { "lat": 42.2974279, "lng": -85.628292 },
        })
        print(result) # Success message: 1 data added


If you have any questions, feel free to check our `Help Center <https://help.tago.io/portal/en/home>`_.

**License**

TagoIO SDK for Python is released under the `[Apache-2.0 License] <https://github.com/tago-io/sdk-python/blob/master/LICENSE>`_

.. toctree::

    Device/index
    Services/index
