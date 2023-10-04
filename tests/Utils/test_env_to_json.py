from tagoio_sdk.modules.Utils.envToJson import envToJson

CONTEXT_ENVIRONMENT = [
    {"key": "account_token", "value": "test_token"},
    {"key": "device_token", "value": "test_token"},
    {"key": "input", "value": "95"},
    {"key": "output", "value": "95"},
]


def test_env_to_json():
    """Test envToJson function."""
    expected = {
        "account_token": "test_token",
        "device_token": "test_token",
        "input": "95",
        "output": "95",
    }
    assert envToJson(CONTEXT_ENVIRONMENT) == expected
