file = open("nada",'a')
name = input('Enter Your Name:')
mark = float(input('Enter Your Mark:'))
fullMark = float(input('Enter Your Mark:'))
pct = mark / fullMark *100
res =["\nStudent Name:",name,"\n Your Mark:", str(mark),"\nYour FullMark", str(fullMark),"\nYour PCT:",str(pct),"%"]
#file.write(f'\n{name} ')
file.writelines(res)
file.write('\n------------------')
file.close()


file = open("nada",'r')
# print(file.readlines())
for x in file.readlines():
    print(x)
file.close()
