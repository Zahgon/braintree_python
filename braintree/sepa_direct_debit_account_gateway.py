import braintree
from braintree.sepa_direct_debit_account import SepaDirectDebitAccount
from braintree.error_result import ErrorResult
from braintree.exceptions.not_found_error import NotFoundError
from braintree.resource import Resource
from braintree.successful_result import SuccessfulResult


class SepaDirectDebitAccountGateway(object):
    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config

    def find(self, sepa_direct_debit_account_token):
        pass

    def delete(self, sepa_direct_debit_account_token):
        pass
