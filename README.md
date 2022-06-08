<br/>
<p align="center">
  <img src="https://assets.tago.io/tagoio/sdk.png" width="250px" alt="TODO"></img>
</p>

Official Python SDK for TagoIO

## Installation

```
pip install tagoio-sdk
```

## Quick Example

# **Insert Device Data**

```
from tagoio_sdk import Device

myDevice = Device({ "token": "my_device_token" })
result = myDevice.sendData({
    "variable": "temperature",
    "unit": "F",
    "value": 55,
    "time": "2015-11-03 13:44:33",
    "location": { "lat": 42.2974279, "lng": -85.628292 },
})
```

## **Edit Device Data**

```
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
```

If you have any questions, feel free to check our [Help Center](https://help.tago.io/portal/en/home)

## License

TagoIO SDK for Python is released under the [Apache-2.0 License](https://github.com/tago-io/sdk-python/blob/master/LICENSE)
