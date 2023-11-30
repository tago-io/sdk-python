<br/>
<p align="center">
  <img src="https://assets.tago.io/tagoio/sdk.png" width="250px" alt="TagoIO"></img>
</p>

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
from tagoio_sdk import Resources

resources = Resources()
resource.devices.sendDeviceData("myDeviceID", {
    "variable": "temperature",
    "unit": "F",
    "value": 55,
    "time": "2015-11-03 13:44:33",
    "location": {"lat": 42.2974279, "lng": -85.628292},
})
```

### Edit Device Data

```python
from tagoio_sdk import Resources

resources = Resource()
resource.devices.editDeviceData("myDeviceID", {
    "id": "idOfTheRecord",
    "value": "new value",
    "unit": "new unit"
})
```

## Development Commands

```bash
poetry install
poetry run pytest tests/
poetry run flake8 src
```

## License

TagoIO SDK for Python is released under the [Apache-2.0 License](https://github.com/tago-io/sdk-python/blob/master/LICENSE)
