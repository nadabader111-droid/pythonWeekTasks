import  pandas as pd
from tabulate import tabulate
#openpyxl

file_name ='example.xlsx'
data = pd.read_excel(file_name)
print(tabulate(data,headers='Keys',tablefmt='fancy_grid'))

