**Billing**
===========

Manage Billing for the account.

=========
getPrices
=========

Get pricing for plans, services and add-ons.

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.billing.getPrices()

===============
getSubscription
===============

Get the account subscription information.

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.billing.getSubscription()

================
editSubscription
================

Get data from TagoIO Device.

    **Parameters:**

        | **subscription**: :ref:`BillingEditSubscription`
        | Object with updates to subscription

    :throws: If the subscription has a pending operation.
    :throws: If updating more than one of plan, services and add-ons at the same time.
    :throws: If purchasing add-ons or changing service limits on the Free plan.
    :throws: If using an invalid coupon.



================
editAllocation
================

    Edit the resource allocation for the profiles in an account.

    The resource allocation array doesn't need to have an object for each of the account's profiles, as long as the sum of the allocated amounts for the services doesn't exceed the account's service limit.

    The resource allocation object for a profile doesn't need to have all the services.

    **Parameters:**

        | **allocation**: :ref:`BillingEditResourceAllocation`
        | Array with the resource allocation

    :throws: If passed an object that is not an allocation array.
    :throws: If the account only has one profile.
    :throws: If one of the profile IDs in the allocation array doesn't exist in the account.
    :throws: If the allocated amount for one of the services exceeds the available amount.

    :returns: Success message.


.. toctree::

    Billing_Type
