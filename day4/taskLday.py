day = int(input('enter your day'))
result = 'out of scope'
if day >= 1  and  day <= 5:
    result = 'work day'
elif day == 6:
    result = 'off day'
elif day == 7:
    result = 'off day'
print(result)