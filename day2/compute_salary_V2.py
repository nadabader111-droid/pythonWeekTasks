salary = int(input('Please Enter Your Salary: '))
totalSalary = salary * 12
print(totalSalary)
if totalSalary>=12000: #true
    print('High Salar')
elif totalSalary>6000:
    print('Normal Salary')
elif totalSalary>3000:
    print('Low Salary')

else:
    print('Very Low Salary')




# >12000 High Salary
# >6000   Normal Salary
# >3000  Low Salary
# <3000   Very Low Salary