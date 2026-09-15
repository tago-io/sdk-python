**Account Type**
=================


.. _AccountOptions:

AccountOptions
--------------

    **Attributes:**

        | user_view_welcome: bool

        | decimal_separator: str

        | thousand_separator: str

        | last_whats_new: Optional[datetime]


.. _AccountOpt:

AccountOpt
----------

    **Attributes:**

        | authenticator: bool

        | sms: bool

        | email: bool


.. _AccountInfo:

AccountInfo
-----------

    **Attributes:**

        | active: bool

        | name: str

        | email: str

        | country: Optional[str]

        | timezone: str

        | company: Optional[str]

        | newsletter: Optional[bool]

        | developer: Optional[bool]

        | blocked: bool

        | id: :ref:`GenericID`

        | language: str

        | last_login: Optional[datetime]

        | options: :ref:`AccountOptions`

        | phone: Optional[str]

        | send_invoice: bool

        | stripe_id: Optional[str]

        | type: str

        | plan: str

        | created_at: datetime

        | updated_at: datetime

        | otp: Optional[:ref:`AccountOpt`]


.. _AccountCreateInfo:

AccountCreateInfo
-----------------

    Information required to create a new TagoIO account.

    **Attributes:**

        | name: str

        | email: str

        | password: str

        | cpassword: str

        | country: Optional[str]

        | timezone: str

        | company: Optional[str]

        | newsletter: Optional[bool]

        | developer: Optional[bool]


.. _OTPType:

OTPType
-------

    Type of One-Time Password authentication method.

    **Values:**

        | "sms" or "email" or "authenticator"


.. _TokenCreateInfo:

TokenCreateInfo
---------------

    Information required to create a new account token.

    **Attributes:**

        | profile_id: :ref:`GenericID`

        | email: str

        | password: str

        | pin_code: str

        | otp_type: :ref:`OTPType`

        | name: str


.. _LoginCredentials:

LoginCredentials
----------------

    Credentials required for account login.

    **Attributes:**

        | email: str

        | password: str

        | otp_type: :ref:`OTPType`

        | pin_code: str


.. _ProfileListInfoForLogin:

ProfileListInfoForLogin
-----------------------

    Profile information returned in login response.

    **Attributes:**

        | id: :ref:`GenericID`

        | name: str


.. _LoginResponse:

LoginResponse
-------------

    Response data from account login endpoint.

    **Attributes:**

        | type: str

        | id: :ref:`GenericID`

        | email: str

        | company: str

        | name: str

        | profiles: List[:ref:`ProfileListInfoForLogin`]
