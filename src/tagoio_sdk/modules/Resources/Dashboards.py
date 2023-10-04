from typing import Optional, TypedDict

from tagoio_sdk.common.Common_Type import ExpireTimeOption, GenericID, Query
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Resources.Dashboards_Type import (
    AnalysisRelated,
    DashboardCreateInfo,
    DashboardInfo,
    DevicesRelated,
    PublicKeyResponse,
)
from tagoio_sdk.modules.Utils.dateParser import dateParser, dateParserList


class Dashboards(TagoIOModule):
    def listDashboard(self, queryObj: Query = {}) -> list[DashboardInfo]:
        """
        Retrieves a list with all dashboards from the account

        :default:

            queryObj: {
                "page": 1,
                "fields": ["id", "name"],
                "filter": {},
                "amount": 20,
                "orderBy": "label,asc",
            }

        :param queryObj Search query params
        """

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

    class dashboard(TypedDict):
        dashboard: GenericID

    def create(self, dashboardObj: DashboardCreateInfo) -> dashboard:
        """
        Create dashboard

        :param dashboardObj Dashboard object
        """
        result = self.doRequest(
            {
                "path": "/dashboard",
                "method": "POST",
                "body": dashboardObj,
            }
        )

        return result

    def edit(self, dashboardID: GenericID, dashboardObj: DashboardInfo) -> str:
        """
        Modify any property of the dashboards

        :param dashboardID Dashboard identification
        :param dashboardObj Dashboard Object with data to be replaced
        """
        result = self.doRequest(
            {
                "path": f"/dashboard/{dashboardID}",
                "method": "PUT",
                "body": {
                    dashboardObj,
                },
            }
        )

        return result

    def delete(self, dashboardID: GenericID) -> str:
        """
        Deletes an dashboard from the account

        :param dashboardID Dashboard identification
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
        Gets information about the dashboard

        :param dashboardID Dashboard identification
        """
        result = self.doRequest(
            {
                "path": f"/dashboard/{dashboardID}",
                "method": "GET",
            }
        )

        result = dateParser(result, ["created_at", "updated_at", "last_access"])
        return result

    class duplicate(TypedDict):
        dashboard_id: str
        message: str

    class dashboardObj(TypedDict):
        setup: Optional[any]
        new_label: Optional[str]

    def duplicate(
        self, dashboardID: GenericID, dashboardObj: Optional[dashboardObj] = None
    ) -> duplicate:
        """
        Duplicate the dashboard to your own account

        :param dashboardID Dashboard identification
        :param dashboardObj Object with data of the duplicate dashboard
        """
        result = self.doRequest(
            {
                "path": f"/dashboard/{dashboardID}/duplicate",
                "method": "POST",
                "body": dashboardObj,
            }
        )

        return result

    def getPublicKey(
        self, dashboardID: GenericID, expireTime: ExpireTimeOption = "never"
    ) -> PublicKeyResponse:
        """
        Generate a new public token for the dashboard

        :param dashboardID Dashboard identification
        :param expireTime Time when token will expire
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
        Get list of devices related with dashboard

        :param dashboardID Dashboard identification
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
        Get list of analysis related with a dashboard

        :param dashboardID Dashboard identification
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
        scope: Optional[any] = {},
    ) -> str:
        """
        Runs an analysis located in a widget's header button

        :param analysisID The id of the analysis to run
        :param dashboardID The id of the dashboard that contains the widget
        :param widgetID The id of the widget that contains the header button
        :param scope Data to send to the analysis
        """
        result = self.doRequest(
            {
                "path": f"/analysis/{analysisID}/run/{dashboardID}/{widgetID}",
                "method": "POST",
                "body": scope,
            }
        )

        return result
