from tagoio_sdk.common.tagoio_module import GenericModuleParams, TagoIOModule
from tagoio_sdk.modules.Resources.IntegrationNetwork import Networks


class Integration(TagoIOModule):
    def __init__(self, params: GenericModuleParams):
        self.networks = Networks(params)
