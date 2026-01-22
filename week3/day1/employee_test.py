from  employee import  Employee


e1 =Employee('Mohamed',600)
print(e1.name)
#data=e1.Annual_salary()
stat = e1.get_level()
#print(data)
print(stat)

print('----------')

#Employee
#name ,age ,salary
#getAnnual_Salary() salary *12

#BaseEmployee
#name ,age ,salary,overTime
#getAnnual_Salary() (salary +overTime) *12


#HourlyEmployee
#name ,age ,salary,price,totalHour
#getAnnual_Salary() (salary +(price*totalHour)) *12

#test_employee
#HourlyEmployee,BaseEmployee,Employee