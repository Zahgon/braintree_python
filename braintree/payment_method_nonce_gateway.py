import braintree
from braintree.payment_method_nonce import PaymentMethodNonce

from braintree.error_result import ErrorResult
from braintree.exceptions.not_found_error import NotFoundError
from braintree.resource import Resource
from braintree.resource_collection import ResourceCollection
from braintree.successful_result import SuccessfulResult

class PaymentMethodNonceGateway(object):
    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config

    def create(self, payment_method_token, params = {"payment_method_nonce": {}}):
        pass

    def find(self, payment_method_nonce):
        pass

    def _parse_payment_method_nonce(self, response):
        pass
