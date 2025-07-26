from typing import Literal
from typing import Optional
from typing import TypedDict
from typing import Union

from tagoio_sdk.common.Common_Type import GenericID


BillingPlan = Literal["free", "starter", "scale"]

BillingAddOn = Literal["mobile", "custom_dns"]

BillingService = Literal[
    "input",
    "output",
    "analysis",
    "data_records",
    "sms",
    "email",
    "run_users",
    "push_notification",
    "file_storage",
]


class BillingServicePrice(TypedDict):
    amount: Union[int, float]
    """
    Amount available in the service tier.
    """
    price: Union[int, float]
    """
    Price for the service tier.
    """


BillingAllServicePrices = dict[BillingService, list[BillingServicePrice]]


class BillingPlanPrices(TypedDict):
    name: BillingPlan
    """
    Plan name.
    """
    price: Union[int, float]
    """
    Plan price.
    """


BillingPlanPrices = list[BillingPlanPrices]


class BillingAddOnPrices(TypedDict):
    name: BillingAddOn
    """
    Add-on name.
    """
    price: Union[int, float]
    """
    Add-on price.
    """


BillingAddOnPrices = list[BillingAddOnPrices]


class BillingPrices(TypedDict):
    plans: BillingPlanPrices
    """
    Prices for each plan.
    """
    addons: BillingAddOnPrices
    """
    Prices for each add-on.
    """
    BillingAllServicePrices: BillingAllServicePrices


class current_cycle(TypedDict):
    start: str
    """
    Date when the current cycle started.
    """
    end: str
    """
    Date when the current cycle ends.
    """


class BillingServiceSubscription(TypedDict):
    limit: Union[int, float]


BillingSubscriptionServices = dict[BillingService, BillingServiceSubscription]

BillingSubscriptionAddOns = dict[BillingAddOn, list[GenericID]]


class BillingPaymentError(TypedDict):
    message: Union[str, None]
    """
    Payment error message.
    """
    details: Union[str, None]
    """
    More details on the payment error.
    """


class BillingPaymentPastDue(TypedDict):
    amount_due: Union[int, float]
    """
    Amount due that was not paid in a recurring payment.
    """
    attempt_count: Union[int, float]
    """
    Amount of attempts for the retried recurring payment.
    """
    invoice_url: str
    """
    URL for the invoice related to the failed recurring payment.
    """


class BillingSubscription(TypedDict):
    account: GenericID
    """
    Account ID.
    """
    plan: BillingPlan
    """
    Account plan.
    """
    services: BillingSubscriptionServices
    """
    Limits for each service in the account's subscription.
    """
    addons: BillingSubscriptionAddOns
    """
    Add-ons in the account's subscription.
    """
    current_cycle: current_cycle
    """
    Current cycle for the account's subscription.
    """
    processing: bool
    """
    Whether changes are still being processed and awaiting response from Stripe.
    """
    payment_error: Optional[BillingPaymentError]
    """
    Payment errors in the account's subscription.
    """
    past_due: Optional[BillingPaymentPastDue]
    """
    Past due information for recurring payment errors.
    """
    upcoming_invoice_total: Union[int, float]
    """
    Value of the upcoming invoice.
    """
    trial_end: Union[str, None]
    """
    Timestamp when the trial for the subscription ends if the subscription has a trial active.
    """


class BillingEditSubscription(TypedDict):
    plan: Optional[BillingPlan]
    """
    New account plan.

    Only one of `plan`, `services` and `addons` is accepted.
    """
    services: Optional[BillingSubscriptionServices]
    """
    New limits for each service in the account's subscription.

    Only one of `plan`, `services` and `addons` is accepted.
    """
    addons: Optional[BillingSubscriptionAddOns]
    """
    Only one of `plan`, `services` and `addons` is accepted.
    New add-ons in the account's subscription.
    """
    coupon: Optional[str]
    """
    Coupon code.
    """


BillingResourceAllocationServices = dict[BillingService, Union[int, float]]


class BillingProfileResourceAllocation(TypedDict):
    profile: GenericID
    """
    Profile ID.
    """
    updated_at: str
    """
    Timestamp when the resource allocation for the profile was last updated.
    """
    BillingResourceAllocationServices: BillingResourceAllocationServices


class BillingProfileEditResourceAllocation(TypedDict):
    profile: Optional[GenericID]
    """
    Profile ID.
    """
    BillingResourceAllocationServices: Optional[BillingResourceAllocationServices]


BillingEditResourceAllocation = list[BillingProfileEditResourceAllocation]
