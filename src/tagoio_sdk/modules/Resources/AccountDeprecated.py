from tagoio_sdk.common.tagoio_module import GenericModuleParams

from .Account import Account
from .Billing import Billing
from .Buckets import Buckets
from .Dashboards import Dashboards
from .Devices import Devices
from .Integration import Integration
from .Profile import Profile
from .Run import Run


class AccountDeprecated(Account):
    """
    @internal
    @deprecated Moved to Resources.
    * Resources().account.info() Relies on Access Manage Permissions
    * Resources(token="TOKEN").account.info() Relies on Analysis/Profile Token
    """

    def __init__(self, params: GenericModuleParams):
        self.buckets = Buckets(params)
        """@deprecated moved to Resources().buckets"""
        self.dashboards = Dashboards(params)
        """@deprecated moved to Resources().dashboards"""
        self.devices = Devices(params)
        """@deprecated moved to Resources().devices"""
        self.billing = Billing(params)
        """@deprecated moved to Resources().billing"""
        self.integration = Integration(params)
        """@deprecated moved to Resources().integration"""
        self.run = Run(params)
        """@deprecated moved to Resources().run"""
        self.profiles = Profile(params)
        """@deprecated moved to Resources().profiles"""
