from tagoio_sdk.common.tagoio_module import GenericModuleParams, TagoIOModule
from tagoio_sdk.modules.Account.Billing import Billing
from tagoio_sdk.modules.Account.Buckets import Buckets
from tagoio_sdk.modules.Account.Profile import Profile


class Account(TagoIOModule):
    def __init__(self, params: GenericModuleParams):
        self.sms = Billing(params)
        self.console = Buckets(params)
        self.email = Profile(params)
