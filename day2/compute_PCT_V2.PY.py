try:
    mark = float(input('Enter Your Mark:'))
    fullmark = int(input('Enter Your Full Mark:'))
    pct = (mark / fullmark) * 100
    print("Your Pct is :",pct,"%")
except:
    print('حدث خطا  غير متوقع يرجي اعاده المحاله وقت لاحق')
if pct>=84:
    print('Excellent')
elif pct>74:
    print('v.good')
elif pct>64:
    print('Good')
elif pct>=50:
    print('pass')
else:
    print('Failed')
#>=50pass
# >64 Good
# >74  v.good
# >84 Excellent
#<50 Failed
