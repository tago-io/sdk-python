import os
from typing import Optional

from tagoio_sdk.common.tagoio_module import TagoIOModule, GenericModuleParams
from .Access import Access
from .Actions import Actions
from .Analyses import Analyses
from .Billing import Billing
from .Buckets import Buckets
from .Dashboards import Dashboards
from .Dictionaries import Dictionaries
from .Devices import Devices
from .Profile import Profile
from .Run import Run
from .Integration import Integration
from .Account import Account


class Resources(TagoIOModule):
    def __init__(self, params: Optional[GenericModuleParams] = None):
        if params is None:
            params = {"token": os.environ.get("T_ANALYSIS_TOKEN")}
        super().__init__(params)
        self.access = Access(params)
        self.actions = Actions(params)
        self.analysis = Analyses(params)
        self.billing = Billing(params)
        self.buckets = Buckets(params)
        self.dashboards = Dashboards(params)
        self.dictionaries = Dictionaries(params)
        self.devices = Devices(params)
        self.profile = Profile(params)
        self.run = Run(params)
        self.integration = Integration(params)
        self.account = Account(params)
