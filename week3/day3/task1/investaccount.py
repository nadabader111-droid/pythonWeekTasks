from account import Account
class Investaccount(Account):
    def __init__(self,name,balance,rate):
        Account.__init__(self, name, balance)
        self.rate = rate

    def getYearlyBalance(self):
        balance = (self._balance +( self._balance *self.rate)) * 12
        return balance

#InvestAccount
# name , balance , rate
# getYearlyBalance() → (balance + (balance * rate)) * 12

