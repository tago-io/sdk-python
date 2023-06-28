from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Resources.Account_Types import AccountInfo
from tagoio_sdk.modules.Utils.dateParser import dateParser


class Account(TagoIOModule):
    def info(self) -> AccountInfo:
        """
        Gets all account information.
        """

        result = self.doRequest(
            {
                "path": "/account",
                "method": "GET",
            }
        )
        result = dateParser(result, ["created_at", "updated_at", "last_login"])

        if result.get("options"):
            result["options"] = dateParser(result["options"], ["last_whats_new"])

        return result
