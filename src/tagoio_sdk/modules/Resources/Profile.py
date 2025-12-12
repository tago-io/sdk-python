from typing import Dict
from typing import List
from typing import Optional

from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.Common_Type import GenericToken
from tagoio_sdk.common.Common_Type import Query
from tagoio_sdk.common.Common_Type import TokenCreateResponse
from tagoio_sdk.common.Common_Type import TokenData
from tagoio_sdk.common.Common_Type import TokenDataList
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Resources.Profile_Type import AuditLog
from tagoio_sdk.modules.Resources.Profile_Type import AuditLogFilter
from tagoio_sdk.modules.Resources.Profile_Type import ProfileCreateInfo
from tagoio_sdk.modules.Resources.Profile_Type import ProfileCredentials
from tagoio_sdk.modules.Resources.Profile_Type import ProfileInfo
from tagoio_sdk.modules.Resources.Profile_Type import ProfileListInfo
from tagoio_sdk.modules.Resources.Profile_Type import ProfileSummary
from tagoio_sdk.modules.Resources.Profile_Type import ProfileTeam
from tagoio_sdk.modules.Resources.Profile_Type import StatisticsDate
from tagoio_sdk.modules.Resources.Profile_Type import UsageStatistic
from tagoio_sdk.modules.Utils.dateParser import dateParser
from tagoio_sdk.modules.Utils.dateParser import dateParserList


class Profile(TagoIOModule):
    def info(self, profileID: GenericID) -> ProfileInfo:
        """
        @description:
            Retrieves detailed information about a specific profile using its ID or 'current' for the active profile.

        @see:
            https://help.tago.io/portal/en/kb/articles/198-profiles Profiles

        @example:
            If receive an error "Authorization Denied", check policy **Account** / **Access profile** in Access Management.
            ```python
            resources = Resources()
            profile_info = resources.profile.info("profile-id-123")
            # Or get current profile
            current_profile = resources.profile.info("current")
            print(profile_info)  # {'info': {'id': 'profile-id-123', 'account': 'account-id-123', ...}, ...}
            ```
        """
        result = self.doRequest(
            {
                "path": f"/profile/{profileID}",
                "method": "GET",
            }
        )

        if result.get("info"):
            result["info"] = dateParser(result["info"], ["created_at", "updated_at"])
        return result

    def list(self) -> list[ProfileListInfo]:
        """
        @description:
            Retrieves a list of all profiles associated with the current account.

        @see:
            https://help.tago.io/portal/en/kb/articles/198-profiles Profiles

        @example:
            If receive an error "Authorization Denied", check policy **Account** / **Access profile** in Access Management.
            ```python
            resources = Resources()
            result = resources.profile.list()
            print(result)  # [{'id': 'profile-id-123', 'name': 'Profile Test', ...}]
            ```
        """
        result = self.doRequest(
            {
                "path": "/profile",
                "method": "GET",
            }
        )
        return result

    def summary(self, profileID: GenericID) -> ProfileSummary:
        """
        @description:
            Retrieves a summary of the profile's usage and statistics.

        @see:
            https://help.tago.io/portal/en/kb/articles/198-profiles Profiles

        @example:
            If receive an error "Authorization Denied", check policy **Account** / **Access profile** in Access Management.
            ```python
            resources = Resources()
            result = resources.profile.summary("profile-id-123")
            print(result)  # {'amount': {'device': 10, 'bucket': 10, 'dashboard': 5, ...}, ...}
            ```
        """
        result = self.doRequest(
            {
                "path": f"/profile/{profileID}/summary",
                "method": "GET",
            }
        )
        return result

    def tokenList(self, profileID: GenericID, queryObj: Optional[Query] = None) -> List[TokenDataList]:
        """
        @description:
            Retrieves a list of all tokens associated with a specific profile.

        @see:
            https://help.tago.io/portal/en/kb/articles/495-account-token Account Token

        @example:
            ```python
            resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
            result = resources.profile.tokenList("profile-id-123", {
                "page": 1,
                "amount": 20,
                "fields": ["name", "token", "permission"]
            })
            print(result)  # [{'name': 'Token #1', 'token': 'token-value', 'permission': 'full', ...}, ...]
            ```
        """

        if queryObj is None:
            queryObj = {}
        if "orderBy" in queryObj:
            firstArgument = queryObj["orderBy"][0]
            secondArgument = queryObj["orderBy"][1]
            orderBy = f"{firstArgument},{secondArgument}"
        else:
            orderBy = "created_at, asc"

        result = self.doRequest(
            {
                "path": f"/profile/{profileID}/token",
                "method": "GET",
                "params": {
                    "page": queryObj.get("page") or 1,
                    "fields": queryObj.get("fields") or ["name", "token", "permission"],
                    "filter": queryObj.get("filter") or {},
                    "amount": queryObj.get("amount") or 20,
                    "orderBy": orderBy,
                },
            }
        )

        result = dateParserList(result, ["last_authorization", "expire_time", "created_at"])

        return result

    def create(self, profileObj: ProfileCreateInfo, allocate_free_resources: bool = False) -> Dict[str, GenericID]:
        """
        @description:
            Creates a new profile with the specified name and optional resource allocation settings.

        @see:
            https://help.tago.io/portal/en/kb/articles/198-profiles Profiles

        @example:
            ```python
            resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
            result = resources.profiles.create({"name": "New Profile"}, allocate_free_resources=True)
            print(result)  # {'id': 'profile-id-123'}
            ```
        """
        params = {}
        if allocate_free_resources:
            params["allocate_free_resources"] = allocate_free_resources

        result = self.doRequest({"path": "/profile/", "method": "POST", "body": profileObj, "params": params})

        return result

    def edit(self, profileID: GenericID, profileObj: Dict) -> str:
        """
        @description:
            Updates profile information with the provided data.

        @see:
            https://help.tago.io/portal/en/kb/articles/198-profiles Profiles

        @example:
            ```python
            resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
            result = resources.profiles.edit("profile-id-123", {"name": "Updated Profile Name"})
            print(result)  # Successfully Updated
            ```
        """
        result = self.doRequest({"path": f"/profile/{profileID}", "method": "PUT", "body": profileObj})

        return result

    def delete(self, profileID: GenericID, credentials: ProfileCredentials) -> str:
        """
        @description:
            Permanently removes a profile from the account.

        @see:
            https://help.tago.io/portal/en/kb/articles/526-two-factor-authentication Two-Factor Authentication (2FA)

        @example:
            ```python
            resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
            # The "pin_code" field is required when 2FA is activated
            result = resources.profiles.delete("profile-id-123", {"password": "your-password", "pin_code": "123456"})
            print(result)  # Successfully Removed
            ```
        """
        result = self.doRequest({"path": f"/profile/{profileID}", "method": "DELETE", "body": credentials})

        return result

    def usageStatisticList(
        self, profileID: GenericID, dateObj: Optional[StatisticsDate] = None
    ) -> List[UsageStatistic]:
        """
        @description:
            Retrieves usage statistics for a profile within a specified time period.
            Usage statistics are cumulative: if a service was not used in a time period,
            the statistics for that time period will not be in the object.

        @example:
            If receive an error "Authorization Denied", check policy **Account** / **Access profile statistics** in Access Management.
            ```python
            resources = Resources()
            result = resources.profiles.usageStatisticList("profile-id-123", {
                "start_date": "2024-09-01",
                "end_date": "2024-12-31",
                "periodicity": "day"
            })
            print(result)  # [{'time': '2024-09-02T00:01:29.749Z', 'analysis': 0.07, 'data_records': 67254, ...}, ...]
            ```
        """
        result = self.doRequest(
            {
                "path": f"/profile/{profileID}/statistics",
                "method": "GET",
                "params": dateObj or {},
            }
        )

        result = dateParserList(result, ["time"])

        return result

    def auditLog(self, profileID: GenericID, filterObj: Optional[AuditLogFilter] = None) -> AuditLog:
        """
        @description:
            Creates a new audit log query for tracking profile activities.

        @see:
            https://help.tago.io/portal/en/kb/articles/audit-log Audit Log

        @example:
            ```python
            resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
            result = resources.profiles.auditLog("profile-id-123", {
                "start_date": "2024-12-01",
                "end_date": "2024-12-07"
            })
            print(result)
            ```
        """
        result = self.doRequest(
            {
                "path": f"/profile/{profileID}/auditlog",
                "method": "GET",
                "params": filterObj or {},
            }
        )

        if result.get("events"):
            result["events"] = dateParserList(result["events"], ["date"])

        return result

    def auditLogQuery(self, profileID: GenericID, queryId: str) -> AuditLog:
        """
        @description:
            Retrieves audit log entries using a previously created query.

        @see:
            https://help.tago.io/portal/en/kb/articles/audit-log Audit Log

        @example:
            ```python
            resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
            result = resources.profiles.auditLogQuery("profile-id-123", "query-id-456")
            print(result)
            ```
        """
        result = self.doRequest({"path": f"/profile/{profileID}/auditlog/{queryId}", "method": "GET"})

        if result.get("events"):
            result["events"] = dateParserList(result["events"], ["date"])

        return result

    def serviceEdit(self, profileID: GenericID, serviceObj: Dict) -> str:
        """
        @description:
            Updates service configuration and resource limits for a profile.

        @example:
            ```python
            resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
            result = resources.profiles.serviceEdit("profile-id-123", {
                "input": 350000,
                "output": 342153,
                "analysis": 5
            })
            print(result)  # Profile resource allocation Successfully Updated
            ```
        """
        result = self.doRequest(
            {
                "path": f"/profile/{profileID}/services",
                "method": "POST",
                "body": serviceObj,
            }
        )

        return result

    def transferTokenToAnotherProfile(self, targetProfileID: GenericID) -> str:
        """
        @description:
            Transfers the current authentication token to another profile.

        @example:
            ```python
            resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
            result = resources.profiles.transferTokenToAnotherProfile("target-profile-123")
            print(result)
            ```
        """
        result = self.doRequest({"path": f"/profile/switch/{targetProfileID}", "method": "PUT"})

        return result

    def tokenCreate(self, profileID: GenericID, tokenParams: TokenData) -> TokenCreateResponse:
        """
        @description:
            Creates a new authentication token for the specified profile.

        @see:
            https://help.tago.io/portal/en/kb/articles/495-account-token Account Token
            https://help.tago.io/portal/en/kb/articles/526-two-factor-authentication Two-Factor Authentication (2FA)

        @example:
            ```python
            resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
            # The "pin_code" / "otp_type" field is required when 2FA is activated
            result = resources.profiles.tokenCreate("profile-id-123", {
                "name": "API Access",
                "permission": "full",
                "email": "example@email.com",
                "password": "your-password"
            })
            print(result)  # {'token': 'token-value', 'name': 'API Access', ...}
            ```
        """
        result = self.doRequest(
            {
                "path": f"/profile/{profileID}/token",
                "method": "POST",
                "body": tokenParams,
            }
        )

        result = dateParser(result, ["expire_date"])

        return result

    def tokenDelete(self, profileID: GenericID, token: GenericToken) -> str:
        """
        @description:
            Revokes and removes an authentication token from the profile.

        @see:
            https://help.tago.io/portal/en/kb/articles/495-account-token Account Token

        @example:
            ```python
            resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
            result = resources.profiles.tokenDelete("profile-id-123", "token-xyz")
            print(result)  # Token Successfully Removed
            ```
        """
        result = self.doRequest({"path": f"/profile/{profileID}/token/{token}", "method": "DELETE"})

        return result

    def addTeamMember(self, profileID: GenericID, email: str) -> str:
        """
        @description:
            Adds a new team member to the profile using their email address.

        @see:
            https://help.tago.io/portal/en/kb/articles/106-sharing-your-profile Team Management - Sharing your Profile

        @example:
            ```python
            resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
            result = resources.profiles.addTeamMember("profile-id-123", "user@example.com")
            print(result)  # User invited
            ```
        """
        result = self.doRequest(
            {
                "path": f"/profile/{profileID}/team",
                "method": "POST",
                "body": {"email": email},
            }
        )

        return result

    def teamList(self, profileID: GenericID) -> List[ProfileTeam]:
        """
        @description:
            Retrieves a list of all team members that have access to the specified profile.

        @see:
            https://help.tago.io/portal/en/kb/articles/106-sharing-your-profile Team Management - Sharing your Profile

        @example:
            ```python
            resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
            result = resources.profiles.teamList("profile-id-123")
            print(result)  # [{'id': 'account-id-123', 'active': False, 'name': 'John Doe', ...}, ...]
            ```
        """
        result = self.doRequest({"path": f"/profile/{profileID}/team", "method": "GET"})

        result = dateParserList(result, ["created_at"])

        return result

    def deleteTeamMember(self, profileID: GenericID, accountId: str) -> str:
        """
        @description:
            Removes a team member from the profile.

        @see:
            https://help.tago.io/portal/en/kb/articles/106-sharing-your-profile Team Management - Sharing your Profile

        @example:
            If receive an error "Authorization Denied", check policy in Access Management.
            ```python
            resources = Resources()
            result = resources.profiles.deleteTeamMember("profile-id-123", "account-id-456")
            print(result)  # Account Successfully Removed
            ```
        """
        result = self.doRequest({"path": f"/profile/{profileID}/team/{accountId}", "method": "DELETE"})

        return result
