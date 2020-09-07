class BankAccount:


    def __init__(self, input_holder_name, input_balance, input_type):
        self.holder_name = input_holder_name
        self.balance = input_balance
        self.type = input_type
        self._rates = {                                                             #'_' infront tells other programmers not to change the value poutside but inside is allowed
            "personal": 10,
            "business": 50,
        }
    
    def pay_in(self, amount):
        self.balance += amount
    
    def pay_monthly_fee(self):
        if(self.type == 'personal'):
            self.balance -= self._rates["personal"]
        elif(self.type == 'business'):
            self.balance -= self._rates["business"]



# def get_account_name(account):
#     return account["holder_name"]