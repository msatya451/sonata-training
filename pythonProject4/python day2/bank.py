class Account:
    def __init__(self,accno,name,acctype,bal):
        seld.account_number=accno
        self.username=name
        self.accounttype=acctype
        self.balance=bal
    def withdraw(self,ammount):
        self.amt=ammount
        if(self.balance<self.amt):
            return 'low balance'