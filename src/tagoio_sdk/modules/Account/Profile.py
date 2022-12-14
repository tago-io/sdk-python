from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Account.Profile_Type import (
    ProfileInfo,
    ProfileListInfo,
    ProfileSummary,
)
from tagoio_sdk.modules.Utils.dateParser import dateParser


class Profile(TagoIOModule):
    """
    Manage profiles in account be sure to use an
    account token with “write” permissions when
    using functions like create, edit and delete.
    """
    def info(self, profileID: GenericID) -> list[ProfileInfo]:
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

        if result.info:
            result.info = dateParser(result.info, ["created_at", "updated_at"])
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
