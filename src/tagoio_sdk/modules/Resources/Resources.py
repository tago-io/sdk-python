import os

from typing import Optional

from tagoio_sdk.common.tagoio_module import GenericModuleParams
from tagoio_sdk.common.tagoio_module import TagoIOModule

from .Account import Account
from .Billing import Billing
from .Buckets import Buckets
from .Dashboards import Dashboards
from .Devices import Devices
from .Integration import Integration
from .Profile import Profile
from .Run import Run


class Resources(TagoIOModule):
    def __init__(self, params: Optional[GenericModuleParams] = None):
        if params is None:
            params = {"token": os.environ.get("T_ANALYSIS_TOKEN")}
        super().__init__(params)
        self.billing = Billing(params)
        self.buckets = Buckets(params)
        self.dashboards = Dashboards(params)
        self.devices = Devices(params)
        self.profile = Profile(params)
        self.run = Run(params)
        self.integration = Integration(params)
        self.account = Account(params)
