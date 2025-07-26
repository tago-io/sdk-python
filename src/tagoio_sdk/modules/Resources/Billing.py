from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Resources.Billing_Type import BillingEditResourceAllocation
from tagoio_sdk.modules.Resources.Billing_Type import BillingEditSubscription
from tagoio_sdk.modules.Resources.Billing_Type import BillingPrices
from tagoio_sdk.modules.Resources.Billing_Type import BillingSubscription


class Billing(TagoIOModule):
    def getPrices(self) -> BillingPrices:
        """
        Get pricing for plans, services and add-ons.
        """
        result = self.doRequest(
            {
                "path": "/pricing",
                "method": "GET",
            }
        )
        return result

    def getSubscription(self) -> BillingSubscription:
        """
        Get the account subscription information.
        """
        result = self.doRequest(
            {
                "path": "/account/subscription",
                "method": "GET",
            }
        )
        return result

    def editSubscription(self, subscription: BillingEditSubscription) -> None:
        """
        Edit an account's subscription to change plan, services or add-ons.

        Only one of either `plan`, `services`, or `addons` can be in `subscription`.

        :param BillingEditSubscription subscription: Object with updates to subscription.

        :throws: If the subscription has a pending operation.
        :throws: If updating more than one of plan, services and add-ons at the same time.
        :throws: If purchasing add-ons or changing service limits on the Free plan.
        :throws: If using an invalid coupon.
        """
        result = self.doRequest(
            {
                "path": "/account/subscription",
                "method": "POST",
                "body": subscription,
            }
        )
        return result

    def editAllocation(self, allocation: BillingEditResourceAllocation) -> str:
        """
        Edit the resource allocation for the profiles in an account.

        The resource allocation array doesn't need to have an object for
        each of the account's profiles,
        as long as the sum of the allocated amounts for the services doesn't
        exceed the account's service limit.

        The resource allocation object for a profile doesn't need to have all the services.

        :param BillingEditResourceAllocation allocation: Array with the resource allocation

        :throws: If passed an object that is not an allocation array.
        :throws: If the account only has one profile.
        :throws: If one of the profile IDs in the allocation array doesn't exist in the account.
        :throws: If the allocated amount for one of the services exceeds the available amount.

        :returns: Success message.
        """

        result = self.doRequest(
            {
                "path": "/account/allocation",
                "method": "POST",
                "body": allocation,
            }
        )
        return result
