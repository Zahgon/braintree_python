import braintree
from braintree.address import Address
from braintree.resource import Resource
from warnings import warn

class MasterpassCard(Resource):
    """
    A class representing Masterpass card. Deprecated
    """
    def __init__(self, gateway, attributes):
        warn("MasterpassCard is deprecated")
        Resource.__init__(self, gateway, attributes)

        if "billing_address" in attributes:
            self.billing_address = Address(gateway, self.billing_address)
        else:
            self.billing_address = None

        if "subscriptions" in attributes:
            self.subscriptions = [braintree.subscription.Subscription(gateway, subscription) for subscription in self.subscriptions]

    @property
    def expiration_date(self):
        pass

    @property
    def masked_number(self):
        pass

