from typing import Any
from typing import Dict
from typing import List
from typing import Literal
from typing import Optional

from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.Common_Type import GenericToken
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Resources.Analysis_Types import AnalysisCreateInfo
from tagoio_sdk.modules.Resources.Analysis_Types import AnalysisInfo
from tagoio_sdk.modules.Resources.Analysis_Types import AnalysisListItem
from tagoio_sdk.modules.Resources.Analysis_Types import AnalysisQuery
from tagoio_sdk.modules.Resources.Analysis_Types import ScriptFile
from tagoio_sdk.modules.Utils.dateParser import dateParser
from tagoio_sdk.modules.Utils.dateParser import dateParserList


class Analyses(TagoIOModule):
    def list(self, queryObj: Optional[AnalysisQuery] = None) -> List[AnalysisListItem]:
        """
        Retrieves a list with all analyses from the account

        :default:

            queryObj: {
                "page": 1,
                "fields": ["id", "name"],
                "filter": {},
                "amount": 20,
                "orderBy": ["name", "asc"],
            }

        :param AnalysisQuery queryObj: Search query params
        """
        queryObj = queryObj or {}
        orderBy = f"{queryObj.get('orderBy', ['name', 'asc'])[0]},{queryObj.get('orderBy', ['name', 'asc'])[1]}"

        result = self.doRequest(
            {
                "path": "/analysis/",
                "method": "GET",
                "params": {
                    "page": queryObj.get("page", 1),
                    "fields": queryObj.get("fields", ["id", "name"]),
                    "filter": queryObj.get("filter", {}),
                    "amount": queryObj.get("amount", 20),
                    "orderBy": orderBy,
                },
            }
        )

        result = dateParserList(result, ["created_at", "updated_at", "last_run"])
        return result

    def create(self, analysisObj: AnalysisCreateInfo) -> Dict[str, GenericID | GenericToken]:
        """
        Create a new analyze

        :param AnalysisCreateInfo analysisObj: Data object to create new TagoIO Analyze
        """
        result = self.doRequest(
            {
                "path": "/analysis",
                "method": "POST",
                "body": analysisObj,
            }
        )
        return result

    def edit(self, analysisID: GenericID, analysisObj: AnalysisInfo) -> str:
        """
        Modify any property of the analyze

        :param GenericID analysisID: Analyze identification
        :param Partial[AnalysisInfo] analysisObj: Analyze Object with data to replace
        """
        result = self.doRequest(
            {
                "path": f"/analysis/{analysisID}",
                "method": "PUT",
                "body": analysisObj,
            }
        )
        return result

    def delete(self, analysisID: GenericID) -> str:
        """
        Deletes an analyze from the account

        :param GenericID analysisID: Analyze identification
        """
        result = self.doRequest(
            {
                "path": f"/analysis/{analysisID}",
                "method": "DELETE",
            }
        )
        return result

    def info(self, analysisID: GenericID) -> AnalysisInfo:
        """
        Gets information about the analyze

        :param GenericID analysisID: Analyze identification
        """
        result = self.doRequest(
            {
                "path": f"/analysis/{analysisID}",
                "method": "GET",
            }
        )
        result = dateParser(result, ["created_at", "updated_at", "last_run"])
        return result

    def run(self, analysisID: GenericID, scopeObj: Optional[Dict[str, Any]] = None) -> Dict[str, GenericToken]:
        """
        Force analyze to run

        :param GenericID analysisID: Analyze identification
        :param Optional[Dict[str, Any]] scopeObj: Simulate scope for analysis
        """
        result = self.doRequest(
            {
                "path": f"/analysis/{analysisID}/run",
                "method": "POST",
                "body": {"scope": scopeObj},
            }
        )
        return result

    def tokenGenerate(self, analysisID: GenericID) -> Dict[str, str]:
        """
        Generate a new token for the analysis

        :param GenericID analysisID: Analyze identification
        """
        result = self.doRequest(
            {
                "path": f"/analysis/{analysisID}/token",
                "method": "GET",
            }
        )
        return result

    def uploadScript(self, analysisID: GenericID, fileObj: ScriptFile) -> str:
        """
        Upload a file (base64) to Analysis. Automatically erase the old one

        :param GenericID analysisID: Analyze identification
        :param ScriptFile fileObj: Object with name, language and content of the file
        """
        result = self.doRequest(
            {
                "path": f"/analysis/{analysisID}/upload",
                "method": "POST",
                "body": {
                    "file": fileObj.get("content"),
                    "file_name": fileObj.get("name"),
                    "language": fileObj.get("language"),
                },
            }
        )
        return result

    def downloadScript(self, analysisID: GenericID, options: Optional[Dict[Literal["version"], int]] = None) -> Dict:
        """
        Get a url to download the analysis. If `version` is specified in `options`, downloads a specific version.

        :param GenericID analysisID: Analysis identification
        :param Optional[Dict[str, int]] options: Options for the Analysis script to download
        """
        version = options.get("version") if options else None

        result = self.doRequest(
            {
                "path": f"/analysis/{analysisID}/download",
                "method": "GET",
                "params": {"version": version} if version else {},
            }
        )
        result = dateParser(result, ["expire_at"])
        return result
