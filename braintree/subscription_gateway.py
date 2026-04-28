import re
import braintree
from braintree.subscription import Subscription
from braintree.error_result import ErrorResult
from braintree.exceptions.not_found_error import NotFoundError
from braintree.resource import Resource
from braintree.resource_collection import ResourceCollection
from braintree.successful_result import SuccessfulResult
from braintree.transaction import Transaction


class SubscriptionGateway(object):
    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config

    def cancel(self, subscription_id):
        pass

    def create(self, params=None):
        pass

    def find(self, subscription_id):
        pass

    def retry_charge(self, subscription_id, amount=None, submit_for_settlement=False):
        pass

    def search(self, *query):
        if isinstance(query[0], list):
            query = query[0]

        response = self.config.http().post(self.config.base_merchant_path() + "/subscriptions/advanced_search_ids", {"search": self.__criteria(query)})
        return ResourceCollection(query, response, self.__fetch)

    def update(self, subscription_id, params=None):
        if params is None:
            params = {}
        Resource.verify_keys(params, Subscription.update_signature())
        response = self.config.http().put(self.config.base_merchant_path() + "/subscriptions/" + subscription_id, {"subscription": params})
        if "subscription" in response:
            return SuccessfulResult({"subscription": Subscription(self.gateway, response["subscription"])})
        elif "api_error_response" in response:
            return ErrorResult(self.gateway, response["api_error_response"])

    def __criteria(self, query):
        criteria = {}
        for term in query:
            if criteria.get(term.name):
                criteria[term.name] = dict(list(criteria[term.name].items()) + list(term.to_param().items()))
            else:
                criteria[term.name] = term.to_param()
        return criteria

    def __fetch(self, query, ids):
        pass

