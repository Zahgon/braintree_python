import braintree
from braintree.address import Address
from braintree.resource import Resource

# NEXT_MAJOR_VERSION remove this class
# SamsungPay is deprecated
class SamsungPayCard(Resource):
    def __init__(self, gateway, attributes):
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
