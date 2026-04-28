import braintree
from braintree.resource import Resource

# NEXT_MAJOR_VERSION - rename to GooglePayCard
class AndroidPayCard(Resource):
    """
    A class representing Braintree Android Pay card objects.
    """
    def __init__(self, gateway, attributes):
        Resource.__init__(self, gateway, attributes)
        if hasattr(self, 'expired'):
            self.is_expired = self.expired

        if "subscriptions" in attributes:
            self.subscriptions = [braintree.subscription.Subscription(gateway, subscription) for subscription in self.subscriptions]

    @property
    def expiration_date(self):
        pass

    @property
    def last_4(self):
        pass

    @property
    def card_type(self):
        pass

    @staticmethod
    def signature():
        options = ["make_default"]

        signature = [
            "customer_id",
            "cardholder_name",
            "cryptogram",
            "google_transaction_id",
            "expiration_month",
            "expiration_year",
            "number",
            "token",
            "eci_indicator",
            {
                "options": options
            },
            {
                "billing_address": [
                    "company",
                    "country_code_alpha2",
                    "country_code_alpha3",
                    "country_code_numeric",
                    "country_name",
                    "extended_address",
                    "first_name",
                    "last_name",
                    "locality",
                    "postal_code",
                    "region",
                    "street_address",
                    "phone_number"
                ]
            }
        ]

        return signature


    @staticmethod
    def card_signature():
        options = ["make_default"]

        signature = [
            "customer_id",
            "cardholder_name",
            "google_transaction_id",
            "expiration_month",
            "expiration_year",
            "number",
            "token",
            {
                "options": options
            },
            {
                "billing_address": [
                    "company",
                    "country_code_alpha2",
                    "country_code_alpha3",
                    "country_code_numeric",
                    "country_name",
                    "extended_address",
                    "first_name",
                    "last_name",
                    "locality",
                    "postal_code",
                    "region",
                    "street_address",
                    "phone_number"
                ]
            }
        ]

        return signature


    @staticmethod
    def network_token_signature():
        return AndroidPayCard.signature()
