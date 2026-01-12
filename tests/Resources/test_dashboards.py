import os

from requests_mock.mocker import Mocker

from tagoio_sdk.modules.Resources.Dashboards_Type import DashboardInfo
from tagoio_sdk.modules.Resources.Resources import Resources

os.environ["T_ANALYSIS_TOKEN"] = "your_token_value"


def mockDashboardList() -> list[DashboardInfo]:
    return {
        "status": True,
        "result": [
            {
                "id": "dashboard_id_1",
                "label": "Dashboard 1",
                "created_at": "2023-02-21T15:17:35.759Z",
                "updated_at": "2023-02-21T15:17:35.759Z",
                "last_access": "2023-02-21T15:17:35.759Z",
                "arrangement": [],
                "tags": [{"key": "type", "value": "monitoring"}],
                "visible": True,
            },
            {
                "id": "dashboard_id_2",
                "label": "Dashboard 2",
                "created_at": "2023-02-21T16:17:35.759Z",
                "updated_at": "2023-02-21T16:17:35.759Z",
                "last_access": "2023-02-21T16:17:35.759Z",
                "arrangement": [],
                "tags": [{"key": "type", "value": "analytics"}],
                "visible": True,
            },
        ],
    }


def mockDashboardInfo() -> DashboardInfo:
    return {
        "status": True,
        "result": {
            "id": "dashboard_id_1",
            "label": "Dashboard 1",
            "created_at": "2023-02-21T15:17:35.759Z",
            "updated_at": "2023-02-21T15:17:35.759Z",
            "last_access": "2023-02-21T15:17:35.759Z",
            "arrangement": [],
            "tags": [{"key": "type", "value": "monitoring"}],
            "visible": True,
            "group_by": [],
            "tabs": [],
            "icon": {"url": "https://example.com/icon.png", "color": "#ff0000"},
            "background": {},
            "type": "normal",
            "blueprint_device_behavior": "more_than_one",
            "blueprint_selector_behavior": "open",
            "theme": {},
            "setup": {},
        },
    }


def mockCreateDashboard() -> dict:
    return {
        "status": True,
        "result": {"dashboard": "dashboard_id_new"},
    }


def mockDuplicateDashboard() -> dict:
    return {
        "status": True,
        "result": {
            "dashboard_id": "dashboard_id_duplicate",
            "message": "Dashboard duplicated successfully",
        },
    }


def mockPublicKey() -> dict:
    return {
        "status": True,
        "result": {
            "token": "public_token_123",
            "expire_time": "2025-01-02T00:00:00.000Z",
        },
    }


def mockDevicesRelated() -> list:
    return {
        "status": True,
        "result": [
            {"id": "device_id_1", "bucket": "bucket_id_1"},
            {"id": "device_id_2", "bucket": "bucket_id_2"},
        ],
    }


def mockAnalysisRelated() -> list:
    return {
        "status": True,
        "result": [
            {"id": "analysis_id_1", "name": "Analysis 1"},
            {"id": "analysis_id_2", "name": "Analysis 2"},
        ],
    }


def testDashboardsMethodList(requests_mock: Mocker) -> None:
    """Test listDashboard method of Dashboards class."""
    mock_response = mockDashboardList()
    requests_mock.get("https://api.tago.io/dashboard", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    query = {
        "page": 1,
        "fields": ["id", "label"],
        "amount": 20,
        "orderBy": ["label", "asc"],
    }

    result = resources.dashboards.listDashboard(query)

    # Check if the result is a list
    assert isinstance(result, list)
    # Check if the result has the expected items
    assert len(result) == 2
    # Check if items have expected properties
    assert result[0]["id"] == "dashboard_id_1"
    assert result[0]["label"] == "Dashboard 1"
    assert result[1]["id"] == "dashboard_id_2"
    assert result[1]["label"] == "Dashboard 2"


def testDashboardsMethodCreate(requests_mock: Mocker) -> None:
    """Test create method of Dashboards class."""
    mock_response = mockCreateDashboard()
    requests_mock.post("https://api.tago.io/dashboard", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    dashboard_data = {
        "label": "New Dashboard",
        "arrangement": [],
        "tags": [{"key": "type", "value": "monitoring"}],
        "visible": True,
    }

    result = resources.dashboards.create(dashboard_data)

    # Check if result has expected structure
    assert result["dashboard"] == "dashboard_id_new"


def testDashboardsMethodEdit(requests_mock: Mocker) -> None:
    """Test edit method of Dashboards class."""
    mock_response = {
        "status": True,
        "result": "Successfully Updated",
    }

    requests_mock.put("https://api.tago.io/dashboard/dashboard_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    dashboard_data = {
        "label": "Updated Dashboard",
        "visible": False,
    }

    result = resources.dashboards.edit("dashboard_id_1", dashboard_data)

    # Check if result has expected message
    assert result == "Successfully Updated"


def testDashboardsMethodDelete(requests_mock: Mocker) -> None:
    """Test delete method of Dashboards class."""
    mock_response = {
        "status": True,
        "result": "Successfully Removed",
    }

    requests_mock.delete("https://api.tago.io/dashboard/dashboard_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    result = resources.dashboards.delete("dashboard_id_1")

    # Check if result has expected message
    assert result == "Successfully Removed"


def testDashboardsMethodInfo(requests_mock: Mocker) -> None:
    """Test info method of Dashboards class."""
    mock_response = mockDashboardInfo()
    requests_mock.get("https://api.tago.io/dashboard/dashboard_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    result = resources.dashboards.info("dashboard_id_1")

    # Check if result has expected properties
    assert result["id"] == "dashboard_id_1"
    assert result["label"] == "Dashboard 1"
    assert result["visible"] == True
    assert result["type"] == "normal"
    assert len(result["tags"]) == 1
    assert result["tags"][0]["key"] == "type"
    assert result["tags"][0]["value"] == "monitoring"


def testDashboardsMethodDuplicate(requests_mock: Mocker) -> None:
    """Test duplicate method of Dashboards class."""
    mock_response = mockDuplicateDashboard()
    requests_mock.post("https://api.tago.io/dashboard/dashboard_id_1/duplicate", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    duplicate_options = {"new_label": "Copy of Dashboard 1"}

    result = resources.dashboards.duplicate("dashboard_id_1", duplicate_options)

    # Check if result has expected properties
    assert result["dashboard_id"] == "dashboard_id_duplicate"
    assert result["message"] == "Dashboard duplicated successfully"


def testDashboardsMethodGetPublicKey(requests_mock: Mocker) -> None:
    """Test getPublicKey method of Dashboards class."""
    mock_response = mockPublicKey()
    requests_mock.get("https://api.tago.io/dashboard/dashboard_id_1/share/public", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    result = resources.dashboards.getPublicKey("dashboard_id_1", "1day")

    # Check if result has expected properties
    assert result["token"] == "public_token_123"
    assert "expire_time" in result


def testDashboardsMethodListDevicesRelated(requests_mock: Mocker) -> None:
    """Test listDevicesRelated method of Dashboards class."""
    mock_response = mockDevicesRelated()
    requests_mock.get("https://api.tago.io/dashboard/dashboard_id_1/devices", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    result = resources.dashboards.listDevicesRelated("dashboard_id_1")

    # Check if the result is a list
    assert isinstance(result, list)
    # Check if the result has the expected items
    assert len(result) == 2
    # Check if items have expected properties
    assert result[0]["id"] == "device_id_1"
    assert result[0]["bucket"] == "bucket_id_1"


def testDashboardsMethodListAnalysisRelated(requests_mock: Mocker) -> None:
    """Test listAnalysisRelated method of Dashboards class."""
    mock_response = mockAnalysisRelated()
    requests_mock.get("https://api.tago.io/dashboard/dashboard_id_1/analysis", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    result = resources.dashboards.listAnalysisRelated("dashboard_id_1")

    # Check if the result is a list
    assert isinstance(result, list)
    # Check if the result has the expected items
    assert len(result) == 2
    # Check if items have expected properties
    assert result[0]["id"] == "analysis_id_1"
    assert result[0]["name"] == "Analysis 1"


def testDashboardsMethodRunWidgetHeaderButtonAnalysis(requests_mock: Mocker) -> None:
    """Test runWidgetHeaderButtonAnalysis method of Dashboards class."""
    mock_response = {
        "status": True,
        "result": "Analysis executed successfully",
    }

    requests_mock.post(
        "https://api.tago.io/analysis/analysis_id_1/run/dashboard_id_1/widget_id_1",
        json=mock_response,
    )

    resources = Resources({"token": "your_token_value"})

    scope_data = {"custom_data": "value"}

    result = resources.dashboards.runWidgetHeaderButtonAnalysis(
        "analysis_id_1", "dashboard_id_1", "widget_id_1", scope_data
    )

    # Check if result has expected message
    assert result == "Analysis executed successfully"


# Widget tests


def mockWidgetInfo() -> dict:
    return {
        "status": True,
        "result": {
            "id": "widget_id_1",
            "label": "Temperature Widget",
            "type": "display",
            "data": [
                {
                    "origin": "device_id_1",
                    "query": "last_value",
                    "variables": ["temperature"],
                }
            ],
            "display": {
                "show_units": True,
                "show_variables": True,
                "variables": [{"origin": "device_id_1", "variable": "temperature"}],
            },
            "dashboard": "dashboard_id_1",
            "realtime": True,
            "analysis_run": None,
        },
    }


def mockCreateWidget() -> dict:
    return {
        "status": True,
        "result": {"widget": "widget_id_new"},
    }


def testWidgetsMethodCreate(requests_mock: Mocker) -> None:
    """Test create method of DashboardWidgets class."""
    mock_response = mockCreateWidget()
    requests_mock.post("https://api.tago.io/dashboard/dashboard_id_1/widget/", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    widget_data = {
        "label": "New Widget",
        "type": "display",
        "data": [
            {
                "origin": "device_id_1",
                "query": "last_value",
                "variables": ["temperature"],
            }
        ],
        "display": {
            "show_units": True,
            "show_variables": True,
        },
    }

    result = resources.dashboards.widgets.create("dashboard_id_1", widget_data)

    # Check if result has expected structure
    assert result["widget"] == "widget_id_new"


def testWidgetsMethodEdit(requests_mock: Mocker) -> None:
    """Test edit method of DashboardWidgets class."""
    mock_response = {
        "status": True,
        "result": "Successfully Updated",
    }

    requests_mock.put(
        "https://api.tago.io/dashboard/dashboard_id_1/widget/widget_id_1",
        json=mock_response,
    )

    resources = Resources({"token": "your_token_value"})

    widget_data = {"label": "Updated Widget"}

    result = resources.dashboards.widgets.edit("dashboard_id_1", "widget_id_1", widget_data)

    # Check if result has expected message
    assert result == "Successfully Updated"


def testWidgetsMethodDelete(requests_mock: Mocker) -> None:
    """Test delete method of DashboardWidgets class."""
    mock_response = {
        "status": True,
        "result": "Successfully Removed",
    }

    requests_mock.delete(
        "https://api.tago.io/dashboard/dashboard_id_1/widget/widget_id_1",
        json=mock_response,
    )

    resources = Resources({"token": "your_token_value"})

    result = resources.dashboards.widgets.delete("dashboard_id_1", "widget_id_1")

    # Check if result has expected message
    assert result == "Successfully Removed"


def testWidgetsMethodInfo(requests_mock: Mocker) -> None:
    """Test info method of DashboardWidgets class."""
    mock_response = mockWidgetInfo()
    requests_mock.get(
        "https://api.tago.io/dashboard/dashboard_id_1/widget/widget_id_1",
        json=mock_response,
    )

    resources = Resources({"token": "your_token_value"})

    result = resources.dashboards.widgets.info("dashboard_id_1", "widget_id_1")

    # Check if result has expected properties
    assert result["id"] == "widget_id_1"
    assert result["label"] == "Temperature Widget"
    assert result["type"] == "display"
    assert result["realtime"] == True
    assert len(result["data"]) == 1


def testWidgetsMethodGetData(requests_mock: Mocker) -> None:
    """Test getData method of DashboardWidgets class."""
    mock_response = {
        "status": True,
        "result": {
            "widget": {"id": "widget_id_1", "dashboard": "dashboard_id_1"},
            "data": [{"variable": "temperature", "value": 25.5}],
        },
    }

    requests_mock.get("https://api.tago.io/data/dashboard_id_1/widget_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    params = {"start_date": "2025-01-01", "end_date": "2025-12-31", "timezone": "UTC"}

    result = resources.dashboards.widgets.getData("dashboard_id_1", "widget_id_1", params)

    # Check if result has expected structure
    assert "widget" in result
    assert result["widget"]["id"] == "widget_id_1"


def testWidgetsMethodSendData(requests_mock: Mocker) -> None:
    """Test sendData method of DashboardWidgets class."""
    mock_response = {
        "status": True,
        "result": ["1 Data Added"],
    }

    requests_mock.post("https://api.tago.io/data/dashboard_id_1/widget_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    data = {
        "origin": "device_id_1",
        "variable": "temperature",
        "value": 25.5,
        "unit": "C",
    }

    result = resources.dashboards.widgets.sendData("dashboard_id_1", "widget_id_1", data)

    # Check if result has expected message
    assert isinstance(result, list)
    assert result[0] == "1 Data Added"


def testWidgetsMethodEditData(requests_mock: Mocker) -> None:
    """Test editData method of DashboardWidgets class."""
    mock_response = {
        "status": True,
        "result": "Device Data Updated",
    }

    requests_mock.put("https://api.tago.io/data/dashboard_id_1/widget_id_1/data", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    data = {"origin": "device_id_1", "id": "data_id_1", "value": 26.0}

    result = resources.dashboards.widgets.editData("dashboard_id_1", "widget_id_1", data)

    # Check if result has expected message
    assert result == "Device Data Updated"


def testWidgetsMethodDeleteData(requests_mock: Mocker) -> None:
    """Test deleteData method of DashboardWidgets class."""
    mock_response = {
        "status": True,
        "result": "Successfully Removed",
    }

    requests_mock.delete("https://api.tago.io/data/dashboard_id_1/widget_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    id_pairs = ["data_1:device_1", "data_2:device_1"]

    result = resources.dashboards.widgets.deleteData("dashboard_id_1", "widget_id_1", id_pairs)

    # Check if result has expected message
    assert result == "Successfully Removed"


def testWidgetsMethodEditResource(requests_mock: Mocker) -> None:
    """Test editResource method of DashboardWidgets class."""
    mock_response = {
        "status": True,
        "result": "Resource Updated",
    }

    requests_mock.put(
        "https://api.tago.io/data/dashboard_id_1/widget_id_1/resource",
        json=mock_response,
    )

    resources = Resources({"token": "your_token_value"})

    resource_data = {
        "device": "device_id_1",
        "name": "Updated Device Name",
        "active": True,
    }

    options = {"identifier": "my-identifier"}

    result = resources.dashboards.widgets.editResource("dashboard_id_1", "widget_id_1", resource_data, options)

    # Check if result has expected message
    assert result == "Resource Updated"


def testWidgetsMethodTokenGenerate(requests_mock: Mocker) -> None:
    """Test tokenGenerate method of DashboardWidgets class."""
    mock_response = {
        "status": True,
        "result": {"widget_token": "widget_token_123"},
    }

    requests_mock.get(
        "https://api.tago.io/dashboard/dashboard_id_1/widget/widget_id_1/token",
        json=mock_response,
    )

    resources = Resources({"token": "your_token_value"})

    result = resources.dashboards.widgets.tokenGenerate("dashboard_id_1", "widget_id_1")

    # Check if result has expected properties
    assert result["widget_token"] == "widget_token_123"
