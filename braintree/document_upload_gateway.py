import braintree
import mimetypes
from braintree.document_upload import DocumentUpload
from braintree.error_result import ErrorResult
from braintree.resource import Resource
from braintree.successful_result import SuccessfulResult


class DocumentUploadGateway(object):
    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config

    def create(self, params=None):
        pass

    def __file_name(self, file):
        pass

    def __content_type(self, file):
        pass

    def __payload(self, params):
        pass
