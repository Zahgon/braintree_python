import braintree
from braintree.us_bank_account import UsBankAccount
from braintree.exceptions.not_found_error import NotFoundError

class UsBankAccountGateway(object):
    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config

    def find(self, us_bank_account_token):
        pass

