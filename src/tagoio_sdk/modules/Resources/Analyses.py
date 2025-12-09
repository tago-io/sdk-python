from typing import Any
from typing import Dict
from typing import List
from typing import Literal
from typing import Optional

import requests

from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.Common_Type import GenericToken
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Resources.Analysis_Types import AnalysisCreateInfo
from tagoio_sdk.modules.Resources.Analysis_Types import AnalysisInfo
from tagoio_sdk.modules.Resources.Analysis_Types import AnalysisListItem
from tagoio_sdk.modules.Resources.Analysis_Types import AnalysisQuery
from tagoio_sdk.modules.Resources.Analysis_Types import ScriptFile
from tagoio_sdk.modules.Resources.Analysis_Types import SnippetRuntime
from tagoio_sdk.modules.Resources.Analysis_Types import SnippetsListResponse
from tagoio_sdk.modules.Utils.dateParser import dateParser
from tagoio_sdk.modules.Utils.dateParser import dateParserList


# Base URL for TagoIO analysis snippets repository
SNIPPETS_BASE_URL = "https://snippets.tago.io"


class Analyses(TagoIOModule):
    def list(self, queryObj: Optional[AnalysisQuery] = None) -> List[AnalysisListItem]:
        """
        @description:
            Lists all analyses from the application with pagination support.
            Use this to retrieve and manage analyses in your application.

        @see:
            https://docs.tago.io/docs/tagoio/analysis/ Analysis

        @example:
            If receive an error "Authorization Denied", check policy **Analysis** / **Access** in Access Management.
            ```python
            resources = Resources()
            list_result = resources.analyses.list({
                "page": 1,
                "fields": ["id", "name"],
                "amount": 10,
                "orderBy": ["name", "asc"]
            })
            print(list_result)  # [{'id': 'analysis-id-123', 'name': 'Analysis Test', ...}]
            ```

        :param AnalysisQuery queryObj: Search query params (optional)
        :return: List of analysis items matching the query
        :rtype: List[AnalysisListItem]
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
        @description:
            Creates a new analysis in your application.

        @see:
            https://help.tago.io/portal/en/kb/articles/120-creating-analysis Creating Analysis

        @example:
            If receive an error "Authorization Denied", check policy **Analysis** / **Create** in Access Management.
            ```python
            resources = Resources()
            new_analysis = resources.analyses.create({
                "name": "My Analysis",
                "runtime": "python",
                "tags": [{"key": "type", "value": "data-processing"}]
            })
            print(new_analysis["id"], new_analysis["token"])  # analysis-id-123, analysis-token-123
            ```

        :param AnalysisCreateInfo analysisObj: Data object to create new TagoIO Analysis
        :return: Dictionary with the new analysis ID and token
        :rtype: Dict[str, GenericID | GenericToken]
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
        @description:
            Modifies an existing analysis.

        @see:
            https://docs.tago.io/docs/tagoio/analysis/ Analysis

        @example:
            If receive an error "Authorization Denied", check policy **Analysis** / **Create** in Access Management.
            ```python
            resources = Resources()
            result = resources.analyses.edit("analysis-id-123", {
                "name": "Updated Analysis",
                "active": False
            })
            print(result)  # Successfully Updated
            ```

        :param GenericID analysisID: Analysis identification
        :param AnalysisInfo analysisObj: Analysis object with data to replace
        :return: Success message
        :rtype: str
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
        @description:
            Deletes an analysis from your application.

        @see:
            https://docs.tago.io/docs/tagoio/analysis/ Analysis

        @example:
            If receive an error "Authorization Denied", check policy **Analysis** / **Delete** in Access Management.
            ```python
            resources = Resources()
            result = resources.analyses.delete("analysis-id-123")
            print(result)  # Successfully Removed
            ```

        :param GenericID analysisID: Analysis identification
        :return: Success message
        :rtype: str
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
        @description:
            Retrieves detailed information about a specific analysis.

        @see:
            https://docs.tago.io/docs/tagoio/analysis/ Analysis

        @example:
            If receive an error "Authorization Denied", check policy **Analysis** / **Access** in Access Management.
            ```python
            resources = Resources()
            analysis_info = resources.analyses.info("analysis-id-123")
            print(analysis_info)  # {'id': 'analysis-id-123', 'name': 'My Analysis', ...}
            ```

        :param GenericID analysisID: Analysis identification
        :return: Detailed analysis information
        :rtype: AnalysisInfo
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
        @description:
            Executes an analysis with optional scope parameters.

        @see:
            https://docs.tago.io/docs/tagoio/analysis/ Analysis

        @example:
            If receive an error "Authorization Denied", check policy **Analysis** / **Run Analysis** in Access Management.
            ```python
            resources = Resources()
            result = resources.analyses.run("analysis-id-123", {"environment": "production"})
            print(result["analysis_token"])  # analysis-token-123
            ```

        :param GenericID analysisID: Analysis identification
        :param Optional[Dict[str, Any]] scopeObj: Simulate scope for analysis
        :return: Dictionary containing the analysis token
        :rtype: Dict[str, GenericToken]
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
        @description:
            Generates a new token for the analysis.
            This is only allowed when the analysis is running in external mode.

        @see:
            https://docs.tago.io/docs/tagoio/analysis/ Analysis

        @example:
            ```python
            resources = Resources()
            token = resources.analyses.tokenGenerate("analysis-id-123")
            print(token["analysis_token"])  # analysis-token-123
            ```

        :param GenericID analysisID: Analysis identification
        :return: Dictionary containing the new analysis token
        :rtype: Dict[str, str]
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
        @description:
            Uploads a script file to an analysis.
            The file content must be base64-encoded. This automatically replaces the old script.

        @see:
            https://docs.tago.io/docs/tagoio/analysis/ Analysis

        @example:
            If receive an error "Authorization Denied", check policy **Analysis** / **Upload Analysis Script** in Access Management.
            ```python
            resources = Resources()
            result = resources.analyses.uploadScript("analysis-id-123", {
                "name": "script.py",
                "content": "base64-encoded-content",
                "language": "python"
            })
            print(result)  # Successfully Uploaded
            ```

        :param GenericID analysisID: Analysis identification
        :param ScriptFile fileObj: Object with name, language and content (base64) of the file
        :return: Success message
        :rtype: str
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

    def downloadScript(
        self,
        analysisID: GenericID,
        options: Optional[Dict[Literal["version"], int]] = None,
    ) -> Dict:
        """
        @description:
            Gets a download URL for the analysis script.
            If version is specified in options, downloads a specific version.

        @see:
            https://docs.tago.io/docs/tagoio/analysis/ Analysis

        @example:
            If receive an error "Authorization Denied", check policy **Analysis** / **Download Analysis Script** in Access Management.
            ```python
            resources = Resources()
            download = resources.analyses.downloadScript("analysis-id-123", {"version": 1})
            print(download["url"])  # https://...
            print(download["expire_at"])  # 2025-01-13T...
            ```

        :param GenericID analysisID: Analysis identification
        :param Optional[Dict[str, int]] options: Options for the Analysis script to download (e.g., {"version": 1})
        :return: Dictionary with download URL, size information, and expiration date
        :rtype: Dict
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

    def listSnippets(self, runtime: SnippetRuntime) -> SnippetsListResponse:
        """
        @description:
            Get all available snippets for a specific runtime environment.
            Fetches analysis code snippets from the public TagoIO snippets repository.

        @see:
            https://help.tago.io/portal/en/kb/articles/64-script-examples Script Examples
            https://help.tago.io/portal/en/kb/articles/104-script-editor Script Editor

        @example:
            ```python
            resources = Resources()
            python_snippets = resources.analyses.listSnippets("python-rt2025")

            # Print all snippet titles
            for snippet in python_snippets["snippets"]:
                print(f"{snippet['title']}: {snippet['description']}")
            ```

        :param SnippetRuntime runtime: The runtime environment to get snippets for
        :return: Snippets metadata including runtime, schema version, and list of available snippets
        :rtype: SnippetsListResponse
        """
        url = f"{SNIPPETS_BASE_URL}/{runtime}.json"

        try:
            response = requests.get(url, headers={"Accept": "*/*"}, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to fetch snippets: {e}") from e

    def getSnippetFile(self, runtime: SnippetRuntime, filename: str) -> str:
        """
        @description:
            Get the raw source code content of a specific snippet file.
            Fetches the actual code content from the TagoIO snippets repository.

        @see:
            https://help.tago.io/portal/en/kb/articles/64-script-examples Script Examples
            https://help.tago.io/portal/en/kb/articles/104-script-editor Script Editor

        @example:
            ```python
            resources = Resources()

            # Get TypeScript code for console example
            code = resources.analyses.getSnippetFile("deno-rt2025", "console.ts")
            print(code)

            # Get Python code for data processing
            python_code = resources.analyses.getSnippetFile("python-rt2025", "avg-min-max.py")
            print(python_code)
            ```

        :param SnippetRuntime runtime: The runtime environment the snippet belongs to
        :param str filename: The filename of the snippet to retrieve
        :return: Raw file content as string
        :rtype: str
        """
        url = f"{SNIPPETS_BASE_URL}/{runtime}/{filename}"

        try:
            response = requests.get(url, headers={"Accept": "*/*"}, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to fetch snippet file: {e}") from e
