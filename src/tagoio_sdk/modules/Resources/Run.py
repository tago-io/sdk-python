from typing import Optional, TypedDict

from tagoio_sdk.common.Common_Type import GenericID, Query
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Resources.Notification_Type import (
    NotificationCreate,
    NotificationCreateReturn,
    NotificationInfo,
)
from tagoio_sdk.modules.Resources.Run_Type import (
    CustomDomainCreate,
    CustomDomainInfo,
    LoginAsUserOptions,
    LoginResponse,
    RunInfo,
    RunSAMLEditInfo,
    RunSAMLInfo,
    UserCreateInfo,
    UserInfo,
)
from tagoio_sdk.modules.Utils.dateParser import dateParser, dateParserList


class Run(TagoIOModule):
    """
    Manage services in account
    Be sure to use an account token with “write” permissions when using
    functions like create, edit and delete.
    """

    def info(self) -> RunInfo:
        result = self.doRequest(
            {
                "path": "/run",
                "method": "GET",
            }
        )

        return result

    def edit(self, data: RunInfo) -> str:
        result = self.doRequest(
            {
                "path": "/run",
                "method": "PUT",
                "body": data,
            }
        )

        return result

    def listUsers(self, query: Query) -> list[UserInfo]:
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
        result = self.doRequest(
            {
                "path": f"/run/users/{userID}",
                "method": "GET",
            }
        )

        result = dateParser(result, ["created_at", "updated_at", "last_login"])

        return result

    def userCreate(self, data: UserCreateInfo) -> str:
        result = self.doRequest(
            {
                "path": "/run/users",
                "method": "POST",
                "body": data,
            }
        )

        return result

    def userEdit(self, userID: GenericID, data: UserInfo) -> str:
        result = self.doRequest(
            {
                "path": f"/run/users/{userID}",
                "method": "PUT",
                "body": data,
            }
        )

        return result

    def userDelete(self, userID: GenericID) -> str:
        result = self.doRequest(
            {
                "path": f"/run/users/{userID}",
                "method": "DELETE",
            }
        )

        return result

    def loginAsUser(
        self, userID: GenericID, options: Optional[LoginAsUserOptions]
    ) -> LoginResponse:
        result = self.doRequest(
            {
                "path": f"/run/users/{userID}/login",
                "params": options,
                "method": "GET",
            }
        )

        result = dateParser(result, ["expire_date"])

        return result

    class emailData(TypedDict):
        subject: str
        body: str

    def emailTest(self, data: emailData) -> str:
        result = self.doRequest(
            {
                "path": "/run/email_test",
                "method": "POST",
                "body": data,
            }
        )

        return result

    def notificationList(self, userID: GenericID) -> list[NotificationInfo]:
        result = self.doRequest(
            {
                "path": f"/run/notification/{userID}",
                "method": "GET",
            }
        )

        return result

    def notificationCreate(
        self, userID: GenericID, data: NotificationCreate
    ) -> NotificationCreateReturn:
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

    def notificationEdit(
        self, notificationID: GenericID, data: NotificationCreate
    ) -> str:
        result = self.doRequest(
            {
                "path": f"/run/notification/{notificationID}",
                "method": "PUT",
                "body": data,
            }
        )

        return result

    def notificationDelete(self, notificationID: GenericID) -> str:
        result = self.doRequest(
            {
                "path": f"/run/notification/{notificationID}",
                "method": "DELETE",
            }
        )

        return result

    def ssoSAMLInfo(self) -> RunSAMLInfo:
        """
        Get the SAML Single Sign-On information for the account's RUN.
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
        Edit the SAML Single Sign-On metadata and mappings for the account's RUN.
        :param: data Updated data for a RUN's SAML Single Sign-On configuration.
        """

        result = self.doRequest(
            {
                "path": "/run/sso/saml",
                "method": "PUT",
                "body": data,
            }
        )

        return result

    def createCustomDomain(
        self, profile_id: str, customDomainData: CustomDomainCreate
    ) -> str:
        """
        Create a TagoRUN custom domain for the profile.
        :param: profile_id ID of the profile
        :param: customDomainData query params
        :returns: Success message.
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
        set details of TagoRun custom domain for the profile.
        :param: profile_id ID of the profile
        :returns: Data for the profile's custom DNS configuration.
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
        delete a TagoRUN custom domain for the profile.
        :param: profile_id ID of the profile
        :returns: Success message.
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
        Regenerate a TagoRUN custom domain for the profile.
        :param: profile_id ID of the profile
        :returns: Success message.
        """

        result = self.doRequest(
            {
                "path": f"/run/customdomain/regenerate/{profile_id}",
                "method": "PUT",
            }
        )

        return result
