from typing import Union

from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Utils.dateParser import dateParser


class Buckets(TagoIOModule):
    def info(self, bucketID: GenericID) -> str:
        """
        Gets information about the bucket
        :param GenericID bucketID: Bucket ID
        """
        result = self.doRequest(
            {
                "path": f"/bucket/{bucketID}",
                "method": "GET",
            }
        )
        result = dateParser(result, ["created_at", "updated_at"])
        return result

    def amount(self, bucketID: GenericID) -> Union[int, float]:
        """
        Get Amount of data on the Bucket
        :param GenericID bucketID: Bucket ID
        """
        result = self.doRequest(
            {
                "path": f"/bucket/{bucketID}/data_amount",
                "method": "GET",
            }
        )
        return result
