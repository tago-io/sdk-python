from tagoio_sdk.common.tagoio_module import GenericModuleParams

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


class AccountDeprecated(Account):
    """
    @internal
    @deprecated Moved to Resources.
    * Resources().account.info() Relies on Access Manage Permissions
    * Resources(token="TOKEN").account.info() Relies on Analysis/Profile Token
    """

    def __init__(self, params: GenericModuleParams):
        self.access = Access(params)
        """@deprecated moved to Resources().access"""
        self.actions = Actions(params)
        """@deprecated moved to Resources().actions"""
        self.analysis = Analyses(params)
        """@deprecated moved to Resources().analysis"""
        self.buckets = Buckets(params)
        """@deprecated moved to Resources().buckets"""
        self.dashboards = Dashboards(params)
        """@deprecated moved to Resources().dashboards"""
        self.dictionaries = Dictionaries(params)
        """@deprecated moved to Resources().dictionaries"""
        self.devices = Devices(params)
        """@deprecated moved to Resources().devices"""
        self.files = Files(params)
        """@deprecated moved to Resources().files"""
        self.notifications = Notifications(params)
        """@deprecated moved to Resources().notifications"""
        self.billing = Billing(params)
        """@deprecated moved to Resources().billing"""
        self.integration = Integration(params)
        """@deprecated moved to Resources().integration"""
        self.run = Run(params)
        """@deprecated moved to Resources().run"""
        self.profiles = Profile(params)
        """@deprecated moved to Resources().profiles"""
        self.secrets = Secrets(params)
        """@deprecated moved to Resources().secrets"""
        self.serviceAuthorization = ServiceAuthorization(params)
        """@deprecated moved to Resources().secrets"""
