from random import randint
correct_answer = 0
for x in range(1,11):
     num1 = randint (1,10)
     num2 = randint (1,10)
     multi =  num1 * num2
     answer = float (input (f' {x}.what is {num1} * {num2}?'))
     res =  "wrong"
     if answer == multi:
        res= "correct"
        correct_answer +=1
     print (res)
     print('-' * 50)
print('correct:', correct_answer)
print('wrong:', 10 - correct_answer)
