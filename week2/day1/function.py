def sayhi():
    print('Hello  CRM System')




def computeSal():
    salary = int(input('Please Enter Your Salary: '))
    totalSalary = salary * 12
    print(totalSalary)

def compute_grade():
    try:
        mark = float(input('Enter Your Mark:'))
        fullmark = int(input('Enter Your Full Mark:'))
        pct = (mark / fullmark) * 100
        print("Your Pct is :", pct, "%")
    except:
        print('حدث خطا غير متوقع يرجي اعاده المحاله وقت لاحق')



def compute_bmi():

 try:
    name = input('Enter Your name:')
    weight = float(input('Enter Your Weight:'))
    height = float(input('Enter Your Height'))
    bmi = weight / (height / 100) ** 2
    #print("Patient Name:", name, "Your BMI:",bmi)
    print(f"Patient Name: {name} Your BMI:{bmi}")
 except:
    print('حدث خطا  غير متوقع يرجي اعاده المحاله وقت لاحق')


def sayhi2(name):
    print(f'Hello  {name}')

n='Osama'
sayhi2(n)



def compute_grade2():
    try:
        mark = float(input('Enter Your Mark:'))
        fullmark = int(input('Enter Your Full Mark:'))
        pct = (mark / fullmark) * 100
        print("Your Pct is :", pct, "%")
    except:
        print('حدث خطا غير متوقع يرجي اعاده المحاله وقت لاحق')


def computeSal2(salary):
    totalSalary = salary * 12
    print(totalSalary)



salary =int(input('Enter Your salary:'))
computeSal2(salary)




def compute_grade(mark,fullmark):
    try:
        pct = (mark / fullmark) * 100
        print("Your Pct is :", pct, "%")
    except:
        print('حدث خطا غير متوقع يرجي اعاده المحاله وقت لاحق')

mark = float(input('Enter Your Mark:'))
fullmark = int(input('Enter Your Full Mark:'))
compute_grade(mark,fullmark)



def compute_bmi2(name,weight,height):
 try:
    bmi = weight / (height / 100) ** 2
    print(f"Patient Name: {name} Your BMI:{bmi}")
 except:
    print('حدث خطا  غير متوقع يرجي اعاده المحاله وقت لاحق')



name = input('Enter Your name:')
weight = float(input('Enter Your Weight:'))
height = float(input('Enter Your Height'))
compute_bmi2(name,weight,height)