from tagoio_sdk.common.tagoio_module import GenericModuleParams
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Resources.IntegrationConnector import Connectors
from tagoio_sdk.modules.Resources.IntegrationNetwork import Networks


class Integration(TagoIOModule):
    def __init__(self, params: GenericModuleParams):
        self.networks = Networks(params)
        self.connectors = Connectors(params)
