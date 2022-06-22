<br/>
<p align="center">
  <img src="https://assets.tago.io/tagoio/sdk.png" width="250px" alt="TagoIO"></img>
</p>

> NOTE: *This version (4.x.x) is still in development. You can access the current (3.x.x) version in [tago-io/tago-sdk-python](https://github.com/tago-io/tago-sdk-python).*

# TagoIO - Python SDK

Official Python SDK for TagoIO

## Installation

```bash
pip install tagoio-sdk
```

## Quick Example

If you have any questions, feel free to check our [Help Center](https://help.tago.io/portal/en/home)

### Insert Device Data

```python
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

### Edit Device Data

```python
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

## Development Commands

```bash
poetry install
poetry run pytest tests/
poetry run flake8 src
```

## License

TagoIO SDK for Python is released under the [Apache-2.0 License](https://github.com/tago-io/sdk-python/blob/master/LICENSE)
