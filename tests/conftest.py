import pytest

from src.tagoio_sdk.common.Common_Type import Data
from src.tagoio_sdk.modules.Device.Device_Type import DeviceInfo
from src.tagoio_sdk.modules.Account.Device_Type import ConfigurationParams


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

    datas = []

    for _ in range(10):
        datas.append(
            {
                "id": _,
                "variable": "temperature",
                "unit": "F",
                "value": "80",
                "time": "2021-01-01T00:00:00.000Z",
                "location": {"lat": 42.2974279, "lng": -85.628292},
            }
        )

    return datas
