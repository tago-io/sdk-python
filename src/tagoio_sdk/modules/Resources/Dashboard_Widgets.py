from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.Common_Type import GenericToken
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Resources.Dashboards_Type import EditDataModel
from tagoio_sdk.modules.Resources.Dashboards_Type import EditDeviceResource
from tagoio_sdk.modules.Resources.Dashboards_Type import EditResourceOptions
from tagoio_sdk.modules.Resources.Dashboards_Type import GetDataModel
from tagoio_sdk.modules.Resources.Dashboards_Type import PostDataModel
from tagoio_sdk.modules.Resources.Dashboards_Type import WidgetInfo


class Widgets(TagoIOModule):
    def create(self, dashboardID: GenericID, widgetObj: WidgetInfo) -> Dict[str, GenericID]:
        """
        @description:
            Creates a new widget for a specified dashboard with the given configuration.
            After created, it is not added into the dashboard arrangement; it is necessary to edit
            the dashboard to include it in the arrangement.

        @see:
            https://help.tago.io/portal/en/kb/articles/15-dashboard-overview Dashboard Overview
            https://docs.tago.io/docs/tagoio/widgets/ Widgets

        @example:
            If receive an error "Authorization Denied", check policy **Dashboard** / **Create and Edit** in Access Management.
            ```python
            resources = Resources()
            result = resources.dashboards.widgets.create("dashboard-id-123", {
                "data": [{
                    "origin": "origin-id-123",
                    "query": "last_value",
                    "variables": ["temperature"]
                }],
                "display": {
                    "show_units": True,
                    "show_variables": True,
                    "variables": [{
                        "origin": "origin-id-123",
                        "variable": "temperature"
                    }]
                },
                "label": "Temperature",
                "type": "display",
            })
            print(result)  # {'widget': 'widget-id-456'}

            # To add the widget size to the dashboard
            # Before running this, make sure doesn't have more widgets in the dashboard.
            resources.dashboards.edit("dashboard-id-123", {
                "arrangement": [{"widget_id": result["widget"], "width": 1, "height": 2, "minW": 1, "minH": 2, "x": 0, "y": 0}]
            })
            ```
        """
        result = self.doRequest(
            {
                "path": f"/dashboard/{dashboardID}/widget/",
                "method": "POST",
                "body": widgetObj,
            }
        )

        return result

    def edit(self, dashboardID: GenericID, widgetID: GenericID, data: Dict) -> str:
        """
        @description:
            Updates an existing widget's configuration on a dashboard.

        @see:
            https://help.tago.io/portal/en/kb/articles/15-dashboard-overview Dashboard Overview
            https://docs.tago.io/docs/tagoio/widgets/ Widgets

        @example:
            If receive an error "Authorization Denied", check policy **Dashboard** / **Edit** in Access Management.
            ```python
            resources = Resources()
            result = resources.dashboards.widgets.edit("dashboard-id-123", "widget-id-456", {
                "label": "Updated Temperature",
            })
            print(result)  # Successfully Updated
            ```
        """
        result = self.doRequest(
            {
                "path": f"/dashboard/{dashboardID}/widget/{widgetID}",
                "method": "PUT",
                "body": data,
            }
        )

        return result

    def delete(self, dashboardID: GenericID, widgetID: GenericID) -> str:
        """
        @description:
            Permanently removes a widget from a dashboard.
            After deleted, it is not removed from the dashboard arrangement; it is necessary to edit
            the dashboard to remove it from the arrangement.

        @see:
            https://help.tago.io/portal/en/kb/articles/15-dashboard-overview Dashboard Overview
            https://docs.tago.io/docs/tagoio/widgets/ Widgets

        @example:
            If receive an error "Authorization Denied", check policy **Dashboard** / **Delete and Edit** in Access Management.
            ```python
            resources = Resources()
            result = resources.dashboards.widgets.delete("dashboard-id-123", "widget-id-456")
            print(result)  # Successfully Removed

            # To remove sizes from all widgets from a dashboard
            # Before running this, make sure doesn't have more widgets in the dashboard.
            resources.dashboards.edit("dashboard-id-123", {"arrangement": []})
            ```
        """
        result = self.doRequest(
            {
                "path": f"/dashboard/{dashboardID}/widget/{widgetID}",
                "method": "DELETE",
            }
        )

        return result

    def info(self, dashboardID: GenericID, widgetID: GenericID) -> WidgetInfo:
        """
        @description:
            Retrieves detailed information about a specific widget.

        @see:
            https://help.tago.io/portal/en/kb/articles/15-dashboard-overview Dashboard Overview
            https://docs.tago.io/docs/tagoio/widgets/ Widgets

        @example:
            If receive an error "Authorization Denied", check policy **Dashboard** / **Access** in Access Management.
            ```python
            resources = Resources()
            result = resources.dashboards.widgets.info("dashboard-id-123", "widget-id-456")
            print(result)  # {'id': 'widget-id-456', 'data': [{'query': 'last_value', ...}, ...], ...}
            ```
        """
        result = self.doRequest(
            {
                "path": f"/dashboard/{dashboardID}/widget/{widgetID}",
                "method": "GET",
            }
        )

        return result

    def getData(
        self,
        dashboardID: GenericID,
        widgetID: GenericID,
        params: Optional[GetDataModel] = None,
    ) -> object:
        """
        @description:
            Retrieves data or resource list for a specific widget based on the given parameters.

        @see:
            https://help.tago.io/portal/en/kb/articles/15-dashboard-overview Dashboard Overview
            https://docs.tago.io/docs/tagoio/widgets/ Widgets

        @example:
            ```python
            resources = Resources()
            result = resources.dashboards.widgets.getData("dashboard-id-123", "widget-id-456", {
                "start_date": "2025-01-01",
                "end_date": "2025-12-31",
                "timezone": "UTC"
            })
            print(result)  # {'widget': {'analysis_run': None, 'dashboard': '6791456f8b726c0009adccec', ...}, ...}
            ```
        """
        result = self.doRequest(
            {
                "path": f"/data/{dashboardID}/{widgetID}",
                "method": "GET",
                "params": params,
            }
        )

        return result

    def sendData(
        self,
        dashboardID: GenericID,
        widgetID: GenericID,
        data: Union[PostDataModel, List[PostDataModel]],
        bypassBucket: bool = False,
    ) -> object:
        """
        @description:
            Sends new data values to be displayed in the widget.

        @see:
            https://help.tago.io/portal/en/kb/articles/15-dashboard-overview Dashboard Overview
            https://docs.tago.io/docs/tagoio/widgets/ Widgets

        @example:
            ```python
            resources = Resources()
            result = resources.dashboards.widgets.sendData("dashboard-id-123", "widget-id-456", {
                "origin": "origin-id-123",
                "variable": "temperature",
                "value": 25.5,
                "unit": "C"
            })
            print(result)  # ['1 Data Added']
            ```
        """
        result = self.doRequest(
            {
                "path": f"/data/{dashboardID}/{widgetID}",
                "method": "POST",
                "params": {
                    "bypass_bucket": bypassBucket,
                },
                "body": data,
            }
        )

        return result

    def editData(
        self,
        dashboardID: GenericID,
        widgetID: GenericID,
        data: Union[EditDataModel, List[EditDataModel]],
        bypassBucket: bool = False,
    ) -> object:
        """
        @description:
            Updates existing data values for a specific widget.

        @see:
            https://help.tago.io/portal/en/kb/articles/15-dashboard-overview Dashboard Overview
            https://docs.tago.io/docs/tagoio/widgets/ Widgets

        @example:
            ```python
            resources = Resources()
            result = resources.dashboards.widgets.editData("dashboard-id-123", "widget-id-456", {
                "origin": "origin-id-123",
                "id": "data-id-789",
                "value": 25.5
            })
            print(result)  # Device Data Updated
            ```
        """
        result = self.doRequest(
            {
                "path": f"/data/{dashboardID}/{widgetID}/data",
                "method": "PUT",
                "params": {
                    "bypass_bucket": bypassBucket,
                },
                "body": data,
            }
        )

        return result

    def deleteData(self, dashboardID: GenericID, widgetID: GenericID, idPairs: List[str]) -> str:
        """
        @description:
            Removes multiple data items from the widget by pairs of data ID and resource ID.

        @see:
            https://help.tago.io/portal/en/kb/articles/15-dashboard-overview Dashboard Overview
            https://docs.tago.io/docs/tagoio/widgets/ Widgets

        @example:
            ```python
            resources = Resources()
            result = resources.dashboards.widgets.deleteData(
                "dashboard-id",
                "widget-id",
                [
                    "data_1-id:device_A-id",
                    "data_2-id:device_A-id",
                    "data_3-id:device_B-id",
                ]
            )
            print(result)  # Successfully Removed
            ```
        """
        result = self.doRequest(
            {
                "path": f"/data/{dashboardID}/{widgetID}",
                "method": "DELETE",
                "params": {
                    "ids": idPairs,
                },
            }
        )

        return result

    def editResource(
        self,
        dashboardID: GenericID,
        widgetID: GenericID,
        resourceData: Union[EditDeviceResource, List[EditDeviceResource]],
        options: Optional[EditResourceOptions] = None,
    ) -> object:
        """
        @description:
            Updates resource values associated with the widget.

        @see:
            https://help.tago.io/portal/en/kb/articles/15-dashboard-overview Dashboard Overview
            https://docs.tago.io/docs/tagoio/widgets/ Widgets

        @example:
            ```python
            resources = Resources()
            result = resources.dashboards.widgets.editResource(
                "dashboard-id-123",
                "widget-id-456",
                {
                    "device": "device-id-789",
                    "name": "Updated Device Name",
                    "active": True
                },
                {"identifier": "my-identifier"}
            )
            print(result)  # Resource Updated
            ```
        """
        if options is None:
            options = {}

        result = self.doRequest(
            {
                "path": f"/data/{dashboardID}/{widgetID}/resource",
                "method": "PUT",
                "params": {
                    "widget_exec": options.get("identifier"),
                },
                "body": resourceData,
            }
        )

        return result

    def tokenGenerate(self, dashboardID: GenericID, widgetID: GenericID) -> Dict[str, GenericToken]:
        """
        @description:
            Generates a new authentication token for embedding a widget. Each call regenerates the token.

        @see:
            https://help.tago.io/portal/en/kb/articles/15-dashboard-overview Dashboard Overview
            https://docs.tago.io/docs/tagoio/widgets/ Widgets

        @example:
            ```python
            resources = Resources()
            result = resources.dashboards.widgets.tokenGenerate("dashboard-id-123", "widget-id-456")
            print(result)  # {'widget_token': 'widget-token-123'}
            ```
        """
        result = self.doRequest(
            {
                "path": f"/dashboard/{dashboardID}/widget/{widgetID}/token",
                "method": "GET",
            }
        )

        return result
