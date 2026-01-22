# #Define  Function   Void  Function
# def Sum(x,y):
#     res =x+y
#     print(res)
# #-----------------------------------
#
#
# #Calling  Function
# x=int(input('Enter X:'))
# y=int(input('Enter Y:'))
# Sum(x,y)
# #---------------------------------------------


# #Define  Function   return  Function
# def Sum2(x,y):
#     res =x+y
#     return (res)
# #-----------------------------------
#
# #Calling  Function
# x=int(input('Enter X2:'))
# y=int(input('Enter Y2:'))
# res= Sum2(x,y) +5
# print(res)
# #-----------------------------------
#
# def computeSal(salary):
#
#     totalSalary = salary * 12
#     return (totalSalary)
# salary = int(input('Please Enter Your Salary: '))
# totalSalary = computeSal(salary)
# print (totalSalary)
# #-----------------------------------------------------------------
#
#
# def compute_grade(mark,fullmark):
#     try:
#         pct = (mark / fullmark) * 100
#         return ("Your Pct is :", pct, "%")
#     except:
#         print('حدث خطا غير متوقع يرجي اعاده المحاله وقت لاحق')
# mark = float(input('Enter Your Mark:'))
# fullmark = int(input('Enter Your Full Mark:'))
# pct = compute_grade(mark,fullmark)
# print(pct)
#
# #-----------------------------------------------------------------
# def compute_bmi(name,weight,height):
#
#  try:
#
#     bmi = weight / (height / 100) ** 2
#     #print("Patient Name:", name, "Your BMI:",bmi)
#     res =f"Patient Name: {name} Your BMI:{bmi}"
#     return res
#  except:
#     print('حدث خطا  غير متوقع يرجي اعاده المحاله وقت لاحق')
# name = input('Enter Your name:')
# weight = float(input('Enter Your Weight:'))
# height = float(input('Enter Your Height'))
# res = compute_bmi(name,weight,height)
# print (res)
# #---------------------------------------------------------
#
#
#
# def computeSal_V2(salary):
#     totalSalary = salary * 12
#     return (totalSalary)
#
# def get_level(annual_salary):
#     if annual_salary >=12000:
#         print('High')
#     elif annual_salary >=6000:
#         print('Normal')
#     elif annual_salary >= 3000:
#         print('Low')
#     else:
#         print('very Low')
#
# salary = int(input('Please Enter Your Salary: '))
# totalSalary = computeSal_V2(salary)
# print (totalSalary)
# get_level(totalSalary)
#
# #--------------------------------

def compute_pct(mark, fullmark):
    pct = (mark / fullmark) * 100
    return pct

def get_pct(total_pct):

    if total_pct >= 84:
        return ('Excellent')
    elif total_pct > 74:
        return('v.good')
    elif total_pct > 64:
        return('Good')
    elif total_pct >= 50:
        return('pass')
    else:
        return('Failed')



