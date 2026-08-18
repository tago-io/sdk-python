from requests_mock.mocker import Mocker

from tagoio_sdk import TagoTiP


def testTagoTiPCmd(requests_mock: Mocker) -> None:
    """Test cmd method of TagoTiP client."""
    requests_mock.post("https://api.tago.io/tip/cmd", json={"status": True, "result": "ok"})

    tagotip = TagoTiP({"token": "your-service-authorization-token"})

    result = tagotip.cmd(
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
    assert requests_mock.last_request.headers["token"] == "your-service-authorization-token"
