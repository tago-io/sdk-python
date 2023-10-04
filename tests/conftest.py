import pytest

from src.tagoio_sdk.common.Common_Type import Data
from src.tagoio_sdk.modules.Device.Device_Type import DeviceInfo
from src.tagoio_sdk.modules.Resources.Device_Type import ConfigurationParams
from src.tagoio_sdk.modules.Resources.IntegrationNetworkType import NetworkInfo


@pytest.fixture
def mockNetworkInfo() -> NetworkInfo:
    """
    Mock to return the object NetworkInfo.
    """

    return {
        "status": True,
        "result": {
            "id": "5ede22a7427104001c248b08",
            "name": "LoRaWAN Activity",
            "profile": "5bbcb03b667d7a002e56664b",
            "middleware_endpoint": "https://lorawan.tago.io",
        },
    }


@pytest.fixture
def mockListNetwork() -> list[NetworkInfo]:
    """
    Mock to return the list of NetworkInfo.
    """

    return {
        "status": True,
        "result": [
            {"id": "60af66df0ae39d0012b0bbe9", "name": "AWS IoT"},
            {"id": "5d48632019b67f001c874a6b", "name": "BeWhere"},
        ],
    }


@pytest.fixture
def mockDeviceInfo() -> DeviceInfo:
    """
    Mock to return the object DeviceInfo.
    """

    return {
        "status": True,
        "result": {
            "active": True,
            "bucket": {"id": "63f50a69fd802b000ac1aa76", "name": "Device #1"},
            "connector": "5f5a8f3351d4db99c40dece5",
            "created_at": "2023-02-21T18:16:09.817Z",
            "description": (
                "Connect any device using HTTPS protocol directly to send/get data "
            ),
            "id": "63f50a69fd802b000ac1aa76",
            "last_input": "2023-02-24T11:18:54.116Z",
            "name": "Device #1",
            "network": "5bbd0d144051a50034cd19fb",
            "payload_decoder": None,
            "profile": "63f4e08fb26aff0009ab99c0",
            "tags": [],
            "updated_at": "2023-02-21T18:16:09.817Z",
            "visible": True,
            "type": "mutable",
            "data_retention": "forever",
        },
    }


@pytest.fixture
def mockBodyCreateDevice() -> Data:
    """
    Mock to return the object Data.
    """

    return {
        "variable": "temperature",
        "unit": "F",
        "value": "80",
        "time": "2021-01-01T00:00:00.000Z",
        "location": {"lat": 42.2974279, "lng": -85.628292},
    }


@pytest.fixture
def mockConfigurationParams() -> ConfigurationParams:
    """
    Mock to return the object ConfigurationParams.
    """
    return {
        "id": "fake_id",
        "key": "phone",
        "value": "fake_value",
        "sent": True,
    }


@pytest.fixture
def mockReturnGetData() -> list[Data]:
    """
    Mock to return ten objects of the ConfigurationParams.
    """

    data = []

    for _ in range(10):
        data.append(
            {
                "id": _,
                "variable": "temperature",
                "unit": "F",
                "value": "80",
                "time": "2021-01-01T00:00:00.000Z",
                "location": {"lat": 42.2974279, "lng": -85.628292},
            }
        )

    return data
