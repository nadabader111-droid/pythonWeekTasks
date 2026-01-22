#check_day
#Enter Your day
#1 2 3 4 5 Workday
#6 7 Off day
#Out Of Scope

day= int(input('Enter Your day(1-7):'))
result = "Out Of Scope"
#if day >=1  and  day <=5:
if 1<= day <=5:
    result ='Workday'
elif day==6 or day==7:
    result ='Off day'
print(result)

