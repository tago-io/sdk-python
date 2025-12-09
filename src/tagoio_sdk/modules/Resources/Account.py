from typing import Dict
from typing import Optional

from tagoio_sdk.common.Common_Type import GenericToken
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Resources.Account_Types import AccountCreateInfo
from tagoio_sdk.modules.Resources.Account_Types import AccountInfo
from tagoio_sdk.modules.Resources.Account_Types import LoginCredentials
from tagoio_sdk.modules.Resources.Account_Types import LoginResponse
from tagoio_sdk.modules.Resources.Account_Types import OTPType
from tagoio_sdk.modules.Resources.Account_Types import TokenCreateInfo
from tagoio_sdk.modules.Utils.dateParser import dateParser
from tagoio_sdk.regions import Regions


class Account(TagoIOModule):
    def info(self) -> AccountInfo:
        """
        @description:
            Gets all account information.

        @see:
            https://api.docs.tago.io/#d1b06528-75e6-4dfc-80fb-9a553a26ea3b

        @example:
            If receive an error "Authorization Denied", check your account token permissions.
            ```python
            resources = Resources()
            account_info = resources.account.info()
            print(account_info)  # {'id': 'account-id', 'name': 'My Account', ...}
            ```
        """
        result = self.doRequest(
            {
                "path": "/account",
                "method": "GET",
            }
        )
        result = dateParser(result, ["created_at", "updated_at", "last_login"])

        if result.get("options"):
            result["options"] = dateParser(result["options"], ["last_whats_new"])

        return result

    def edit(self, accountObj: Dict) -> str:
        """
        @description:
            Edit current account information.

        @see:
            https://api.docs.tago.io/#d1b06528-75e6-4dfc-80fb-9a553a26ea3b

        @example:
            If receive an error "Authorization Denied", check your account token permissions.
            ```python
            resources = Resources()
            result = resources.account.edit({
                "id": "account-id"
                "name": "Updated Account Name",
                "timezone": "America/New_York",
                "company": "My Company"
            })
            print(result)  # Account Successfully Updated
            ```
        """
        result = self.doRequest(
            {
                "path": "/account",
                "method": "PUT",
                "body": accountObj,
            }
        )

        return result

    def delete(self) -> str:
        """
        @description:
            Delete current account. This action is irreversible and will remove all profiles and data.

        @see:
            https://help.tago.io/portal/en/kb/articles/210-deleting-your-account

        @example:
            If receive an error "Authorization Denied", check your account token permissions.
            ```python
            resources = Resources()
            result = resources.account.delete()
            print(result)  # Account Successfully Deleted
            ```
        """
        result = self.doRequest(
            {
                "path": "/account",
                "method": "DELETE",
            }
        )

        return result

    @staticmethod
    def tokenCreate(tokenParams: TokenCreateInfo, region: Optional[Regions] = None) -> Dict[str, GenericToken]:
        """
        @description:
            Generates and retrieves a new token for the account.

        @see:
            https://help.tago.io/portal/en/kb/articles/495-account-token

        @example:
            ```python
            from tagoio_sdk.modules.Resources.Account import Account

            token_result = Account.tokenCreate({
                "profile_id": "profile-id-123",
                "email": "user@example.com",
                "password": "your-password",
                "pin_code": "123456",
                "otp_type": "email",
                "name": "My API Token"
            })
            print(token_result["token"])  # your-new-token-123
            ```
        """
        result = TagoIOModule.doRequestAnonymous(
            {
                "path": "/account/profile/token",
                "method": "POST",
                "body": tokenParams,
            },
            region,
        )

        return result

    @staticmethod
    def login(credentials: LoginCredentials, region: Optional[Regions] = None) -> LoginResponse:
        """
        @description:
            Retrieve list of profiles for login and perform authentication.

        @see:
            https://api.docs.tago.io/#3196249b-4aef-46ff-b5c3-f103b6f0bfbd

        @example:
            ```python
            from tagoio_sdk.modules.Resources.Account import Account

            login_result = Account.login({
                "email": "user@example.com",
                "password": "your-password",
                "otp_type": "email",
                "pin_code": "123456"
            })
            print(login_result)  # {'type': 'user', 'id': '...', 'profiles': [...]}
            ```
        """
        result = TagoIOModule.doRequestAnonymous(
            {
                "path": "/account/login",
                "method": "POST",
                "body": credentials,
            },
            region,
        )

        return result

    @staticmethod
    def passwordRecover(email: str, region: Optional[Regions] = None) -> str:
        """
        @description:
            Send password recovery email to the specified address.

        @see:
            https://help.tago.io/portal/en/kb/articles/209-resetting-my-password

        @example:
            ```python
            from tagoio_sdk.modules.Resources.Account import Account

            result = Account.passwordRecover("user@example.com")
            print(result)  # Email sent successfully
            ```
        """
        result = TagoIOModule.doRequestAnonymous(
            {
                "path": f"/account/passwordreset/{email}",
                "method": "GET",
            },
            region,
        )

        return result

    def passwordChange(self, password: str) -> str:
        """
        @description:
            Change account password for the authenticated user.

        @see:
            https://help.tago.io/portal/en/kb/articles/209-resetting-my-password

        @example:
            If receive an error "Authorization Denied", check your account token permissions.
            ```python
            resources = Resources()
            result = resources.account.passwordChange("new-secure-password")
            print(result)  # Password changed successfully
            ```
        """
        result = self.doRequest(
            {
                "path": "/account/passwordreset",
                "method": "POST",
                "body": {"password": password},
            }
        )

        return result

    @staticmethod
    def create(createParams: AccountCreateInfo, region: Optional[Regions] = None) -> str:
        """
        @description:
            Create a new TagoIO account.

        @example:
            ```python
            from tagoio_sdk.modules.Resources.Account import Account

            result = Account.create({
                "name": "John Doe",
                "email": "john@example.com",
                "password": "secure-password",
                "cpassword": "secure-password",
                "timezone": "America/New_York",
                "company": "My Company",
                "newsletter": False
            })
            print(result)  # Account created successfully
            ```
        """
        result = TagoIOModule.doRequestAnonymous(
            {
                "path": "/account",
                "method": "POST",
                "body": createParams,
            },
            region,
        )

        return result

    @staticmethod
    def resendConfirmation(email: str, region: Optional[Regions] = None) -> str:
        """
        @description:
            Re-send confirmation account email to the specified address.

        @example:
            ```python
            from tagoio_sdk.modules.Resources.Account import Account

            result = Account.resendConfirmation("user@example.com")
            print(result)  # Confirmation email sent
            ```
        """
        result = TagoIOModule.doRequestAnonymous(
            {
                "path": f"/account/resend_confirmation/{email}",
                "method": "GET",
            },
            region,
        )

        return result

    @staticmethod
    def confirmAccount(token: GenericToken, region: Optional[Regions] = None) -> str:
        """
        @description:
            Confirm account creation using the token sent via email.

        @example:
            ```python
            from tagoio_sdk.modules.Resources.Account import Account

            result = Account.confirmAccount("confirmation-token-123")
            print(result)  # Account confirmed successfully
            ```
        """
        result = TagoIOModule.doRequestAnonymous(
            {
                "path": f"/account/confirm/{token}",
                "method": "GET",
            },
            region,
        )

        return result

    @staticmethod
    def requestLoginPINCode(credentials: Dict[str, str], typeOTP: OTPType, region: Optional[Regions] = None) -> str:
        """
        @description:
            Request the PIN Code for a given OTP Type (authenticator, sms, or email).

        @see:
            https://help.tago.io/portal/en/kb/articles/526-two-factor-authentication

        @example:
            ```python
            from tagoio_sdk.modules.Resources.Account import Account

            result = Account.requestLoginPINCode(
                {"email": "user@example.com", "password": "your-password"},
                "email"
            )
            print(result)  # PIN code sent
            ```
        """
        body = {**credentials, "otp_type": typeOTP}
        result = TagoIOModule.doRequestAnonymous(
            {
                "path": "/account/login/otp",
                "method": "POST",
                "body": body,
            },
            region,
        )

        return result

    def enableOTP(self, credentials: Dict[str, str], typeOTP: OTPType) -> str:
        """
        @description:
            Enable OTP (One-Time Password) for a given OTP Type (authenticator, sms, or email).
            You will be requested to confirm the operation with a pin code.

        @see:
            https://help.tago.io/portal/en/kb/articles/526-two-factor-authentication

        @example:
            If receive an error "Authorization Denied", check your account token permissions.
            ```python
            resources = Resources()
            result = resources.account.enableOTP(
                {"email": "user@example.com", "password": "your-password"},
                "email"
            )
            print(result)  # OTP enabled, confirmation required
            ```
        """
        result = self.doRequest(
            {
                "path": f"/account/otp/{typeOTP}/enable",
                "method": "POST",
                "body": credentials,
            }
        )

        return result

    def disableOTP(self, credentials: Dict[str, str], typeOTP: OTPType) -> str:
        """
        @description:
            Disable OTP (One-Time Password) for a given OTP Type (authenticator, sms, or email).

        @see:
            https://help.tago.io/portal/en/kb/articles/526-two-factor-authentication

        @example:
            If receive an error "Authorization Denied", check your account token permissions.
            ```python
            resources = Resources()
            result = resources.account.disableOTP(
                {"email": "user@example.com", "password": "your-password"},
                "authenticator"
            )
            print(result)  # OTP disabled successfully
            ```
        """
        result = self.doRequest(
            {
                "path": f"/account/otp/{typeOTP}/disable",
                "method": "POST",
                "body": credentials,
            }
        )

        return result

    def confirmOTP(self, pinCode: str, typeOTP: OTPType) -> str:
        """
        @description:
            Confirm OTP enabling process for a given OTP Type (authenticator, sms, or email).

        @see:
            https://help.tago.io/portal/en/kb/articles/526-two-factor-authentication

        @example:
            If receive an error "Authorization Denied", check your account token permissions.
            ```python
            resources = Resources()
            result = resources.account.confirmOTP("123456", "email")
            print(result)  # OTP confirmed successfully
            ```
        """
        result = self.doRequest(
            {
                "path": f"/account/otp/{typeOTP}/confirm",
                "method": "POST",
                "body": {"pin_code": pinCode},
            }
        )

        return result

    @staticmethod
    def acceptTeamInvitation(token: str, region: Optional[Regions] = None) -> str:
        """
        @description:
            Accept a team member invitation to become a profile's team member.

        @example:
            ```python
            from tagoio_sdk.modules.Resources.Account import Account

            result = Account.acceptTeamInvitation("invitation-token-123")
            print(result)  # Invitation accepted
            ```
        """
        result = TagoIOModule.doRequestAnonymous(
            {
                "path": f"/profile/team/accept/{token}",
                "method": "GET",
            },
            region,
        )

        return result

    @staticmethod
    def declineTeamInvitation(token: str, region: Optional[Regions] = None) -> str:
        """
        @description:
            Decline a team member invitation to become a profile's team member.

        @example:
            ```python
            from tagoio_sdk.modules.Resources.Account import Account

            result = Account.declineTeamInvitation("invitation-token-123")
            print(result)  # Invitation declined
            ```
        """
        result = TagoIOModule.doRequestAnonymous(
            {
                "path": f"/profile/team/decline/{token}",
                "method": "GET",
            },
            region,
        )

        return result
