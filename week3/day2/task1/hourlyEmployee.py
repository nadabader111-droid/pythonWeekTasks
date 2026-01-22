from  employee import Employee
class HourlyEmployee(Employee):
    def __init__(self,name ,age ,salary,price,totalHour):
        Employee.__init__(self,name ,age ,salary)
        self.price =price
        self.totalHour =totalHour

    def getAnnual_Salary(self):
        annual = (self.salary + (self.totalHour * self.price)) * 12
        return annual


    def sayHi(self):
        print()