class Transfer(object):
    
    def __init__(self, trsf_id, account_from, account_to, amount, category, date, commission):
        self.trsf_id = trsf_id
        self.account_from = account_from
        self.account_to = account_to
        self.amount = amount
        self.category = category
        self.date = date
        self.commission = commission


