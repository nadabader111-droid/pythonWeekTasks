class Employee:

    def __init__(self,name,salary):
        self.name= name
        self.__salary= salary


    def getSalary(self):

         return  self.__salary


    def setSalary(self,salary):
        if salary >=0:
            self.__salary =salary
        else:
            print('Invalid salary')

    def getAuuanlSalary(self):
        return self.__salary *12