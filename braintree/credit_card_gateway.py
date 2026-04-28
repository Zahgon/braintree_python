import braintree
import warnings
from braintree.credit_card import CreditCard
from braintree.error_result import ErrorResult
from braintree.exceptions.not_found_error import NotFoundError
from braintree.ids_search import IdsSearch
from braintree.resource import Resource
from braintree.resource_collection import ResourceCollection
from braintree.successful_result import SuccessfulResult


class CreditCardGateway(object):
    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config

    def create(self, params=None):
        pass

    def delete(self, credit_card_token):
        pass

    def expired(self):
        pass

    def expiring_between(self, start_date, end_date):
        pass

    def find(self, credit_card_token):
        pass

    def forward(self, credit_card_token, receiving_merchant_id):
        raise NotFoundError("This method of forwarding payment methods is no longer supported. Please consider the Grant API for similar functionality.")

    def from_nonce(self, nonce):
        pass

    def update(self, credit_card_token, params=None):
        if params is None:
            params = {}
        Resource.verify_keys(params, CreditCard.update_signature())
        self.__check_for_deprecated_attributes(params)
        response = self.config.http().put(self.config.base_merchant_path() + "/payment_methods/credit_card/" + credit_card_token, {"credit_card": params})
        if "credit_card" in response:
            return SuccessfulResult({"credit_card": CreditCard(self.gateway, response["credit_card"])})
        elif "api_error_response" in response:
            return ErrorResult(self.gateway, response["api_error_response"])

    def __fetch_expired(self, query, ids):
        pass

    def __fetch_existing_between(self, query, ids):
        pass

    def _post(self, url, params=None):
        pass

    # NEXT_MAJOR_VERSION remove these checks when the attributes are removed
    def __check_for_deprecated_attributes(self, params):
        if "device_session_id" in params.keys():
            warnings.warn("device_session_id is deprecated, use device_data parameter instead", DeprecationWarning)
        if "fraud_merchant_id" in params.keys():
            warnings.warn("fraud_merchant_id is deprecated, use device_data parameter instead", DeprecationWarning)
        if "venmo_sdk_payment_method_code" in params.keys() or "venmo_sdk_session" in params.keys():
            warnings.warn("The Venmo SDK integration is Unsupported. Please update your integration to use Pay with Venmo instead.", DeprecationWarning)
