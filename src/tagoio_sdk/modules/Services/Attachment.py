from typing import TypedDict

from tagoio_sdk.common.Common_Type import Base64
from tagoio_sdk.common.tagoio_module import TagoIOModule


class ArchiveFile(TypedDict):
    name: str
    content: Base64
    type: str


class Attachment(TagoIOModule):
    def upload(self, archive: ArchiveFile) -> str:
        """
        Send Attachment

        :param ArchiveFile archive: Archive JSON Object
        """
        result = self.doRequest(
            {
                "path": "/analysis/services/attachment/upload",
                "method": "POST",
                "body": {
                    "archive": archive["content"],
                    "filename": archive["name"],
                    "type": archive["type"],
                },
            }
        )
        return result
