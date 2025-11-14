from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import TypedDict

from tagoio_sdk.common.Common_Type import ExpireTimeOption
from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.Common_Type import Query
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Resources.Dashboard_Widgets import Widgets
from tagoio_sdk.modules.Resources.Dashboards_Type import AnalysisRelated
from tagoio_sdk.modules.Resources.Dashboards_Type import DashboardCreateInfo
from tagoio_sdk.modules.Resources.Dashboards_Type import DashboardInfo
from tagoio_sdk.modules.Resources.Dashboards_Type import DevicesRelated
from tagoio_sdk.modules.Resources.Dashboards_Type import PublicKeyResponse
from tagoio_sdk.modules.Utils.dateParser import dateParser
from tagoio_sdk.modules.Utils.dateParser import dateParserList


class Dashboards(TagoIOModule):
    def listDashboard(self, queryObj: Optional[Query] = None) -> List[DashboardInfo]:
        """
        @description:
            Lists all dashboards from your application with pagination support.

        @see:
            https://docs.tago.io/docs/tagoio/dashboards/ Dashboard Overview

        @example:
            If receive an error "Authorization Denied", check policy **Dashboard** / **Access** in Access Management.
            ```python
            resources = Resources()
            result = resources.dashboards.listDashboard({
                "page": 1,
                "fields": ["id", "name"],
                "amount": 10,
                "orderBy": ["label", "asc"]
            })
            print(result)  # [{'id': 'dashboard-id-123', 'label': 'My Dashboard', ...}, ...]
            ```
        """

        if queryObj is None:
            queryObj = {}
        if "orderBy" in queryObj:
            firstArgument = queryObj["orderBy"][0]
            secondArgument = queryObj["orderBy"][1]
            orderBy = f"{firstArgument},{secondArgument}"
        else:
            orderBy = "label,asc"

        result = self.doRequest(
            {
                "path": "/dashboard",
                "method": "GET",
                "params": {
                    "page": queryObj.get("page") or 1,
                    "fields": queryObj.get("fields") or ["id", "name"],
                    "filter": queryObj.get("filter") or {},
                    "amount": queryObj.get("amount") or 20,
                    "orderBy": orderBy,
                },
            }
        )

        result = dateParserList(result, ["created_at", "updated_at", "last_access"])
        return result

    class CreateDashboardResponse(TypedDict):
        dashboard: GenericID

    def create(self, dashboardObj: DashboardCreateInfo) -> CreateDashboardResponse:
        """
        @description:
            Creates a new dashboard in your application.

        @see:
            https://docs.tago.io/docs/tagoio/dashboards/ Dashboard Overview

        @example:
            If receive an error "Authorization Denied", check policy **Dashboard** / **Create** in Access Management.
            ```python
            resources = Resources()
            result = resources.dashboards.create({
                "label": "My Dashboard",
                "tags": [{"key": "type", "value": "monitoring"}]
            })
            print(result)  # {'dashboard': 'dashboard-id-123'}
            ```
        """
        result = self.doRequest(
            {
                "path": "/dashboard",
                "method": "POST",
                "body": dashboardObj,
            }
        )

        return result

    def edit(self, dashboardID: GenericID, dashboardObj: Dict[str, Any]) -> str:
        """
        @description:
            Modifies an existing dashboard's properties.

        @see:
            https://docs.tago.io/docs/tagoio/dashboards/ Dashboard Overview

        @example:
            If receive an error "Authorization Denied", check policy **Dashboard** / **Edit** in Access Management.
            ```python
            resources = Resources()
            result = resources.dashboards.edit("dashboard-id-123", {
                "label": "Updated Dashboard",
                "active": False
            })
            print(result)  # Successfully Updated
            ```
        """
        result = self.doRequest(
            {
                "path": f"/dashboard/{dashboardID}",
                "method": "PUT",
                "body": dashboardObj,
            }
        )

        return result

    def delete(self, dashboardID: GenericID) -> str:
        """
        @description:
            Deletes a dashboard from the application.

        @see:
            https://docs.tago.io/docs/tagoio/dashboards/ Dashboard Overview

        @example:
            If receive an error "Authorization Denied", check policy **Dashboard** / **Delete** in Access Management.
            ```python
            resources = Resources()
            result = resources.dashboards.delete("dashboard-id-123")
            print(result)  # Successfully Removed
            ```
        """
        result = self.doRequest(
            {
                "path": f"/dashboard/{dashboardID}",
                "method": "DELETE",
            }
        )

        return result

    def info(self, dashboardID: GenericID) -> DashboardInfo:
        """
        @description:
            Retrieves detailed information about a specific dashboard.

        @see:
            https://docs.tago.io/docs/tagoio/dashboards/ Dashboard Overview

        @example:
            If receive an error "Authorization Denied", check policy **Dashboard** / **Access** in Access Management.
            ```python
            resources = Resources()
            dashboard_info = resources.dashboards.info("dashboard-id-123")
            print(dashboard_info)  # {'id': 'dashboard-id-123', 'label': 'My Dashboard', ...}
            ```
        """
        result = self.doRequest(
            {
                "path": f"/dashboard/{dashboardID}",
                "method": "GET",
            }
        )

        result = dateParser(result, ["created_at", "updated_at", "last_access"])
        return result

    class DuplicateDashboardResponse(TypedDict):
        dashboard_id: str
        message: str

    class DuplicateDashboardOptions(TypedDict):
        setup: Optional[Any]
        new_label: Optional[str]

    def duplicate(
        self,
        dashboardID: GenericID,
        dashboardObj: Optional[DuplicateDashboardOptions] = None,
    ) -> DuplicateDashboardResponse:
        """
        @description:
            Creates a copy of an existing dashboard.

        @see:
            https://docs.tago.io/docs/tagoio/dashboards/ Dashboard Overview

        @example:
            If receive an error "Authorization Denied", check policy **Dashboard** / **Duplicate** in Access Management.
            ```python
            resources = Resources()
            result = resources.dashboards.duplicate("dashboard-id-123", {"new_label": "Copy of My Dashboard"})
            print(result)  # {'dashboard_id': 'new-dashboard-id', 'message': 'Dashboard duplicated successfully'}
            ```
        """
        result = self.doRequest(
            {
                "path": f"/dashboard/{dashboardID}/duplicate",
                "method": "POST",
                "body": dashboardObj,
            }
        )

        return result

    def getPublicKey(self, dashboardID: GenericID, expireTime: ExpireTimeOption = "never") -> PublicKeyResponse:
        """
        @description:
            Generates a new public access token for the dashboard.

        @see:
            https://docs.tago.io/docs/tagoio/dashboards/ Dashboard Overview

        @example:
            If receive an error "Authorization Denied", check policy in Access Management.
            ```python
            resources = Resources()
            public_key = resources.dashboards.getPublicKey("dashboard-id-123", "1day")
            print(public_key)  # {'token': 'token-id-123', 'expire_time': '2025-01-02T00:00:00.000Z'}
            ```
        """
        result = self.doRequest(
            {
                "path": f"/dashboard/{dashboardID}/share/public",
                "method": "GET",
                "params": {
                    "expire_time": expireTime,
                },
            }
        )

        result = dateParser(result, ["expire_time"])

        return result

    def listDevicesRelated(self, dashboardID: GenericID) -> list[DevicesRelated]:
        """
        @description:
            Lists all devices associated with the dashboard.

        @see:
            https://docs.tago.io/docs/tagoio/dashboards/ Dashboard Overview

        @example:
            If receive an error "Authorization Denied", check policy **Dashboard** / **Related devices** in Access Management.
            ```python
            resources = Resources()
            devices = resources.dashboards.listDevicesRelated("dashboard-id-123")
            print(devices)  # [{'id': 'device-id-123'}, {'id': 'device-id-xyz'}, ...]
            ```
        """
        result = self.doRequest(
            {
                "path": f"/dashboard/{dashboardID}/devices",
                "method": "GET",
            }
        )

        return result

    def listAnalysisRelated(self, dashboardID: GenericID) -> list[AnalysisRelated]:
        """
        @description:
            Lists all analyses associated with a dashboard.

        @see:
            https://docs.tago.io/docs/tagoio/dashboards/ Dashboard Overview

        @example:
            If receive an error "Authorization Denied", check policy **Dashboard** / **Related analysis** in Access Management.
            ```python
            resources = Resources()
            analyses = resources.dashboards.listAnalysisRelated("dashboard-id-123")
            print(analyses)  # [{'id': 'analysis-id-123', 'name': 'Analysis #1'}, ...]
            ```
        """
        result = self.doRequest(
            {
                "path": f"/dashboard/{dashboardID}/analysis",
                "method": "GET",
            }
        )

        return result

    def runWidgetHeaderButtonAnalysis(
        self,
        analysisID: GenericID,
        dashboardID: GenericID,
        widgetID: GenericID,
        scope: Optional[Dict[str, Any]] = None,
    ) -> str:
        """
        @description:
            Executes an analysis from a widget's header button.

        @see:
            https://docs.tago.io/docs/tagoio/dashboards/ Dashboard Overview

        @example:
            ```python
            resources = Resources()
            result = resources.dashboards.runWidgetHeaderButtonAnalysis(
                "analysis-id-123",
                "dashboard-id-456",
                "widget-id-789",
                {"custom_data": "value"}
            )
            print(result)  # Analysis executed successfully
            ```
        """
        if scope is None:
            scope = {}
        result = self.doRequest(
            {
                "path": f"/analysis/{analysisID}/run/{dashboardID}/{widgetID}",
                "method": "POST",
                "body": {"scope": scope},
            }
        )

        return result

    def __init__(self, params):
        super().__init__(params)
        self.widgets = Widgets(params)
