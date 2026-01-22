try:
    name = input('Enter Your name:')
    weight = float(input('Enter Your Weight:'))
    height = float(input('Enter Your Height'))
    bmi = weight / (height / 100) ** 2
    #print("Patient Name:", name, "Your BMI:",bmi)
    print(f"Patient Name: {name} Your BMI:{bmi}")
except:
    print('حدث خطا  غير متوقع يرجي اعاده المحاله وقت لاحق')

#Solution 1
if bmi >30:
    print('Obese')
elif bmi >24 :
    print('Over Weight')
elif bmi >18:
    print('Normal Weight')
else:
    print('Under Weight')
#------------------------------
#Solution 2
if bmi <18:
    print('Under Weight')
elif bmi <24:
    print('Normal Weight')

elif bmi <30:
    print(' Over Weight')
else:
    print('Obese')


# >18  <24   Normal Weight
# >24 <30  Over Weight
# <18 Under Weight
# >30 Obese



