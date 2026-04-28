from braintree.credit_card_verification import CreditCardVerification
from braintree.credit_card_verification_search import CreditCardVerificationSearch
from braintree.exceptions.not_found_error import NotFoundError
from braintree.ids_search import IdsSearch
from braintree.resource_collection import ResourceCollection
from braintree.error_result import ErrorResult
from braintree.successful_result import SuccessfulResult


class CreditCardVerificationGateway(object):
    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config

    def find(self, verification_id):
        pass

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


    def search(self, *query):
        if isinstance(query[0], list):
            query = query[0]

        search_params = self.__criteria(query)
        search_params["verification_type"] = ["credit_card"]
        response = self.config.http().post(self.config.base_merchant_path() + "/verifications/advanced_search_ids", {"search": search_params})
        return ResourceCollection(query, response, self.__fetch)

    def __fetch_verifications(self, query, verification_ids):
        pass

    def create(self, params):
        pass
