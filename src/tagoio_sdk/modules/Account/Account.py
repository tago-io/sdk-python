from tagoio_sdk.common.tagoio_module import GenericModuleParams, TagoIOModule
from tagoio_sdk.modules.Account.Billing import Billing
from tagoio_sdk.modules.Account.Buckets import Buckets
from tagoio_sdk.modules.Account.Devices import Devices
from tagoio_sdk.modules.Account.Profile import Profile
from tagoio_sdk.modules.Account.Run import Run


class Account(TagoIOModule):
    def __init__(self, params: GenericModuleParams):
        self.billing = Billing(params)
        self.buckets = Buckets(params)
        self.profile = Profile(params)
        self.devices = Devices(params)
        self.run = Run(params)
