import braintree
import re
import warnings
from braintree.dispute import Dispute
from braintree.dispute_details import DisputeEvidence
from braintree.error_result import ErrorResult
from braintree.successful_result import SuccessfulResult
from braintree.exceptions.not_found_error import NotFoundError
from braintree.paginated_result import PaginatedResult
from braintree.paginated_collection import PaginatedCollection
from braintree.resource_collection import ResourceCollection

class DisputeGateway(object):
    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config

    def accept(self, dispute_id):
        pass

    def add_file_evidence(self, dispute_id, document_upload_id_or_request):
        pass

    def add_text_evidence(self, dispute_id, content_or_request):
        pass

    def finalize(self, dispute_id):
        pass

    def find(self, dispute_id):
        pass

    def remove_evidence(self, dispute_id, evidence_id):
        pass

    def search(self, *query):
        if isinstance(query[0], list):
            query = query[0]

        self.search_criteria = self.__criteria(query)

        pc = PaginatedCollection(self.__fetch_disputes)
        return SuccessfulResult({"disputes": pc})

    def __fetch_disputes(self, page):
        pass

    def __criteria(self, query):
        criteria = {}

        for term in query:
            if criteria.get(term.name):
                criteria[term.name] = dict(list(criteria[term.name].items()) + list(term.to_param().items()))
            else:
                criteria[term.name] = term.to_param()
        return criteria
