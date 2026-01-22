try:
    mark = float(input('Enter Your Mark:'))
    fullmark = int(input('Enter Your Full Mark:'))
    pct = (mark / fullmark) * 100
    print("Your Pct is :",pct,"%")
except:
    print('حدث خطا  غير متوقع يرجي اعاده المحاله وقت لاحق')


#compute_BMI
#Enter your name: Ali
#Enter your Weight: 84.5
#Enter your Height:185.5
#bmi=weight/(height/100)**2
# Patient Name: Ali Your BMI:24.455525252
