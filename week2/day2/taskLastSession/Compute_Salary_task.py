def compute_pct(salary):
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

salary = int(input('Please Enter Your Salary: '))
compute_pct(salary)