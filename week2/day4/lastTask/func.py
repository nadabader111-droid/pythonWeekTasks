def compute_bmi(n, w, h):
    bmi = w / (h / 100) ** 2
    res = [n,bmi]
    return res

def get_bmi(bmi):
    if bmi > 30:
        return 'Obese'
    elif bmi > 25:
        return 'Over Weight'
    elif bmi > 18:
        return 'Normal Weight'
    else:
        return 'Under Weight'