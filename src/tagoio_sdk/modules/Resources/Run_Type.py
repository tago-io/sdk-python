from datetime import datetime
from typing import Dict
from typing import Literal
from typing import Optional
from typing import TypedDict
from typing import Union

from tagoio_sdk.common.Common_Type import ExpireTimeOption
from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.Common_Type import GenericToken
from tagoio_sdk.common.Common_Type import TagsObj


ThemeOption = Literal[
    "actionSchedule",
    "actionTriggerByData",
    "actionTriggerByResource",
    "actionTriggerByMQTT",
    "alertDangerBackground",
    "alertInfoBackground",
    "alertWarningBackground",
    "analysisExternal",
    "analysisInternal",
    "buttonDanger",
    "buttonDangerText",
    "buttonDefault",
    "buttonDefaultText",
    "buttonDisabled",
    "buttonDisabledText",
    "buttonIconLabel",
    "buttonPrimary",
    "buttonPrimaryText",
    "buttonSuccess",
    "buttonSuccessText",
    "buttonWarning",
    "buttonWarningText",
    "deviceInputOutput1Day",
    "deviceInputOutput3Days",
    "deviceInputOutput3Hours",
    "deviceInputOutput6Hours",
    "deviceInputOutputRest",
    "dottedBorder",
    "dropdownAccent",
    "dropdownBackground",
    "floatingSidebarTitle",
    "footerBackground",
    "formControlBorder",
    "gaugeEmpty",
    "gaugeFill",
    "gaugePrimaryText",
    "gaugeSecondaryText",
    "iconRadioSelected",
    "iconRadioSubTitle",
    "informationIcon",
    "inputBackground",
    "inputBackgroundReadOnly",
    "inputError",
    "inputForeground",
    "inputForegroundReadOnly",
    "lightBorder",
    "limitAlert",
    "link",
    "listNavColor",
    "listTitleLabel",
    "loading",
    "loginButton",
    "loginButtonText",
    "loginForeground",
    "loginForm",
    "modalContainer",
    "modalOverlay",
    "navbar",
    "navbarBetaDeveloperBorder",
    "navbarButton",
    "navbarDropdownBorder",
    "navbarDropdownOption",
    "navbarDropdownOptionBorder",
    "navbarText",
    "navDescription",
    "notificationButtonAmount",
    "notificationButtonAmountText",
    "notificationFilterBackground",
    "notificationFooter",
    "notificationItemBorder",
    "notificationItemDate",
    "notificationItemTextAccepted",
    "notificationItemUnread",
    "primary",
    "publicPageNavigationBar",
    "sidebarAccessSelected",
    "sidebarAccountSelected",
    "sidebarActionSelected",
    "sidebarAnalysisSelected",
    "sidebarBackground",
    "sidebarBillingSelected",
    "sidebarBucketSelected",
    "sidebarDashboardSelected",
    "sidebarDeviceSelected",
    "sidebarExploreSelected",
    "sidebarFileSelected",
    "sidebarForegroundIcon",
    "sidebarForegroundText",
    "sidebarHomeSelected",
    "sidebarItem",
    "sidebarRibbon",
    "sidebarRunSelected",
    "sidebarSeparator",
    "sidebarSeparatorForeground",
    "sidebarUserSelected",
    "snakeButtonOutline",
    "svgTagoFont",
    "svgTagoIOHole",
    "switchDisabledBackground",
    "switchSlider",
    "tabBackground",
    "tabLabelBorder",
    "tooltipContainer",
    "tooltipText",
    "verticalTabItem",
    "verticalTabItemBorder",
    "widgetCardBackground",
    "widgetIconsAccent",
    "widgetIconsBackground",
    "widgetIconsColor",
    "widgetIconsFooterBasic",
    "widgetIconsFooterPremium",
    "auth_bg_opacity",
    "auth_bg_src",
    "auth_bg_type",
    "auth_form_opacity",
]


class sidebar_buttons(TypedDict):
    color: str
    href: str
    iconUrl: str
    text: str
    type: str


class signup_fields(TypedDict):
    name: str
    placeholder: str
    required: bool
    type: str


class feature_devicewifisetup(TypedDict):
    background_color: str
    button_cancel_background_color: str
    button_cancel_text_color: str
    button_confirm_background_color: str
    button_confirm_text_color: str
    enabled: bool
    ip: str
    language: str
    name: str
    port: str
    protocol: str
    text_color: str
    translations: Dict[str, object]


class email_templates(TypedDict):
    subject: str
    value: str


class feature_geolocation(TypedDict):
    buffer_size: Union[int, float]
    device: Union[str, None]
    enabled: bool
    middleware_url: str
    minimum_distance: Union[int, float]
    minimum_interval: Union[int, float]
    target: str


class otp(TypedDict):
    authenticator: bool
    sms: bool
    email: bool


class RunInfo(TypedDict):
    profile: GenericID
    active: bool
    name: str
    sub_title: str
    url: str
    email_domain: Union[str, None]
    signup_method: str
    favicon: Union[str, None]
    logo: Union[str, None]
    signup_logo: Union[str, None]
    signup_logo_options: object
    sidebar_buttons: list[sidebar_buttons]
    signup_fields: list[signup_fields]
    email_templates: Dict[str, email_templates]
    feature_devicewifisetup: feature_devicewifisetup
    feature_geolocation: feature_geolocation
    theme: ThemeOption
    integration: object
    sso_saml_active: bool
    security: Dict[str, otp]


class UserCreateInfo(TypedDict):
    name: str
    email: str
    password: str
    timezone: str
    company: Optional[str]
    phone: Optional[str]
    language: Optional[str]
    tags: Optional[list[TagsObj]]
    active: Optional[bool]


class UserInfo(TypedDict):
    name: str
    email: str
    timezone: str
    company: Optional[str]
    phone: Optional[str]
    language: Optional[str]
    tags: Optional[list[TagsObj]]
    active: Optional[bool]
    id: GenericID
    profile: GenericID
    active: bool
    newsletter: bool
    last_login: Union[datetime, None]
    created_at: datetime
    updated_at: datetime
    options: object
    tags: list[TagsObj]


class LoginResponse(TypedDict):
    token: GenericToken
    expire_date: ExpireTimeOption


class LoginAsUserOptions(TypedDict):
    expire_time: Optional[str]
    """
    Date to expire the login token.

    :example:
    3 months", "1 year", "20 hours"

    :default: "8 hours"
    """


class SAMLAttributeMappings(TypedDict):
    email: str
    firstName: str
    lastName: Optional[str]
    phone: Optional[str]
    company: Optional[str]
    language: Optional[str]
    timezone: Optional[str]
    tags: Dict[str, str]


class sp(TypedDict):
    entity_id: str
    acs_url: str
    metadata: str


class idp(TypedDict):
    issuer: str


class RunSAMLInfo(TypedDict):
    sp: sp
    """
    Information for TagoIO's API routes to use as a Service Provider in SAML authentication flows.
    """

    idp: idp
    """
    Relevant information from the Identity Provider's metadata after being parsed by TagoIO.
    """

    mapping: SAMLAttributeMappings
    """
    Attribute mappings for the Identity Provider's attributes to the attributes used in TagoIO.
    """


class RunSAMLEditInfo(TypedDict):
    idp_metadata: Optional[str]
    """
    Identity Provider's XML metadata encoded in a base 64 string.
    """

    mapping: SAMLAttributeMappings
    """
    Attribute mappings for the Identity Provider's attributes to the attributes used in TagoIO.
    """


class CustomDomainDnsRecord(TypedDict):
    status: bool
    """
    Status for the DNS record check.

    When `true`, the DNS record is properly configured with the provided key and value.
    When `false`, the DNS record is either not yet configured or the `key` exists but the
    value in the DNS record does not match the `value` provided.
    """

    type: str
    """
    Type of the DNS record.
    """

    key: str
    """
    Key for key-value pair in the DNS record.
    """

    value: str
    """
    Value for the key-value pair the DNS record.
    """

    current_value: Optional[str]
    """
    Current value in the provider's record for the DNS record's `key`.

    Only returned when the DNS record has the matching `key` configured.

    When `status` is `true`, the value here will be the same as the one in `value`.
    When `status` is `false`, the value here can is either stale or there was an error
    opying the provided `value` in the DNS provider's record.
    """


class CustomDomainResponse(TypedDict):
    """
    Type for the Custom Domain response from the API, unparsed.

    :internal
    """

    active: bool
    """
    Whether the custom domain is active.

    This is only `true` when all the required DNS records are properly configured in the DNS
    provider.
    """

    domain: str
    """
    Configured domain for the RUN.
    """

    subdomain: str
    """
    Configured subdomain for the RUN.
    """

    email: str
    """
    Mailing address for the RUN with custom domain.
    """

    dns_ssl: CustomDomainDnsRecord
    """
    DNS record for the SSL certificate.
    The information in this record needs to be configured in the DNS provider for the custom domain.
    """

    dns_page: CustomDomainDnsRecord
    """
    DNS record for the page endpoint.

    The information in this record needs to be configured in the DNS provider for the custom domain.
    """

    dns_email_1: CustomDomainDnsRecord
    """
    First DNS record for the e-mail.

    The information in this record needs to be configured in the DNS provider for the custom domain.
    """

    dns_email_2: CustomDomainDnsRecord
    """
    Second DNS record for the e-mail.

    The information in this record needs to be configured in the DNS provider for the custom domain.
    """

    dns_email_3: CustomDomainDnsRecord
    """
    Third DNS record for the e-mail.

    The information in this record needs to be configured in the DNS provider for the custom domain.
    """

    created_at: str
    """
    Timestamp (in string format) for when the custom domain was configured.
    """


class CustomDomainInfo(TypedDict):
    """
    Type for the Custom Domain information in a profile's RUN.
    """

    active: bool
    """
    Whether the custom domain is active.

    This is only `true` when all the required DNS records are properly configured in the DNS
    provider.
    """

    domain: str
    """
    Configured domain for the RUN.
    """

    subdomain: str
    """
    Configured subdomain for the RUN.
    """

    email: str
    """
    Mailing address for the RUN with custom domain.
    """

    dns_ssl: CustomDomainDnsRecord
    """
    DNS record for the SSL certificate.
    The information in this record needs to be configured in the DNS provider for the custom domain.
    """

    dns_page: CustomDomainDnsRecord
    """
    DNS record for the page endpoint.

    The information in this record needs to be configured in the DNS provider for the custom domain.
    """

    dns_email_1: CustomDomainDnsRecord
    """
    First DNS record for the e-mail.

    The information in this record needs to be configured in the DNS provider for the custom domain.
    """

    dns_email_2: CustomDomainDnsRecord
    """
    Second DNS record for the e-mail.

    The information in this record needs to be configured in the DNS provider for the custom domain.
    """

    dns_email_3: CustomDomainDnsRecord
    """
    Third DNS record for the e-mail.

    The information in this record needs to be configured in the DNS provider for the custom domain.
    """

    created_at: datetime
    """
    Timestamp for when the custom domain was configured.
    """


class CustomDomainCreate(TypedDict):
    """
    Type for the data required to configure a profile's RUN Custom Domain.
    """

    domain: str
    """
    Domain for the RUN's custom domain.

    If the desired custom domain is `portal.mycompany.com`, this will be `"mycompany.com"`.
    """

    subdomain: str
    """
    Subdomain for the RUN's custom domain.

    If the desired custom domain is `portal.mycompany.com`, this will be `"portal"`.
    """

    email: str
    """
    Mailing address for the RUN with custom domain.

    If the desired custom domain is `portal.mycompany.com`, this can be either
    `"portal.mycompany.com"` or `"mycompany.com"`.
    """
