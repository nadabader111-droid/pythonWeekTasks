from  employee import Employee
class BaseEmployee(Employee):
    def __init__(self,name ,age ,salary,overTime):
        Employee.__init__(self,name ,age ,salary)
        self.overTime =overTime

    def getAnnual_Salary(self):
        annual = (self.salary +self.overTime) * 12
        return annual

    def sayHi(self):
        print()

