from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.Common_Type import Query
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Resources.IntegrationNetworkType import NetworkInfo


class Networks(TagoIOModule):
    def listNetwork(self, queryObj: Query = None) -> list[NetworkInfo]:
        """
        Retrieves a list with all networks from the account

        :default:
            fields: ["id", "name"]

        :param fields Fields to be returned
        """

        if queryObj is None:
            queryObj = {}
        if "orderBy" in queryObj:
            firstArgument = queryObj["orderBy"][0]
            secondArgument = queryObj["orderBy"][1]
            orderBy = f"{firstArgument},{secondArgument}"
        else:
            orderBy = "name,asc"

        result = self.doRequest(
            {
                "path": "/integration/network",
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

        return result

    def info(self, networkID: GenericID, fields: NetworkInfo = None) -> NetworkInfo:
        """
        Retrieves the information of the network.

        :default:
            fields: ["id", "name"]

        :param networkID Network ID
        :param fields    Fields to be returned
        """

        if fields is None:
            fields = ["id", "name"]
        result = self.doRequest(
            {
                "path": f"/integration/network/{networkID}",
                "method": "GET",
                "params": {
                    "fields": fields,
                },
            }
        )

        return result
