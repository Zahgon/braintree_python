from braintree.util.crypto import Crypto
from braintree.webhook_notification import WebhookNotification
import sys
from base64 import encodebytes
from datetime import datetime

class WebhookTestingGateway(object):
    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config

    def sample_notification(self, kind, id, source_merchant_id=None):
        pass

    def __sample_xml(self, kind, id, source_merchant_id):
        pass

    def __subject_sample_xml(self, kind, id):
        pass

    def __check_sample_xml(self):
        pass

    def __transaction_disbursed_sample_xml(self, id):
        pass

    def __transaction_retried_sample_xml(self, id):
        pass

    def __transaction_reviewed_sample_xml(self, id):
        pass

    def __transaction_settled_sample_xml(self, id):
        pass

    def __transaction_settlement_declined_sample_xml(self, id):
        pass

    def __disbursement_exception_sample_xml(self, id):
        pass

    def __disbursement_sample_xml(self, id):
        pass

    def __dispute_under_review_sample_xml(self, id):
        pass

    def __dispute_opened_sample_xml(self, id):
        pass

    def __dispute_lost_sample_xml(self, id):
        pass

    def __dispute_won_sample_xml(self, id):
        pass

    def __dispute_accepted_sample_xml(self, id):
        pass

    def __dispute_auto_accepted_sample_xml(self, id):
        pass

    def __dispute_disputed_sample_xml(self, id):
        pass

    def __dispute_expired_sample_xml(self, id):
        pass

    def __old_dispute_under_review_sample_xml(self, id):
        pass

    def __old_dispute_opened_sample_xml(self, id):
        pass

    def __old_dispute_lost_sample_xml(self, id):
        pass

    def __old_dispute_won_sample_xml(self, id):
        pass

    def __old_dispute_accepted_sample_xml(self, id):
        pass

    def __old_dispute_auto_accepted_sample_xml(self, id):
        pass

    def __old_dispute_disputed_sample_xml(self, id):
        pass

    def __old_dispute_expired_sample_xml(self, id):
        pass

    def __new_dispute_under_review_sample_xml(self, id):
        pass

    def __new_dispute_opened_sample_xml(self, id):
        pass

    def __new_dispute_lost_sample_xml(self, id):
        pass

    def __new_dispute_won_sample_xml(self, id):
        pass

    def __new_dispute_accepted_sample_xml(self, id):
        pass

    def __new_dispute_auto_accepted_sample_xml(self, id):
        pass

    def __new_dispute_disputed_sample_xml(self, id):
        pass

    def __new_dispute_expired_sample_xml(self, id):
        pass

    def __refund_failed_sample_xml(self, id):
        pass

    def __subscription_sample_xml(self, id):
        pass

    def __subscription_billing_skipped_sample_xml(self, id):
        pass

    def __subscription_charged_successfully_sample_xml(self, id):
        pass

    def __subscription_charged_unsuccessfully_sample_xml(self, id):
        pass

    def __merchant_account_approved_sample_xml(self, id):
        pass

    def __merchant_account_declined_sample_xml(self, id):
        pass

    def __partner_merchant_connected_sample_xml(self):
        pass

    def __partner_merchant_disconnected_sample_xml(self):
        pass

    def __connected_merchant_status_transitioned_xml(self, id):
        pass

    def __connected_merchant_paypal_status_changed_xml(self, id):
        pass

    def __partner_merchant_declined_sample_xml(self):
        pass

    def __oauth_access_revocation_sample_xml(self, id):
        pass

    def __account_updater_daily_report_sample_xml(self):
        pass

    def __granted_payment_instrument_update(self):
        pass

    def __granted_payment_method_revoked(self, id):
        pass

    def __payment_method_revoked_by_customer(self, id):
        pass

    def __local_payment_completed(self, id):
        pass

    def __default_local_payment_completed(self):
        pass
    def __blik_one_click_local_payment_completed(self):
        pass

    def __local_payment_expired(self):
        pass

    def __local_payment_funded(self):
        pass

    def __local_payment_reversed(self):
        pass

    def __payment_method_customer_data_updated_sample_xml(self, id):
        pass

    def __venmo_account_xml(self, id):
        pass
