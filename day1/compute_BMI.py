try:
    name = input('Enter Your name:')
    weight = float(input('Enter Your Weight:'))
    height = float(input('Enter Your Height'))
    bmi = weight / (height / 100) ** 2
   # print("Patient Name:", name, "Your BMI:",bmi)
    print(f"Patient Name: {name} Your BMI:{bmi}")
except:
    print('حدث خطا  غير متوقع يرجي اعاده المحاله وقت لاحق')


#compute_BMI
#Enter your name: Ali
#Enter your Weight: 84.5
#Enter your Height:185.5
#bmi=weight/(height/100)**2
# Patient Name: Ali Your BMI:24.455525252