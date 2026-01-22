from func import compute_bmi,get_bmi

name = input('Enter Your name:')
weight = float(input('Enter Your Weight:'))
height = float(input('Enter Your Height'))

res = compute_bmi(name, weight, height)
total_bmi= get_bmi(res[1])

print(f"Patient Name: {res[0]} Your BMI:{res[1]}")
print(total_bmi)