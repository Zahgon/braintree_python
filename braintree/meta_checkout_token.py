import braintree
from braintree.address import Address
from braintree.resource import Resource

class MetaCheckoutToken(Resource):
    def __init__(self, gateway, attributes):
        Resource.__init__(self, gateway, attributes)

    @property
    def expiration_date(self):
        pass

    @property
    def masked_number(self):
        pass
