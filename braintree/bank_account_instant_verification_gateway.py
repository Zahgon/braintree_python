from braintree.bank_account_instant_verification_jwt import BankAccountInstantVerificationJwt
from braintree.successful_result import SuccessfulResult
from braintree.error_result import ErrorResult
from braintree.exceptions.unexpected_error import UnexpectedError
from braintree.util.graphql_client import GraphQLClient


class BankAccountInstantVerificationGateway(object):
    def __init__(self, gateway):
        self.gateway = gateway
        self.config = self.gateway.config
        self.graphql_client = self.gateway.graphql_client

    CREATE_JWT_MUTATION = """
        mutation CreateBankAccountInstantVerificationJwt($input: CreateBankAccountInstantVerificationJwtInput!) {
            createBankAccountInstantVerificationJwt(input: $input) {
                jwt
            }
        }
    """

    def create_jwt(self, request):
        pass
