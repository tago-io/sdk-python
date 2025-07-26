import os

from typing import Optional

from tagoio_sdk.common.tagoio_module import GenericModuleParams
from tagoio_sdk.common.tagoio_module import TagoIOModule

from .Access import Access
from .Account import Account
from .Actions import Actions
from .Analyses import Analyses
from .Billing import Billing
from .Buckets import Buckets
from .Dashboards import Dashboards
from .Devices import Devices
from .Dictionaries import Dictionaries
from .Files import Files
from .Integration import Integration
from .Notifications import Notifications
from .Profile import Profile
from .Run import Run
from .Secrets import Secrets
from .Service_Authorization import ServiceAuthorization


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
        self.files = Files(params)
        self.notifications = Notifications(params)
        self.profile = Profile(params)
        self.run = Run(params)
        self.secrets = Secrets(params)
        self.serviceAuthorization = ServiceAuthorization(params)
        self.integration = Integration(params)
        self.account = Account(params)
