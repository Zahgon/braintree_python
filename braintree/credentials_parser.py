import os
import sys
import braintree
from braintree.exceptions.configuration_error import ConfigurationError
from braintree.environment import Environment

class CredentialsParser(object):
    def __init__(self, client_id=None, client_secret=None, access_token=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token

    def parse_client_credentials(self):
        pass

    def parse_access_token(self):
        pass

    def get_environment(self, credential):
        pass

    def get_merchant_id(self, credential):
        pass
