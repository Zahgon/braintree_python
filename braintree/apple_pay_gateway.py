from urllib.parse import quote
from braintree.apple_pay_options import ApplePayOptions
from braintree.error_result import ErrorResult
from braintree.successful_result import SuccessfulResult
from braintree.exceptions.unexpected_error import UnexpectedError

class ApplePayGateway(object):
    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config

    def register_domain(self, domain):
        pass

    def unregister_domain(self, domain):
        pass

    def registered_domains(self):
        pass
