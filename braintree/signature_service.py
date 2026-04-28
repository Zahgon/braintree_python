import urllib
from braintree.util.crypto import Crypto

class SignatureService(object):

    def __init__(self, private_key, hashfunc=Crypto.sha1_hmac_hash):
        self.private_key = private_key
        self.hmac_hash = hashfunc

    def sign(self, data):
        pass

    def hash(self, data):
        pass
