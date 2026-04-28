from braintree.error_result import ErrorResult
from braintree.resource import Resource
from braintree.resource_collection import ResourceCollection
from braintree.successful_result import SuccessfulResult
from braintree.exceptions.not_found_error import NotFoundError
from braintree.merchant import Merchant
from braintree.oauth_credentials import OAuthCredentials


class MerchantGateway(object):
    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config

    def create(self, params):
        pass

    def __create_merchant(self, params=None):
        pass

