**Account**
===========

Manage your TagoIO account, authentication, and security settings.

====
info
====

Gets all account information including settings, preferences, and OTP configuration.

See: `Edit Account <https://api.docs.tago.io/#d1b06528-75e6-4dfc-80fb-9a553a26ea3b>`_

    **Returns:**

        | :ref:`AccountInfo`

    .. code-block:: python

        # If receive an error "Authorization Denied", check your account token permissions.
        from tagoio_sdk import Resources

        resources = Resources()
        account_info = resources.account.info()
        print(account_info)  # {'id': 'account-id', 'name': 'My Account', ...}


====
edit
====

Edit current account information such as name, timezone, company, and preferences.

See: `Edit Account <https://api.docs.tago.io/#d1b06528-75e6-4dfc-80fb-9a553a26ea3b>`_

    **Parameters:**

        | **accountObj**: dict
        | Account information to update

    **Returns:**

        | str

    .. code-block:: python

        # If receive an error "Authorization Denied", check your account token permissions.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.account.edit({
            "name": "Updated Account Name",
            "timezone": "America/New_York",
            "company": "My Company"
        })
        print(result)  # Account Successfully Updated


======
delete
======

Delete current account. This action is irreversible and will remove all profiles and data.

See: `Deleting Your Account <https://help.tago.io/portal/en/kb/articles/210-deleting-your-account>`_

    **Returns:**

        | str

    .. code-block:: python

        # If receive an error "Authorization Denied", check your account token permissions.
        # WARNING: This action is irreversible!
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.account.delete()
        print(result)  # Account Successfully Deleted


==============
passwordChange
==============

Change account password for the authenticated user.

See: `Resetting My Password <https://help.tago.io/portal/en/kb/articles/209-resetting-my-password>`_

    **Parameters:**

        | **password**: str
        | New password

    **Returns:**

        | str

    .. code-block:: python

        # If receive an error "Authorization Denied", check your account token permissions.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.account.passwordChange("new-secure-password")
        print(result)  # Password changed successfully


=========
enableOTP
=========

Enable OTP (One-Time Password) for a given OTP Type (authenticator, sms, or email).
You will be requested to confirm the operation with a pin code.

See: `Two-Factor Authentication <https://help.tago.io/portal/en/kb/articles/526-two-factor-authentication>`_

    **Parameters:**

        | **credentials**: dict
        | Dictionary with email and password

        | **typeOTP**: :ref:`OTPType`
        | Type of OTP: "authenticator", "sms", or "email"

    **Returns:**

        | str

    .. code-block:: python

        # If receive an error "Authorization Denied", check your account token permissions.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.account.enableOTP(
            {"email": "user@example.com", "password": "your-password"},
            "email"
        )
        print(result)  # OTP enabled, confirmation required


==========
disableOTP
==========

Disable OTP (One-Time Password) for a given OTP Type (authenticator, sms, or email).

See: `Two-Factor Authentication <https://help.tago.io/portal/en/kb/articles/526-two-factor-authentication>`_

    **Parameters:**

        | **credentials**: dict
        | Dictionary with email and password

        | **typeOTP**: :ref:`OTPType`
        | Type of OTP: "authenticator", "sms", or "email"

    **Returns:**

        | str

    .. code-block:: python

        # If receive an error "Authorization Denied", check your account token permissions.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.account.disableOTP(
            {"email": "user@example.com", "password": "your-password"},
            "authenticator"
        )
        print(result)  # OTP disabled successfully


==========
confirmOTP
==========

Confirm OTP enabling process for a given OTP Type (authenticator, sms, or email).

See: `Two-Factor Authentication <https://help.tago.io/portal/en/kb/articles/526-two-factor-authentication>`_

    **Parameters:**

        | **pinCode**: str
        | Six-digit PIN code

        | **typeOTP**: :ref:`OTPType`
        | Type of OTP: "authenticator", "sms", or "email"

    **Returns:**

        | str

    .. code-block:: python

        # If receive an error "Authorization Denied", check your account token permissions.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.account.confirmOTP("123456", "email")
        print(result)  # OTP confirmed successfully


===========
tokenCreate
===========

Generates and retrieves a new token for the account. This is a static method that doesn't require authentication.

See: `Account Token <https://help.tago.io/portal/en/kb/articles/495-account-token>`_

    **Parameters:**

        | **tokenParams**: :ref:`TokenCreateInfo`
        | Token creation parameters

        | *Optional* **region**: :ref:`Regions`
        | TagoIO Region Server (default: USA)

    **Returns:**

        | dict

    .. code-block:: python

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


=====
login
=====

Retrieve list of profiles for login and perform authentication. This is a static method that doesn't require authentication.

See: `Login to Account <https://api.docs.tago.io/#3196249b-4aef-46ff-b5c3-f103b6f0bfbd>`_

    **Parameters:**

        | **credentials**: :ref:`LoginCredentials`
        | Login credentials including email, password, OTP type, and PIN code

        | *Optional* **region**: :ref:`Regions`
        | TagoIO Region Server (default: USA)

    **Returns:**

        | :ref:`LoginResponse`

    .. code-block:: python

        from tagoio_sdk.modules.Resources.Account import Account

        login_result = Account.login({
            "email": "user@example.com",
            "password": "your-password",
            "otp_type": "email",
            "pin_code": "123456"
        })
        print(login_result)  # {'type': 'user', 'id': '...', 'profiles': [...]}


==============
passwordRecover
==============

Send password recovery email to the specified address. This is a static method that doesn't require authentication.

See: `Resetting My Password <https://help.tago.io/portal/en/kb/articles/209-resetting-my-password>`_

    **Parameters:**

        | **email**: str
        | Email address for password recovery

        | *Optional* **region**: :ref:`Regions`
        | TagoIO Region Server (default: USA)

    **Returns:**

        | str

    .. code-block:: python

        from tagoio_sdk.modules.Resources.Account import Account

        result = Account.passwordRecover("user@example.com")
        print(result)  # Email sent successfully


======
create
======

Create a new TagoIO account. This is a static method that doesn't require authentication.

    **Parameters:**

        | **createParams**: :ref:`AccountCreateInfo`
        | Account creation parameters

        | *Optional* **region**: :ref:`Regions`
        | TagoIO Region Server (default: USA)

    **Returns:**

        | str

    .. code-block:: python

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


==================
resendConfirmation
==================

Re-send confirmation account email to the specified address. This is a static method that doesn't require authentication.

    **Parameters:**

        | **email**: str
        | Email address to resend confirmation

        | *Optional* **region**: :ref:`Regions`
        | TagoIO Region Server (default: USA)

    **Returns:**

        | str

    .. code-block:: python

        from tagoio_sdk.modules.Resources.Account import Account

        result = Account.resendConfirmation("user@example.com")
        print(result)  # Confirmation email sent


==============
confirmAccount
==============

Confirm account creation using the token sent via email. This is a static method that doesn't require authentication.

    **Parameters:**

        | **token**: str
        | Confirmation token from email

        | *Optional* **region**: :ref:`Regions`
        | TagoIO Region Server (default: USA)

    **Returns:**

        | str

    .. code-block:: python

        from tagoio_sdk.modules.Resources.Account import Account

        result = Account.confirmAccount("confirmation-token-123")
        print(result)  # Account confirmed successfully


==================
requestLoginPINCode
==================

Request the PIN Code for a given OTP Type (authenticator, sms, or email). This is a static method that doesn't require authentication.

See: `Two-Factor Authentication <https://help.tago.io/portal/en/kb/articles/526-two-factor-authentication>`_

    **Parameters:**

        | **credentials**: dict
        | Dictionary with email and password

        | **typeOTP**: :ref:`OTPType`
        | Type of OTP: "authenticator", "sms", or "email"

        | *Optional* **region**: :ref:`Regions`
        | TagoIO Region Server (default: USA)

    **Returns:**

        | str

    .. code-block:: python

        from tagoio_sdk.modules.Resources.Account import Account

        result = Account.requestLoginPINCode(
            {"email": "user@example.com", "password": "your-password"},
            "email"
        )
        print(result)  # PIN code sent


====================
acceptTeamInvitation
====================

Accept a team member invitation to become a profile's team member. This is a static method that doesn't require authentication.

    **Parameters:**

        | **token**: str
        | Invitation token from email

        | *Optional* **region**: :ref:`Regions`
        | TagoIO Region Server (default: USA)

    **Returns:**

        | str

    .. code-block:: python

        from tagoio_sdk.modules.Resources.Account import Account

        result = Account.acceptTeamInvitation("invitation-token-123")
        print(result)  # Invitation accepted


=====================
declineTeamInvitation
=====================

Decline a team member invitation to become a profile's team member. This is a static method that doesn't require authentication.

    **Parameters:**

        | **token**: str
        | Invitation token from email

        | *Optional* **region**: :ref:`Regions`
        | TagoIO Region Server (default: USA)

    **Returns:**

        | str

    .. code-block:: python

        from tagoio_sdk.modules.Resources.Account import Account

        result = Account.declineTeamInvitation("invitation-token-123")
        print(result)  # Invitation declined

.. toctree::

    Account_Type
    ../../regions
