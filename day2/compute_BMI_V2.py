try:
    name = input('Enter Your name:')
    weight = float(input('Enter Your Weight:'))
    height = float(input('Enter Your Height'))
    bmi = weight / (height / 100) ** 2
    #print("Patient Name:", name, "Your BMI:",bmi)
    print(f"Patient Name: {name} Your BMI:{bmi}")
except:
    print('حدث خطا  غير متوقع يرجي اعاده المحاله وقت لاحق')


if bmi>=50:
    print('Over Weight')
else:
    print('Normal Weight')

# >18  <24   Normal Weight
# >24 <30  Over Weight
# <18 Under Weight
# <30 Obese
#>25 Over Weight
#<25 Normal Weight

#compute_BMI
#Enter your name: Ali
#Enter your Weight: 84.5
#Enter your Height:185.5
#bmi=weight/(height/100)**2
# Patient Name: Ali Your BMI:24.455525252