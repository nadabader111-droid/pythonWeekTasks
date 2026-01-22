from account import Account
class SavingAccount(Account):
    def __init__(self,name,balance,bouns):
        Account.__init__(self, name, balance)

        self.bouns = bouns

    def getYearlyBalance(self):
        balance = (self._balance + self.bouns) * 12
        return balance




#SavingAccount
# name , balance , bonus
# getYearlyBalance() → (balance + bonus) * 12







