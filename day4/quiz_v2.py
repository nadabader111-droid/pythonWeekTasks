from random import randint

for x in range(1,11):
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    muilt = num1 * num2
    answer = float(input(f'{x}.What is  {num1} * {num2} ?'))
    res = 'Wrong'
    if answer == muilt:
        res = 'Correct'

    print('-'*50)

    print(res)



print('Game Over')