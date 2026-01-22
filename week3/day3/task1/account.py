from  abc import ABC ,abstractmethod
class Account(ABC):
    def __init__(self,name ,balance):
        self.name = name
        self._balance = balance

    @abstractmethod
    def getYearlyBalance(self):
        pass


    def getBalance(self):
        return  self._balance

    def setBalance(self,balance):
        if balance >=0:
            self._balance =balance
        else:
            print('In valid balance')


#Account
# name , balance
# getYearlyBalance() → balance * 12

