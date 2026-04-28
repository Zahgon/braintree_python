import re
import braintree
from braintree.plan import Plan
from braintree.error_result import ErrorResult
from braintree.exceptions.not_found_error import NotFoundError
from braintree.resource import Resource
from braintree.resource_collection import ResourceCollection
from braintree.successful_result import SuccessfulResult

class PlanGateway(object):
    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config

    def all(self):
        pass

    def create(self, params=None):
        pass

    def find(self, plan_id):
        pass

    def update(self, plan_id, params=None):
        if params is None:
            params = {}
        Resource.verify_keys(params, Plan.update_signature())
        response = self.config.http().put(self.config.base_merchant_path() + "/plans/" + plan_id, {"plan": params})
        if "plan" in response:
            return SuccessfulResult({"plan": Plan(self.gateway, response["plan"])})
        elif "api_error_response" in response:
            return ErrorResult(self.gateway, response["api_error_response"])

