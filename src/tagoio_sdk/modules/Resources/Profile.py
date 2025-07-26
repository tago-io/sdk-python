from typing import List
from typing import Optional

from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.Common_Type import Query
from tagoio_sdk.common.Common_Type import TokenDataList
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Resources.Profile_Type import ProfileInfo
from tagoio_sdk.modules.Resources.Profile_Type import ProfileListInfo
from tagoio_sdk.modules.Resources.Profile_Type import ProfileSummary
from tagoio_sdk.modules.Utils.dateParser import dateParser
from tagoio_sdk.modules.Utils.dateParser import dateParserList


class Profile(TagoIOModule):
    """
    Manage profiles in account be sure to use an
    account token with “write” permissions when
    using functions like create, edit and delete.
    """

    def info(self, profileID: GenericID) -> ProfileInfo:
        """
        Get Profile info
        :param: profileID Profile identification
        """
        result = self.doRequest(
            {
                "path": f"/profile/{profileID}",
                "method": "GET",
            }
        )

        if result.get("info"):
            result["info"] = dateParser(result["info"], ["created_at", "updated_at"])
        return result

    def list(self) -> list[ProfileListInfo]:
        """
        Lists all the profiles in your account
        """
        result = self.doRequest(
            {
                "path": "/profile",
                "method": "GET",
            }
        )
        return result

    def summary(self, profileID: GenericID) -> ProfileSummary:
        """
        Gets profile summary
        :param: profileID Profile identification
        """
        result = self.doRequest(
            {
                "path": f"/profile/{profileID}/summary",
                "method": "GET",
            }
        )
        return result

    def tokenList(
        self, profileID: GenericID, queryObj: Optional[Query] = None
    ) -> List[TokenDataList]:
        """
        Lists all the tokens in your account
        :param: profileID Profile identification
        """

        if queryObj is None:
            queryObj = {}
        if "orderBy" in queryObj:
            firstArgument = queryObj["orderBy"][0]
            secondArgument = queryObj["orderBy"][1]
            orderBy = f"{firstArgument},{secondArgument}"
        else:
            orderBy = "created_at, asc"

        result = self.doRequest(
            {
                "path": f"/profile/{profileID}/token",
                "method": "GET",
                "params": {
                    "page": queryObj.get("page") or 1,
                    "fields": queryObj.get("fields") or ["name", "token", "permission"],
                    "filter": queryObj.get("filter") or {},
                    "amount": queryObj.get("amount") or 20,
                    "orderBy": orderBy,
                },
            }
        )

        result = dateParserList(
            result, ["last_authorization", "expire_time", "created_at"]
        )

        return result
