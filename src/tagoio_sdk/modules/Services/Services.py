from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Services.Attachment import Attachment
from tagoio_sdk.modules.Services.Console import ConsoleService
from tagoio_sdk.modules.Services.Email import Email
from tagoio_sdk.modules.Services.MQTT import MQTT
from tagoio_sdk.modules.Services.Notification import Notification
from tagoio_sdk.modules.Services.PDF import PDFService
from tagoio_sdk.modules.Services.SMS import SMS


class Services(TagoIOModule):

    console = ConsoleService()

    sms = SMS()

    email = Email()

    MQTT = MQTT()

    Notification = Notification()

    Attachment = Attachment()

    PDF = PDFService()
