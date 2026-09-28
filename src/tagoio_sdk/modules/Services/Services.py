from typing import Optional

from tagoio_sdk.common.tagoio_module import GenericModuleParams
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Services.Attachment import Attachment
from tagoio_sdk.modules.Services.Console import ConsoleService
from tagoio_sdk.modules.Services.Email import Email
from tagoio_sdk.modules.Services.MQTT import MQTT
from tagoio_sdk.modules.Services.Notification import Notification
from tagoio_sdk.modules.Services.PDF import PDFService
from tagoio_sdk.modules.Services.SMS import SMS
from tagoio_sdk.params import get_params


class Services(TagoIOModule):
    def __init__(self, params: Optional[GenericModuleParams] = None):
        self.params = get_params(params)
        super().__init__(self.params)
        self.sms = SMS(self.params)
        self.console = ConsoleService(self.params)
        self.email = Email(self.params)
        self.MQTT = MQTT(self.params)
        self.Notification = Notification(self.params)
        self.Attachment = Attachment(self.params)
        self.PDF = PDFService(self.params)
