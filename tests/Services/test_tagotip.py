import os

from requests_mock.mocker import Mocker

from tagoio_sdk.modules.Services.Services import Services


os.environ["T_ANALYSIS_TOKEN"] = "your_token_value"


def testTagoTiPCmd(requests_mock: Mocker) -> None:
    """Test cmd method of TagoTiP service."""
    requests_mock.post(
        "https://api.tago.io/tip/cmd", json={"status": True, "result": "ok"}
    )

    services = Services({"token": "your-service-authorization-token"})

    result = services.tagotip.cmd(
        {
            "serial": "mqtt1",
            "protocol": "mqtt",
            "body": "reboot-now",
        }
    )

    assert result == "ok"
    assert requests_mock.last_request.json() == {
        "serial": "mqtt1",
        "protocol": "mqtt",
        "body": "reboot-now",
    }
