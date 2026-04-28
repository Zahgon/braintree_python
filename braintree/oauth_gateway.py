import braintree
from braintree.error_result import ErrorResult
from braintree.successful_result import SuccessfulResult
from braintree.exceptions.not_found_error import NotFoundError
from braintree.oauth_credentials import OAuthCredentials

import sys
from urllib.parse import quote_plus
from functools import reduce

class OAuthGateway(object):
    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config

    def create_token_from_code(self, params):
        pass

    def create_token_from_refresh_token(self, params):
        pass

    def revoke_access_token(self, access_token):
        pass

    def _create_token(self, params):
        pass

    def connect_url(self, raw_params):
        pass

    def _sub_query(self, params, root):
        pass
