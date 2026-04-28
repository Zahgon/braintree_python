import braintree
from braintree.discount import Discount
from braintree.resource_collection import ResourceCollection

class DiscountGateway(object):
    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config

    def all(self):
        pass
