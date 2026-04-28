import braintree
from braintree.error_result import ErrorResult
from braintree.successful_result import SuccessfulResult
from braintree.transaction import Transaction
from braintree.exceptions.test_operation_performed_in_production_error import TestOperationPerformedInProductionError

class TestingGateway(object):
    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config

    def make_past_due(self, subscription_id, number_of_days_past_due=1):
        pass

    def settle_transaction(self, transaction_id):
        pass

    def settlement_confirm_transaction(self, transaction_id):
        pass

    def settlement_decline_transaction(self, transaction_id):
        pass

    def settlement_pending_transaction(self, transaction_id):
        pass

    def create_3ds_verification(self, merchant_account_id, params):
        pass

    def __create_result(self, response):
        pass

    def __check_environment(self):
        pass

