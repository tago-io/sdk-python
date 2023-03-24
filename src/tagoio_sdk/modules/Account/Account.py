from tagoio_sdk.common.tagoio_module import GenericModuleParams, TagoIOModule
from tagoio_sdk.modules.Account.Billing import Billing
from tagoio_sdk.modules.Account.Buckets import Buckets
from tagoio_sdk.modules.Account.Devices import Devices
from tagoio_sdk.modules.Account.Profile import Profile
from tagoio_sdk.modules.Account.Integration import Integration
from tagoio_sdk.modules.Account.Run import Run
from tagoio_sdk.modules.Utils.dateParser import dateParser
from tagoio_sdk.modules.Account.Account_Types import AccountInfo


class Account(TagoIOModule):
    def __init__(self, params: GenericModuleParams):
        super().__init__(params)
        self.billing = Billing(params)
        self.buckets = Buckets(params)
        self.profile = Profile(params)
        self.devices = Devices(params)
        self.integration = Integration(params)
        self.run = Run(params)

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
