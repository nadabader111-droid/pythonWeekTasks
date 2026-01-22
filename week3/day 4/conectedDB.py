from sqlite3 import connect
import  os

dp_path =f"{os.getcwd()}\\hr.db"

print(dp_path)
db =connect(dp_path)
cur =db.cursor()
sql ="select first_name,phone_number ,salary ,salary * 12 as total from employees"
data = cur.execute(sql).fetchall()
for x in data:
    print(x)




