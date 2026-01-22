from  abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,name ,age ,salary):
        self.name =name
        self.age =age
        self.salary =salary

    @abstractmethod
    def getAnnual_Salary(self):
        pass

    @abstractmethod
    def sayHi(self):
        pass
