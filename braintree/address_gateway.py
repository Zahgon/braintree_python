import re
import braintree
from braintree.address import Address
from braintree.error_result import ErrorResult
from braintree.exceptions.not_found_error import NotFoundError
from braintree.resource import Resource
from braintree.successful_result import SuccessfulResult

class AddressGateway(object):
    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config

    def __validate_chars_in_args(self, customer_id, address_id):
        if not re.search(r"\A[0-9A-Za-z_-]+\Z", customer_id):
            raise KeyError("customer_id contains invalid characters")
        if not re.search(r"\A[0-9A-Za-z]+\Z", address_id):
            raise KeyError("address_id contains invalid characters")

    def create(self, params=None):
        pass

    def delete(self, customer_id, address_id):
        pass

    def find(self, customer_id, address_id):
        pass

    def update(self, customer_id, address_id, params=None):
        if params is None:
            params = {}
        Resource.verify_keys(params, Address.update_signature())
        self.__validate_chars_in_args(customer_id, address_id)
        response = self.config.http().put(
            self.config.base_merchant_path() + "/customers/" + customer_id + "/addresses/" + address_id,
            {"address": params}
        )
        if "address" in response:
            return SuccessfulResult({"address": Address(self.gateway, response["address"])})
        elif "api_error_response" in response:
            return ErrorResult(self.gateway, response["api_error_response"])

