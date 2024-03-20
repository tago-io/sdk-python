from typing import Union

from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Utils.dateParser import dateParser


class Buckets(TagoIOModule):
    def info(self, bucketID: GenericID) -> str:
        """
        @deprecated Moved to Resources.devices.info(deviceID)
        Gets information about the bucket
        :param GenericID bucketID: Bucket ID
        """
        result = self.doRequest(
            {
                "path": f"/device/{bucketID}",
                "method": "GET",
            }
        )
        result = dateParser(result, ["created_at", "updated_at"])
        return result

    def amount(self, bucketID: GenericID) -> Union[int, float]:
        """
        @deprecated Moved to Resources.devices.amount(deviceID)
        Get Amount of data on the Bucket
        :param GenericID bucketID: Bucket ID
        """
        result = self.doRequest(
            {
                "path": f"/device/{bucketID}/data_amount",
                "method": "GET",
            }
        )
        return result
