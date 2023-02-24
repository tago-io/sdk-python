import pytest

from faker.generator import Generator
from src.tagoio_sdk.common.Common_Type import Data
from src.tagoio_sdk.modules.Device.Device_Type import DeviceInfo
from src.tagoio_sdk.modules.Account.Device_Type import ConfigurationParams


@pytest.fixture
def mockDeviceInfo(faker: Generator) -> DeviceInfo:
    """
    Mock to return the object DeviceInfo.

    :param faker are a plugin of pytest to generate fake data.
    https://faker.readthedocs.io/en/master/index.html
    """

    return {
        "status": True,
        "result": {
            "active": True,
            "bucket": {"id": faker.pystr(), "name": "Device #1"},
            "connector": "5f5a8f3351d4db99c40dece5",
            "created_at": faker.date_time().isoformat(),
            "description": (
                "Connect any device using HTTPS protocol directly to send/get data "
            ),
            "id": faker.pystr(),
            "last_input": faker.date_time().isoformat(),
            "name": "Device #1",
            "network": faker.pystr(),
            "payload_decoder": None,
            "profile": faker.pystr(),
            "tags": [],
            "updated_at": faker.date_time().isoformat(),
            "visible": True,
            "type": "mutable",
            "data_retention": "forever",
        },
    }


@pytest.fixture
def mockBodyCreateDevice(faker: Generator) -> Data:
    """
    Mock to return the object Data.

    :param faker are a plugin of pytest to generate fake data.
    https://faker.readthedocs.io/en/master/index.html
    """

    return {
        "variable": "temperature",
        "unit": "F",
        "value": faker.random_int(min=30, max=80),
        "time": faker.date_time().now().isoformat(),
        "location": {"lat": 42.2974279, "lng": -85.628292},
    }


@pytest.fixture
def mockConfigurationParams(faker: Generator) -> ConfigurationParams:
    """
    Mock to return the object ConfigurationParams.

    :param faker are a plugin of pytest to generate fake data.
    https://faker.readthedocs.io/en/master/index.html
    """
    return {
        "id": faker.pystr(),
        "key": "phone",
        "value": faker.phone_number(),
        "sent": True,
    }


@pytest.fixture
def mockReturnGetData(faker: Generator) -> list[Data]:
    """
    Mock to return ten objects of the ConfigurationParams.

    :param faker are a plugin of pytest to generate fake data.
    https://faker.readthedocs.io/en/master/index.html
    """

    datas = []

    for _ in range(10):
        datas.append(
            {
                "id": _,
                "variable": "temperature",
                "unit": "F",
                "value": faker.random_int(min=30, max=80),
                "time": faker.date_time().now().isoformat(),
                "location": {"lat": 42.2974279, "lng": -85.628292},
            }
        )

    return datas
