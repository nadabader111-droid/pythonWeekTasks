from  employee import Employee
from  baseEmployee import  BaseEmployee
from  hourlyEmployee import HourlyEmployee


#e1= Employee('Mohamed' , 25 , 1000)
b1= BaseEmployee('Osama' , 25 , 1000,500)
h1= HourlyEmployee('Nada' , 25 , 1000,5,50)

#print(e1.name , e1.getAnnual_Salary())
print(b1.name , b1.getAnnual_Salary())
print(h1.name , h1.getAnnual_Salary())



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






