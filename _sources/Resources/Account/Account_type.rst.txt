**Account Type**
=================


.. _AccountOptions:

AccountOptions
--------------
    **Attributes:**

        | **user_view_welcome**: bool
        | **decimal_separator**: str
        | **thousand_separator**: str
        | **last_whats_new**: Optional[datetime]


.. _AccountOpt:

AccountOpt
-----------
    **Attributes:**

        | **authenticator**: bool
        | **sms**: bool
        | **email**: bool


.. _AccountInfo:

AccountInfo
-----------
    **Attributes:**

        | **active**: bool
        | **name**: str
        | **email**: str
        | **country**: Optional[str]
        | **timezone**: str
        | **company**: Optional[str]
        | **newsletter**: Optional[bool]
        | **developer**: Optional[bool]
        | **blocked**: bool
        | **id**: GenericID
        | **language**: str
        | **last_login**: Optional[datetime]
        | **options**: :ref:`AccountOptions`
        | **phone**: Optional[str]
        | **send_invoice**: bool
        | **stripe_id**: Optional[str]
        | **type**: str
        | **plan**: str
        | **created_at**: datetime
        | **updated_at**: datetime
        | **otp**: Optional[:ref:`AccountOpt`]
