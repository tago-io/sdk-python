from src.tagoio_sdk.common.tagoio_module import TagoIOModule


def test_converter_dict_param_filter_single_key_value():
    """
    Test case 1: dictionary with single key-value pair
    """
    params = {"filter": {"tags": [{"key": "org_id", "value": "123"}]}}
    expected_result = {"filter[tags][0][key]": "org_id", "filter[tags][0][value]": "123"}

    tokenFake = {"token": "fake_token"}
    TagoIOModule(params=tokenFake)._converter_dict_param_filter(params) == expected_result

    assert params == expected_result


def test_converter_dict_param_filter_multiple_key_value():
    """
    Test case 2: dictionary with multiple key-value pairs
    """
    params = {
        "filter": {
            "tags": [
                {"key": "org_id", "value": "123"},
                {"key": "device_type", "value": "test"}
            ]
        }
    }
    expected_result = {
        "filter[tags][0][key]": "org_id",
        "filter[tags][0][value]": "123",
        "filter[tags][1][key]": "device_type",
        "filter[tags][1][value]": "test"
    }

    tokenFake = {"token": "fake_token"}
    TagoIOModule(params=tokenFake)._converter_dict_param_filter(params) == expected_result

    assert params == expected_result


def test_converter_dict_param_filter_nested_dict():
    """
    Test case 3: nested dictionary
    """
    params = {"filter": {"tags": [{"key": "org_id", "value": "123"}]},
              "sort": {"field": "created_at", "order": "asc"}}
    expected_result = {
        "filter[tags][0][key]": "org_id",
        "filter[tags][0][value]": "123",
        "sort": {"field": "created_at", "order": "asc"}
    }

    tokenFake = {"token": "fake_token"}
    TagoIOModule(params=tokenFake)._converter_dict_param_filter(params) == expected_result

    assert params == expected_result


def test_converter_dict_param_filter_empty_dict():
    """
    Test case 4: empty dictionary
    """
    params = {}
    expected_result = {}

    tokenFake = {"token": "fake_token"}
    TagoIOModule(params=tokenFake)._converter_dict_param_filter(params) == expected_result

    assert params == expected_result
