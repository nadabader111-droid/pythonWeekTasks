from account import Account
from investaccount import Investaccount
from savingAccount import SavingAccount

#A1 = Account("nada",500)
S1 = SavingAccount("bader",500,500)
I1 = Investaccount("saud",500,0.20)
#A1.setBalance(800)
S1.setBalance(600)
I1.setBalance(100)

#print(A1.name,A1.getYearlyBalance())
print(S1.name,S1.getYearlyBalance())
print(I1.name,I1.getYearlyBalance())



#test_account
#Account , SavingAccount , InvestAccount