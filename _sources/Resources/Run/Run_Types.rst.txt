**Run Type**
=================


.. _ThemeOption:

ThemeOption
-------------

**ThemeOption** =
    | "actionSchedule" or
    | "actionTriggerByData" or
    | "actionTriggerByResource" or
    | "actionTriggerByMQTT" or
    | "alertDangerBackground" or
    | "alertInfoBackground" or
    | "alertWarningBackground" or
    | "analysisExternal" or
    | "analysisInternal" or
    | "buttonDanger" or
    | "buttonDangerText" or
    | "buttonDefault" or
    | "buttonDefaultText" or
    | "buttonDisabled" or
    | "buttonDisabledText" or
    | "buttonIconLabel" or
    | "buttonPrimary" or
    | "buttonPrimaryText" or
    | "buttonSuccess" or
    | "buttonSuccessText" or
    | "buttonWarning" or
    | "buttonWarningText" or
    | "deviceInputOutput1Day" or
    | "deviceInputOutput3Days" or
    | "deviceInputOutput3Hours" or
    | "deviceInputOutput6Hours" or
    | "deviceInputOutputRest" or
    | "dottedBorder" or
    | "dropdownAccent" or
    | "dropdownBackground" or
    | "floatingSidebarTitle" or
    | "footerBackground" or
    | "formControlBorder" or
    | "gaugeEmpty" or
    | "gaugeFill" or
    | "gaugePrimaryText" or
    | "gaugeSecondaryText" or
    | "iconRadioSelected" or
    | "iconRadioSubTitle" or
    | "informationIcon" or
    | "inputBackground" or
    | "inputBackgroundReadOnly" or
    | "inputError" or
    | "inputForeground" or
    | "inputForegroundReadOnly" or
    | "lightBorder" or
    | "limitAlert" or
    | "link" or
    | "listNavColor" or
    | "listTitleLabel" or
    | "loading" or
    | "loginButton" or
    | "loginButtonText" or
    | "loginForeground" or
    | "loginForm" or
    | "modalContainer" or
    | "modalOverlay" or
    | "navbar" or
    | "navbarBetaDeveloperBorder" or
    | "navbarButton" or
    | "navbarDropdownBorder" or
    | "navbarDropdownOption" or
    | "navbarDropdownOptionBorder" or
    | "navbarText" or
    | "navDescription" or
    | "notificationButtonAmount" or
    | "notificationButtonAmountText" or
    | "notificationFilterBackground" or
    | "notificationFooter" or
    | "notificationItemBorder" or
    | "notificationItemDate" or
    | "notificationItemTextAccepted" or
    | "notificationItemUnread" or
    | "primary" or
    | "publicPageNavigationBar" or
    | "sidebarAccessSelected" or
    | "sidebarAccountSelected" or
    | "sidebarActionSelected" or
    | "sidebarAnalysisSelected" or
    | "sidebarBackground" or
    | "sidebarBillingSelected" or
    | "sidebarBucketSelected" or
    | "sidebarDashboardSelected" or
    | "sidebarDeviceSelected" or
    | "sidebarExploreSelected" or
    | "sidebarFileSelected" or
    | "sidebarForegroundIcon" or
    | "sidebarForegroundText" or
    | "sidebarHomeSelected" or
    | "sidebarItem" or
    | "sidebarRibbon" or
    | "sidebarRunSelected" or
    | "sidebarSeparator" or
    | "sidebarSeparatorForeground" or
    | "sidebarUserSelected" or
    | "snakeButtonOutline" or
    | "svgTagoFont" or
    | "svgTagoIOHole" or
    | "switchDisabledBackground" or
    | "switchSlider" or
    | "tabBackground" or
    | "tabLabelBorder" or
    | "tooltipContainer" or
    | "tooltipText" or
    | "verticalTabItem" or
    | "verticalTabItemBorder" or
    | "widgetCardBackground" or
    | "widgetIconsAccent" or
    | "widgetIconsBackground" or
    | "widgetIconsColor" or
    | "widgetIconsFooterBasic" or
    | "widgetIconsFooterPremium" or
    | "auth_bg_opacity" or
    | "auth_bg_src" or
    | "auth_bg_type" or
    | "auth_form_opacity"


.. _sidebar_buttons:

sidebar_buttons
-----------------
    **Attributes:**

        | **color**: str
        | **href**: str
        | **iconUrl**: str
        | **text**: str
        | **type**: str



.. _signup_fields:

signup_fields
--------------

    **Attributes:**

        | **name**: str
        | **placeholder**: str
        | **required**: bool
        | **type**: str


.. _feature_devicewifisetup:

feature_devicewifisetup
-----------------------

    **Attributes:**

        | **background_color**: str
        | **button_cancel_background_color**: str
        | **button_cancel_text_color**: str
        | **button_confirm_background_color**: str
        | **button_confirm_text_color**: str
        | **enabled**: bool
        | **ip**: str
        | **language**: str
        | **name**: str
        | **port**: str
        | **protocol**: str
        | **text_color**: str
        | **translations**: Dict[str, object]



.. _email_templates:

email_templates
---------------

    **Attributes:**

        | **subject**: str
        | **value**: str

.. _TypedDict:

TypedDict
---------

    **Attributes:**

        | **subject**: str
        | **value**: str

.. _feature_geolocation:

feature_geolocation
-------------------

    **Attributes:**

        | **buffer_size**: Union[int, float]
        | **device**: Union[str, None]
        | **enabled**: bool
        | **middleware_url**: str
        | **minimum_distance**: Union[int, float]
        | **minimum_interval**: Union[int, float]
        | **target**: str


.. _otp:

otp
---

    **Attributes:**

        | **authenticator**: bool
        | **sms**: bool
        | **email**: bool


.. _RunInfo:

RunInfo
-------

    **Attributes:**

        | **profile**: GenericID
        | **active**: bool
        | **name**: str
        | **sub_title**: str
        | **url**: str
        | **email_domain**: Union[str, None]
        | **signup_method**: str
        | **favicon**: Union[str, None]
        | **logo**: Union[str, None]
        | **signup_logo**: Union[str, None]
        | **signup_logo_options**: object
        | **sidebar_buttons**: list[sidebar_buttons]
        | **signup_fields**: list[signup_fields]
        | **email_templates**: Dict[str, email_templates]
        | **feature_devicewifisetup**: feature_devicewifisetup
        | **feature_geolocation**: feature_geolocation
        | **theme**: ThemeOption
        | **integration**: object
        | **sso_saml_active**: bool
        | **security**: Dict[str, otp]

.. _UserCreateInfo:

UserCreateInfo
--------------

    **Attributes:**

        | **name**: str
        | **email**: str
        | **password****: str
        | **timezone**: str
        | **company**: Optional[str]
        | **phone**: Optional[str]
        | **language**: Optional[str]
        | **tags**: Optional[list[:ref:`TagsObj`]]
        | **active**: Optional[bool]

.. _UserInfo:

UserInfo
--------

    **Attributes:**

        | **name**: str
        | **email**: str
        | **timezone**: str
        | **company**: Optional[str]
        | **phone**: Optional[str]
        | **language**: Optional[str]
        | **tags**: Optional[list[:ref:`TagsObj`]]
        | **active**: Optional[bool]
        | **id**: GenericID
        | **profile**: GenericID
        | **active**: bool
        | **newsletter**: bool
        | **last_login**: Union[datetime, None]
        | **created_at**: datetime
        | **updated_at**: datetime
        | **options**: object
        | **tags**: list[:ref:`TagsObj`]

.. _LoginResponse:

LoginResponse
-------------

    **Attributes:**

        | **token**: GenericToken
        | **expire_date**: ExpireTimeOption

.. _LoginAsUserOptions:

LoginAsUserOptions
------------------

    **Attributes:**

        | **expire_time**: Optional[str]
        | Date to expire the login token.

    **example:**
        | "3 months", "1 year", "20 hours"
        | :default: "8 hours"



.. _SAMLAttributeMappings:

SAMLAttributeMappings
---------------------

    **Attributes:**

        | **email**: str
        | **firstName**: str
        | **lastName**: Optional[str]
        | **phone**: Optional[str]
        | **company**: Optional[str]
        | **language**: Optional[str]
        | **timezone**: Optional[str]
        | **tags**: Dict[str, str]

.. _sp:

sp
---

    **Attributes:**

        | **entity_id**: str
        | **acs_url**: str
        | **metadata**: str

.. _idp:

idp
---

    **Attributes:**
        | **issuer**: str

.. _RunSAMLInfo:

RunSAMLInfo
-----------

    **Attributes:**

        | **sp**: sp
        | Information for TagoIO's API routes to use as a Service Provider in SAML authentication flows.

        | **idp**: idp
        | Relevant information from the Identity Provider's metadata after being parsed by TagoIO.

        | **mapping**: SAMLAttributeMappings
        | Attribute mappings for the Identity Provider's attributes to the attributes used in TagoIO.


.. _RunSAMLEditInfo:

RunSAMLEditInfo
---------------

    **Attributes:**

        | **idp_metadata**: Optional[str]
        | Identity Provider's XML metadata encoded in a base 64 string.

        | **mapping**: SAMLAttributeMappings
        | Attribute mappings for the Identity Provider's attributes to the attributes used in TagoIO.

.. _CustomDomainDnsRecord:

CustomDomainDnsRecord
---------------------

    **Attributes:**

        | **status**: bool

        | Status for the DNS record check.

        | When `true`, the DNS record is properly configured with the provided key and value.
        | When `false`, the DNS record is either not yet configured or the `key` exists but the
        | value in the DNS record does not match the `value` provided.

        | **type**: str
        | Type of the DNS record.

        | **key**: str
        | Key for key-value pair in the DNS record.

        | **value**: str
        | Value for the key-value pair the DNS record.

        | **current_value**: Optional[str]
        | Current value in the provider's record for the DNS record's `key`.
        | Only returned when the DNS record has the matching `key` configured.

        | When `status` is `true`, the value here will be the same as the one in `value`.
        | When `status` is `false`, the value here can is either stale or there was an error
        | copying the provided `value` in the DNS provider's record.


.. _CustomDomainResponse:

CustomDomainResponse
--------------------

    **Attributes:**

        | Type for the Custom Domain response from the API, unparsed.

        | :internal

        | **active**: bool
        | Whether the custom domain is active.

        | This is only `true` when all the required DNS records are properly configured in the DNS provider.

        | **domain**: str
        | Configured domain for the RUN.

        | **subdomain**: str
        | Configured subdomain for the RUN.

        | **email**: str
        | Mailing address for the RUN with custom domain.

        | **dns_ssl**: CustomDomainDnsRecord
        | DNS record for the SSL certificate.
        | The information in this record needs to be configured in the DNS provider for the custom domain.

        | **dns_page**: CustomDomainDnsRecord
        | DNS record for the page endpoint.

        | The information in this record needs to be configured in the DNS provider for the custom domain.

        | **dns_email_1**: CustomDomainDnsRecord
        | First DNS record for the e-mail.

        | The information in this record needs to be configured in the DNS provider for the custom domain.

        | **dns_email_2**: CustomDomainDnsRecord
        | Second DNS record for the e-mail.

        | The information in this record needs to be configured in the DNS provider for the custom domain.

        | **dns_email_3**: CustomDomainDnsRecord
        | Third DNS record for the e-mail.

        | The information in this record needs to be configured in the DNS provider for the custom domain.

        | **created_at**: str
        | Timestamp (in string format) for when the custom domain was configured.


.. _CustomDomainInfo:

CustomDomainInfo
----------------

    **Attributes:**

        | Type for the Custom Domain information in a profile's RUN.

        | **active**: bool
        | Whether the custom domain is active.
        | This is only `true` when all the required DNS records are properly configured in the DNS
        | provider.

        | **domain**: str
        | Configured domain for the RUN.

        | **subdomain**: str
        | Configured subdomain for the RUN.

        | **email**: str
        | Mailing address for the RUN with custom domain.

        | **dns_ssl**: CustomDomainDnsRecord
        | DNS record for the SSL certificate.
        | The information in this record needs to be configured in the DNS provider for the custom domain.

        | **dns_page**: CustomDomainDnsRecord
        | DNS record for the page endpoint.

        | The information in this record needs to be configured in the DNS provider for the custom domain.

        | **dns_email_1**: CustomDomainDnsRecord
        | First DNS record for the e-mail.

        | The information in this record needs to be configured in the DNS provider for the custom domain.

        | **dns_email_2**: CustomDomainDnsRecord
        | Second DNS record for the e-mail.

        | The information in this record needs to be configured in the DNS provider for the custom domain.

        | **dns_email_3**: CustomDomainDnsRecord
        | Third DNS record for the e-mail.

        | The information in this record needs to be configured in the DNS provider for the custom domain.

        | **created_at**: datetime
        | Timestamp for when the custom domain was configured.

.. _customdomaincreate:

CustomDomainCreate
------------------

Type for the data required to configure a profile's RUN Custom Domain.

        **Attributes:**

            | **domain**: str
            | Domain for the RUN's custom domain.

            | If the desired custom domain is `portal.mycompany.com`, this will be `"mycompany.com"`.

            | **subdomain**: str
            | Subdomain for the RUN's custom domain.
            | If the desired custom domain is `portal.mycompany.com`, this will be `"portal"`.

            | **email**: str
            | Mailing address for the RUN with custom domain.
            | If the desired custom domain is `portal.mycompany.com`, this can be either `"portal.mycompany.com"` or `"mycompany.com"`.
