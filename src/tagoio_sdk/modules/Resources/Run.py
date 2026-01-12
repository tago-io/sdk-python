from typing import Dict
from typing import Optional

from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.Common_Type import Query
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Resources.Notification_Type import NotificationCreate
from tagoio_sdk.modules.Resources.Notification_Type import NotificationCreateReturn
from tagoio_sdk.modules.Resources.Notification_Type import NotificationInfo
from tagoio_sdk.modules.Resources.Run_Type import CustomDomainCreate
from tagoio_sdk.modules.Resources.Run_Type import CustomDomainInfo
from tagoio_sdk.modules.Resources.Run_Type import EmailTestData
from tagoio_sdk.modules.Resources.Run_Type import LoginAsUserOptions
from tagoio_sdk.modules.Resources.Run_Type import LoginResponse
from tagoio_sdk.modules.Resources.Run_Type import RunInfo
from tagoio_sdk.modules.Resources.Run_Type import RunSAMLEditInfo
from tagoio_sdk.modules.Resources.Run_Type import RunSAMLInfo
from tagoio_sdk.modules.Resources.Run_Type import UserCreateInfo
from tagoio_sdk.modules.Resources.Run_Type import UserInfo
from tagoio_sdk.modules.Utils.dateParser import dateParser
from tagoio_sdk.modules.Utils.dateParser import dateParserList


class Run(TagoIOModule):
    def info(self) -> RunInfo:
        """
        @description:
            Retrieves information about the current Run environment configuration.

        @see:
            https://help.tago.io/portal/en/kb/articles/191-tagorun TagoRun
            https://help.tago.io/portal/en/kb/articles/run-themes Run Themes

        @example:
            If receive an error "Authorization Denied", check policy **Profile** / **Access TagoRun settings** in Access Management.
            ```python
            resources = Resources()
            result = resources.run.info()
            print(result)  # {'name': 'My Run Environment', 'logo': 'https://example.com/logo.png', ...}
            ```
        """
        result = self.doRequest(
            {
                "path": "/run",
                "method": "GET",
            }
        )

        return result

    def edit(self, data: Dict) -> str:
        """
        @description:
            Updates the Run environment configuration settings.

        @see:
            https://help.tago.io/portal/en/kb/articles/191-tagorun TagoRun
            https://help.tago.io/portal/en/kb/articles/run-themes Run Themes

        @example:
            If receive an error "Authorization Denied", check policy **Profile** / **Edit TagoRun settings** in Access Management.
            ```python
            resources = Resources()
            result = resources.run.edit({"name": "My Run Environment", "logo": "https://example.com/logo.png"})
            print(result)  # TagoIO Run Successfully Updated
            ```
        """
        result = self.doRequest(
            {
                "path": "/run",
                "method": "PUT",
                "body": data,
            }
        )

        return result

    def listUsers(self, query: Optional[Query] = {}) -> list[UserInfo]:
        """
        @description:
            Retrieves a paginated list of Run users with customizable fields and filtering options.

        @see:
            https://help.tago.io/portal/en/kb/articles/191-tagorun TagoRun

        @example:
            If receive an error "Authorization Denied", or return empty list check policy **Run User** / **Access** in Access Management.
            ```python
            resources = Resources()
            result = resources.run.listUsers({
                "page": 1,
                "fields": ["id", "name", "email"],
                "amount": 20
            })
            print(result)  # [{'id': 'user-id-123', 'name': 'John Doe', 'email': 'example@email.com'}]
            ```
        """
        if "orderBy" in query:
            firstArgument = query["orderBy"][0]
            secondArgument = query["orderBy"][1]
            orderBy = f"{firstArgument},{secondArgument}"
        else:
            orderBy = "name,asc"

        result = self.doRequest(
            {
                "path": "/run/users",
                "method": "GET",
                "params": {
                    "page": query.get("page") or 1,
                    "fields": query.get("fields") or ["id", "name"],
                    "filter": query.get("filter") or {},
                    "amount": query.get("amount") or 20,
                    "orderBy": orderBy,
                },
            }
        )
        result = dateParserList(result, ["created_at", "updated_at", "last_login"])

        return result

    def userInfo(self, userID: GenericID) -> UserInfo:
        """
        @description:
            Retrieves detailed information about a specific Run user.

        @see:
            https://help.tago.io/portal/en/kb/articles/191-tagorun TagoRun

        @example:
            If receive an error "Authorization Denied", check policy **Run User** / **Access** in Access Management.
            ```python
            resources = Resources()
            result = resources.run.userInfo("user-id-123")
            print(result)  # {'id': 'user-id-123', 'name': 'John Doe', 'email': 'example@email.com', ...}
            ```
        """
        result = self.doRequest(
            {
                "path": f"/run/users/{userID}",
                "method": "GET",
            }
        )

        result = dateParser(result, ["created_at", "updated_at", "last_login"])

        return result

    def userCreate(self, data: UserCreateInfo) -> Dict[str, str]:
        """
        @description:
            Creates a new user in the Run environment.

        @see:
            https://help.tago.io/portal/en/kb/articles/191-tagorun TagoRun

        @example:
            If receive an error "Authorization Denied", check policy **Run User** / **Create** in Access Management.
            ```python
            resources = Resources()
            result = resources.run.userCreate({
                "name": "John Doe",
                "email": "john@example.com",
                "password": "secure123",
                "timezone": "America/New_York"
            })
            print(result)  # {'user': 'user-id-123'}
            ```
        """
        result = self.doRequest(
            {
                "path": "/run/users",
                "method": "POST",
                "body": data,
            }
        )

        return result

    def userEdit(self, userID: GenericID, data: Dict) -> str:
        """
        @description:
            Updates information for an existing Run user.

        @see:
            https://help.tago.io/portal/en/kb/articles/191-tagorun TagoRun

        @example:
            If receive an error "Authorization Denied", check policy **Run User** / **Edit** in Access Management.
            ```python
            resources = Resources()
            result = resources.run.userEdit("user-id-123", {"name": "Updated Name"})
            print(result)  # TagoIO Run User Successfully Updated
            ```
        """
        result = self.doRequest(
            {
                "path": f"/run/users/{userID}",
                "method": "PUT",
                "body": data,
            }
        )

        return result

    def userDelete(self, userID: GenericID) -> str:
        """
        @description:
            Permanently deletes a user from the Run environment.

        @see:
            https://help.tago.io/portal/en/kb/articles/191-tagorun TagoRun

        @example:
            If receive an error "Authorization Denied", check policy **Run User** / **Delete** in Access Management.
            ```python
            resources = Resources()
            result = resources.run.userDelete("user-id-123")
            print(result)  # Successfully Removed
            ```
        """
        result = self.doRequest(
            {
                "path": f"/run/users/{userID}",
                "method": "DELETE",
            }
        )

        return result

    def loginAsUser(self, userID: GenericID, options: Optional[LoginAsUserOptions] = None) -> LoginResponse:
        """
        @description:
            Generates a login token to authenticate as a specific Run user.

        @example:
            If receive an error "Authorization Denied", check policy **Run User** / **Login as user** in Access Management.
            ```python
            resources = Resources()
            result = resources.run.loginAsUser("user-id-123")
            print(result["token"])  # eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ...
            ```
        """
        result = self.doRequest(
            {
                "path": f"/run/users/{userID}/login",
                "params": options,
                "method": "GET",
            }
        )

        result = dateParser(result, ["expire_date"])

        return result

    def emailTest(self, data: EmailTestData) -> str:
        """
        @description:
            Tests the email configuration by sending a test message.

        @example:
            ```python
            resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
            result = resources.run.emailTest({"subject": "Test Email", "body": "This is a test message"})
            print(result)  # E-mail sent to example@email.com
            ```
        """
        result = self.doRequest(
            {
                "path": "/run/email_test",
                "method": "POST",
                "body": data,
            }
        )

        return result

    def notificationList(self, userID: GenericID) -> list[NotificationInfo]:
        """
        @description:
            Retrieves a list of notifications for a specific Run user.

        @see:
            https://help.tago.io/portal/en/kb/articles/223-notifications-for-users Notifications for Users

        @example:
            If receive an error "Authorization Denied", check policy **Run User** / **Access notification** in Access Management.
            ```python
            resources = Resources()
            result = resources.run.notificationList("user-id-123")
            print(result)  # [{'id': 'notification-id-123', 'title': 'System Update', 'message': 'Features', ...}]
            ```
        """
        result = self.doRequest(
            {
                "path": f"/run/notification/{userID}",
                "method": "GET",
            }
        )

        return result

    def notificationCreate(self, userID: GenericID, data: NotificationCreate) -> NotificationCreateReturn:
        """
        @description:
            Creates a new notification for a Run user.

        @see:
            https://help.tago.io/portal/en/kb/articles/223-notifications-for-users Notifications for Users

        @example:
            If receive an error "Authorization Denied", check policy **Run User** / **Create notification** in Access Management.
            ```python
            resources = Resources()
            result = resources.run.notificationCreate("user-id-123", {
                "title": "Update",
                "message": "New feature available"
            })
            print(result)  # {'id': 'notification-id-123'}
            ```
        """
        result = self.doRequest(
            {
                "path": "/run/notification/",
                "method": "POST",
                "body": {
                    "run_user": userID,
                    **data,
                },
            }
        )

        return result

    def notificationEdit(self, notificationID: GenericID, data: Dict) -> str:
        """
        @description:
            Updates an existing notification in the Run environment.

        @see:
            https://help.tago.io/portal/en/kb/articles/223-notifications-for-users Notifications for Users

        @example:
            If receive an error "Authorization Denied", check policy **Run User** / **Edit notification** in Access Management.
            ```python
            resources = Resources()
            result = resources.run.notificationEdit("notification-id-123", {"title": "Updated Title"})
            print(result)  # TagoIO Notification User Successfully Updated
            ```
        """
        result = self.doRequest(
            {
                "path": f"/run/notification/{notificationID}",
                "method": "PUT",
                "body": data,
            }
        )

        return result

    def notificationDelete(self, notificationID: GenericID) -> str:
        """
        @description:
            Deletes a notification from the Run environment.

        @see:
            https://help.tago.io/portal/en/kb/articles/223-notifications-for-users Notifications for Users

        @example:
            If receive an error "Authorization Denied", check policy **Run User** / **Delete notification** in Access Management.
            ```python
            resources = Resources()
            result = resources.run.notificationDelete("notification-id-123")
            print(result)  # Successfully Removed
            ```
        """
        result = self.doRequest(
            {
                "path": f"/run/notification/{notificationID}",
                "method": "DELETE",
            }
        )

        return result

    def ssoSAMLInfo(self) -> RunSAMLInfo:
        """
        @description:
            Retrieves the SAML Single Sign-On configuration information for the Run environment.

        @see:
            https://help.tago.io/portal/en/kb/articles/491-single-sign-on-sso Single Sign-On (SSO)

        @example:
            ```python
            resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
            result = resources.run.ssoSAMLInfo()
            print(result)  # {'sp': {'entity_id': 'https://example.com', ...}, ...}
            ```
        """
        result = self.doRequest(
            {
                "path": "/run/sso/saml",
                "method": "GET",
            }
        )

        return result

    def ssoSAMLEdit(self, data: RunSAMLEditInfo) -> str:
        """
        @description:
            Updates the SAML SSO configuration for the Run environment.

        @see:
            https://help.tago.io/portal/en/kb/articles/491-single-sign-on-sso Single Sign-On (SSO)

        @example:
            ```python
            resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
            result = resources.run.ssoSAMLEdit({
                "active": True,
                "idp_metadata": "<xml>...</xml>"
            })
            print(result)  # TagoIO Run SAML SSO Successfully Updated
            ```
        """
        result = self.doRequest(
            {
                "path": "/run/sso/saml",
                "method": "PUT",
                "body": data,
            }
        )

        return result

    def createCustomDomain(self, profile_id: str, customDomainData: CustomDomainCreate) -> str:
        """
        @description:
            Creates a custom domain configuration for the Run environment.

        @see:
            https://help.tago.io/portal/en/kb/articles/custom-domain-configuration Custom Domain Configuration

        @example:
            ```python
            resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
            result = resources.run.createCustomDomain("profile-id-123", {
                "domain": "app.mycompany.com"
            })
            print(result)  # Custom domain created successfully
            ```
        """
        result = self.doRequest(
            {
                "path": f"/run/customdomain/{profile_id}",
                "body": customDomainData,
                "method": "POST",
            }
        )

        return result

    def getCustomDomain(self, profile_id: str) -> CustomDomainInfo:
        """
        @description:
            Retrieves the custom domain configuration for a Run profile.

        @see:
            https://help.tago.io/portal/en/kb/articles/custom-domain-configuration Custom Domain Configuration

        @example:
            ```python
            resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
            result = resources.run.getCustomDomain("profile-id-123")
            print(result)  # {'domain': 'app.mycompany.com', 'verified': True, ...}
            ```
        """
        result = self.doRequest(
            {
                "path": f"/run/customdomain/{profile_id}",
                "method": "GET",
            }
        )

        parsedResult = dateParser(result, ["created_at"])

        return parsedResult

    def deleteCustomDomain(self, profile_id: str) -> str:
        """
        @description:
            Removes the custom domain configuration from a Run profile.

        @see:
            https://help.tago.io/portal/en/kb/articles/custom-domain-configuration Custom Domain Configuration

        @example:
            ```python
            resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
            result = resources.run.deleteCustomDomain("profile-id-123")
            print(result)  # Custom domain deleted successfully
            ```
        """
        result = self.doRequest(
            {
                "path": f"/run/customdomain/{profile_id}",
                "method": "DELETE",
            }
        )
        return result

    def regenerateCustomDomain(self, profile_id: str) -> str:
        """
        @description:
            Regenerates the custom domain configuration for a Run profile.

        @see:
            https://help.tago.io/portal/en/kb/articles/custom-domain-configuration Custom Domain Configuration

        @example:
            ```python
            resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
            result = resources.run.regenerateCustomDomain("profile-id-123")
            print(result)  # Custom domain regenerated successfully
            ```
        """
        result = self.doRequest(
            {
                "path": f"/run/customdomain/regenerate/{profile_id}",
                "method": "PUT",
            }
        )

        return result
