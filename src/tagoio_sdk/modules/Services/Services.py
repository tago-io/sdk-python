import os
from typing import Optional
from tagoio_sdk.common.tagoio_module import GenericModuleParams, TagoIOModule
from tagoio_sdk.modules.Services.Attachment import Attachment
from tagoio_sdk.modules.Services.Console import ConsoleService
from tagoio_sdk.modules.Services.Email import Email
from tagoio_sdk.modules.Services.MQTT import MQTT
from tagoio_sdk.modules.Services.Notification import Notification
from tagoio_sdk.modules.Services.PDF import PDFService
from tagoio_sdk.modules.Services.SMS import SMS


class Services(TagoIOModule):
    def __init__(self, params: Optional[GenericModuleParams] = None):
        if params is None:
            params = {"token": os.environ.get("T_ANALYSIS_TOKEN")}
        super().__init__(params)
        self.sms = SMS(params)
        self.console = ConsoleService(params)
        self.email = Email(params)
        self.MQTT = MQTT(params)
        self.Notification = Notification(params)
        self.Attachment = Attachment(params)
        self.PDF = PDFService(params)
