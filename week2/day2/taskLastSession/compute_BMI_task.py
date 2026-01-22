#Define  Function
def compute_bmi(weight,height,name ):
    bmi = weight / (height / 100) ** 2
    print(f"Patient Name: {name} Your BMI:{bmi}")
    if bmi >= 50:
        print('Over Weight')
    else:
        print('Normal Weight')
#-----------------------------------

#Calling  Function
name = input('Enter Your name:')
weight = float(input('Enter Your Weight:'))
height = float(input('Enter Your Height'))

compute_bmi(weight,height,name )
#---------------------------------------------