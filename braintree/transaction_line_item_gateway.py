import braintree
from braintree.error_result import ErrorResult
from braintree.resource import Resource
from braintree.resource_collection import ResourceCollection
from braintree.transaction_line_item import TransactionLineItem
from braintree.exceptions.not_found_error import NotFoundError
from braintree.exceptions.request_timeout_error import RequestTimeoutError

class TransactionLineItemGateway(object):
    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config

    def find_all(self, transaction_id):
        pass
