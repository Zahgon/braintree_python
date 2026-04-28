from braintree.attribute_getter import AttributeGetter

class BankAccountInstantVerificationJwt(AttributeGetter):
    def __init__(self, jwt):
        self.jwt = jwt

    @property
    def jwt(self):
        pass

    @jwt.setter
    def jwt(self, value):
        pass
