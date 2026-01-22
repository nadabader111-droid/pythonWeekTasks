class Employee:

    def __init__(self,name,salary):
        self.name=name
        self.salary =salary

    def Annual_salary(self):
        data = self.salary * 12
        return  data


    def get_level(self):
        total =self.Annual_salary()
        if total >= 12000:
            return 'High Salary'
        elif total >= 6000:
            return  'Normal Salary'
        elif total >=3000:
            return 'Low salary'
        else:
            return  'very low salary'








# student   test_Student
#Feilds name,mark,fullMark
#Functions Get_PCT()