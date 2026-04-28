from datetime import datetime

class TransactionUsBankAccountRequest(object):
    def __init__(self, parent):
        self.parent = parent
        self._ach_mandate_text = None
        self._ach_mandate_accepted_at = None

    def ach_mandate_text(self, ach_mandate_text):
        pass

    def ach_mandate_accepted_at(self, ach_mandate_accepted_at):
        pass

    def done(self):
        pass

    def to_param_dict(self):
        pass
