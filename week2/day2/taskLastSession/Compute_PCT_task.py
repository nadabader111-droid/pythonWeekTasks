def compute_pct(mark , fullmark):
    pct = (mark / fullmark) * 100

    print("Your Pct is :",pct,"%")
    if pct >= 84:
        print('Excellent')
    elif pct > 74:
        print('v.good')
    elif pct > 64:
        print('Good')
    elif pct >= 50:
        print('pass')
    else:
        print('Failed')

mark = float(input('Enter Your Mark:'))
fullmark = int(input('Enter Your Full Mark:'))
compute_pct(mark , fullmark)
