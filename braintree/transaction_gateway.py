import braintree
import warnings
from braintree.error_result import ErrorResult
from braintree.resource import Resource
from braintree.resource_collection import ResourceCollection
from braintree.successful_result import SuccessfulResult
from braintree.transaction import Transaction
from braintree.exceptions.not_found_error import NotFoundError
from braintree.exceptions.request_timeout_error import RequestTimeoutError


class TransactionGateway(object):
    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config

    def adjust_authorization(self, transaction_id, amount):
        pass

    def clone_transaction(self, transaction_id, params):
        pass

    def cancel_release(self, transaction_id):
        pass

    def create(self, params):
        pass

    def credit(self, params):
        pass

    def find(self, transaction_id):
        pass

    def refund(self, transaction_id, amount_or_options=None):
        """
        Refunds an existing transaction. It expects a transaction_id. ::

            result = braintree.Transaction.refund("my_transaction_id")
        """
        pass

    def sale(self, params):
        pass

    def search(self, *query):
        if isinstance(query[0], list):
            query = query[0]

        response = self.config.http().post(self.config.base_merchant_path() + "/transactions/advanced_search_ids", {"search": self.__criteria(query)})
        if "search_results" in response:
            return ResourceCollection(query, response, self.__fetch)
        else:
            raise RequestTimeoutError("search timeout")

    def submit_for_settlement(self, transaction_id, amount=None, params=None):
        pass

    def update_details(self, transaction_id, params=None):
        pass

    def submit_for_partial_settlement(self, transaction_id, amount, params=None):
        pass

    def package_tracking(self, transaction_id, params=None):
        pass

    def void(self, transaction_id):
        pass

    def __fetch(self, query, ids):
        pass

    def __criteria(self, query):
        criteria = {}
        for term in query:
            if criteria.get(term.name):
                criteria[term.name] = dict(list(criteria[term.name].items()) + list(term.to_param().items()))
            else:
                criteria[term.name] = term.to_param()
        return criteria

    def _post(self, url, params=None):
        pass

    # NEXT_MAJOR_VERSION remove these checks when the attributes are removed
    def __check_for_deprecated_attributes(self, params):
        if "device_session_id" in params.keys():
            warnings.warn("device_session_id is deprecated, use device_data parameter instead", DeprecationWarning)
        if "fraud_merchant_id" in params.keys():
            warnings.warn("fraud_merchant_id is deprecated, use device_data parameter instead", DeprecationWarning)
        if "three_d_secure_token" in params.keys():
            warnings.warn("three_d_secure_token is deprecated, use three_d_secure_authentication_id parameter instead", DeprecationWarning)
        if "venmo_sdk_payment_method_code" in params.keys() or "venmo_sdk_session" in params.keys():
            warnings.warn("The Venmo SDK integration is Unsupported. Please update your integration to use Pay with Venmo instead.", DeprecationWarning)
