import warnings
from braintree.error_result import ErrorResult
from braintree.merchant_account import MerchantAccount
from braintree.paginated_collection import PaginatedCollection
from braintree.paginated_result import PaginatedResult
from braintree.resource import Resource
from braintree.resource_collection import ResourceCollection
from braintree.successful_result import SuccessfulResult
from braintree.exceptions.not_found_error import NotFoundError

class MerchantAccountGateway(object):
    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config

    def find(self, merchant_account_id):
        pass

    def create_for_currency(self, params=None):
        pass

    def all(self):
        pass

    def _fetch_merchant_accounts(self, current_page):
        pass

    def _post(self, url, params=None):
        pass

    def _put(self, url, params=None):
        if params is None:
            params = {}
        response = self.config.http().put(self.config.base_merchant_path() + url, params)
        if "merchant_account" in response:
            return SuccessfulResult({"merchant_account": MerchantAccount(self.gateway, response["merchant_account"])})
        elif "api_error_response" in response:
            return ErrorResult(self.gateway, response["api_error_response"])