import warnings

from typing import Any
from typing import Optional
from typing import TypedDict
from typing import Union

from tagoio_sdk.common.tagoio_module import TagoIOModule


class AttachmentOptions(TypedDict):
    archive: str
    """
    Archive itself
    """
    filename: str
    """
    Name for the archive
    """


class TemplateOptions(TypedDict):
    name: str
    """
    Template name

    You can create an e-mail template on TagoRUN options at https://admin.tago.io/run
    """
    params: Optional[dict[str, Union[int, float]]]
    """
    Parameters to parse on Template

    You can use that parameter as local variable using $PARAMETER_KEY$

    :example: params = { name: 'John' }

    will be $name$ on template document
    """


class EmailBase(TypedDict):
    to: str
    """
    E-mail address to be sent

    :example: "myclien@tago.io"
    """
    from_name: Optional[str]
    """
    Name of origin

    :example: "My Run"
    """
    subject: str
    """
    Subject of the e-mail

    only allow with message or html
    """
    attachment: Optional[AttachmentOptions]
    """
    Attachment for the e-mail
    """


class EmailRawText(TypedDict):
    message: str
    """
    Message in raw text for email body
    """


class EmailHTML(TypedDict):
    html: str
    """
    HTML email body
    """


class EmailWithTemplate(TypedDict):
    to: str
    """
    E-mail address to be sent

    :example: "myclien@tago.io"
    """
    from_name: Optional[str]
    """
    Name of origin

    :example: "My Run"
    """
    attachment: Optional[AttachmentOptions]
    """
    Attachment for the e-mail
    """
    template: Optional[TemplateOptions]
    """
    Use TagoRUN E-Mail Template

    Tip: If you use template together with attachment the
    back-end will generate a parameter called 'URL';
    """


EmailWithHTML = Union[EmailBase, EmailHTML]
EmailWithRawText = Union[EmailBase, EmailRawText]


class Email(TagoIOModule):
    def send(
        self, email: Union[Any, EmailWithRawText, EmailWithHTML, EmailWithTemplate]
    ) -> str:
        if email.get("html") and email.get("message"):
            warnings.warn("HTML field will overwrite message field", stacklevel=2)

        result = self.doRequest(
            {
                "path": "/analysis/services/email/send",
                "method": "POST",
                "body": email,
            }
        )
        return result
