**Billing Type**
=================

.. _BillingPlan:

BillingPlan
------------

    **BillingPlan** = "free" or "starter" or "scale"

.. _BillingAddOn:

BillingAddOn
-------------

    **BillingAddOn** = "mobile" or "custom_dns"


.. _BillingService:

BillingService
---------------

    **BillingService** =
        "input" or
        "output"or
        "analysis"or
        "data_records" or
        "sms" or
        "email" or
        "run_users" or
        "push_notification" or
        "file_storage"


.. _BillingServicePrice:

BillingServicePrice
-------------------

    **Attributes:**

        | **amount**: int or float
        | Amount available in the service tier.

        | **price**: int or float
        | Price for the service tier.


.. _BillingAllServicePrices:

BillingAllServicePrices
------------------------

    **BillingAllServicePrices** = dict[:ref:`BillingService`, list[:ref:`BillingServicePrice`]]


.. _BillingPlanPricesItem:

BillingPlanPrices
------------------

    **Attributes:**

        | **name**: :ref:`BillingPlan`
        | Plan name.

        | **price**: int or float
        | Plan price.



.. _BillingPlanPricesList:

BillingPlanPrices
------------------

    **BillingPlanPrices** = list[:ref:`BillingPlanPricesItem`]



.. _BillingAddOnPricesItem:

BillingAddOnPrices
------------------

    **Attributes:**

        | **name**: :ref:`BillingAddOn`
        | Add-on name.

        | **price**: int or float
        | Add-on price.


.. _BillingAddOnPricesList:

BillingAddOnPrices
------------------

    **BillingAddOnPrices** = list[:ref:`BillingAddOnPricesItem`]


.. _BillingPrices:

BillingPrices
-------------

    **Attributes:**

        | **plans**: :ref:`BillingPlanPricesList`
        | Prices for each plan.

        | **addons**: :ref:`BillingAddOnPricesList`
        | Prices for each add-on.

        **BillingAllServicePrices**: :ref:`BillingAllServicePrices`


.. _current_cycle:

current_cycle
--------------

    **Attributes:**

        | **start**: str
        | Date when the current cycle started.

        | **end**: str
        | Date when the current cycle ends.


.. _BillingServiceSubscription:

BillingServiceSubscription
--------------------------

    **Attributes:**

        limit: int or float


.. _BillingSubscriptionServices:

BillingSubscriptionServices
----------------------------

    **BillingSubscriptionServices** = dict[BillingService, BillingServiceSubscription]


.. _BillingSubscriptionAddOns:

BillingSubscriptionAddOns
--------------------------

    **BillingSubscriptionAddOns** = dict[BillingAddOn, list[GenericID]]



.. _BillingPaymentError:

BillingPaymentError
-------------------

    **Attributes:**

        | **message**: str or None
        | Payment error message.

        | **details**: str or None
        | More details on the payment error.


.. _BillingPaymentPastDue:

BillingPaymentPastDue
-----------------------

    **Attributes:**

        | **amount_due**: int or float
        | Amount due that was not paid in a recurring payment.

        | **attempt_count**: int or float
        | Amount of attempts for the retried recurring payment.

        | **invoice_url**: str
        | URL for the invoice related to the failed recurring payment.


.. _BillingSubscription:

BillingSubscription
--------------------

    **Attributes:**

        | **account**: :ref:`GenericID`
        | Account ID.

        | **plan**: :ref:`BillingPlan`
        | Account plan.

        | **services**: :ref:`BillingSubscriptionServices`
        | Limits for each service in the account's subscription.

        | **addons**: :ref:`BillingSubscriptionAddOns`
        | Add-ons in the account's subscription.

        | **current_cycle**: :ref:`current_cycle`
        | Current cycle for the account's subscription.

        | **processing**: bool
        | Whether changes are still being processed and awaiting response from Stripe.

        | **payment_error**: Optional[:ref:`BillingPaymentError`]
        | Payment errors in the account's subscription.

        | **past_due**: Optional[:ref:`BillingPaymentPastDue`]
        | Past due information for recurring payment errors.

        | **upcoming_invoice_total**: int or float
        | Value of the upcoming invoice.

        | **trial_end**: str or None
        | Timestamp when the trial for the subscription ends if the subscription has a trial active.


.. _BillingEditSubscription:

BillingEditSubscription
------------------------

    **Attributes:**

        | **plan**: Optional[:ref:`BillingPlan`]
        | New account plan.
        | Only one of `plan`, `services` and `addons` is accepted.

        | **services**: Optional[:ref:`BillingSubscriptionServices`]
        | New limits for each service in the account's subscription.
        | Only one of `plan`, `services` and `addons` is accepted.

        | **addons**: Optional[:ref:`BillingSubscriptionAddOns`]
        | Only one of `plan`, `services` and `addons` is accepted.
        | New add-ons in the account's subscription.

        | **coupon**: Optional[str]
        | Coupon code.


.. _BillingResourceAllocationServices:

BillingResourceAllocationServices
-----------------------------------

    **BillingResourceAllocationServices** = dict[BillingService, Union[int, float]]


.. _BillingProfileResourceAllocation:

BillingProfileResourceAllocation
---------------------------------

    **Attributes:**

        | **profile**: :ref:`GenericID`
        | Profile ID.

        | **updated_at**: str
        | Timestamp when the resource allocation for the profile was last updated.

        **BillingResourceAllocationServices**: :ref:`BillingResourceAllocationServices`


.. _BillingProfileEditResourceAllocation:

BillingProfileEditResourceAllocation
-------------------------------------

    **Attributes:**

        | **profile**: Optional[:ref:`GenericID`]
        | Profile ID.

        **BillingResourceAllocationServices**: Optional[:ref:`BillingResourceAllocationServices`]


.. _BillingEditResourceAllocation:

BillingEditResourceAllocation
------------------------------

    **BillingEditResourceAllocation** = list[:ref:`BillingProfileEditResourceAllocation`]


