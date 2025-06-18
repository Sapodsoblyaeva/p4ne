from matplotlib import pyplot
from openpyxl import load_workbook
import os

# print("Текущая рабочая директория:", os.getcwd())

wb = load_workbook('/Users/sveta/Documents/p4ne/lab1.2/data_analysis_lab.xlsx') 


sheet = wb['Data']
sheet['A'][1:] 

def getvalue(x): 
    return x.value

list_x = list(map(getvalue, sheet['A'][1:]))

list_y = list(map(getvalue, sheet['C'][1:]))

list_z = list(map(getvalue, sheet['D'][1:]))

# print(list_x)
# print(list_y)

pyplot.plot(list_x, list_y, label="График роста относительной температуры по годам") 
pyplot.plot(list_x, list_z, label="График роста солнечной активности по годам") 

pyplot.xlabel("Годы")
pyplot.ylabel("Температура и Активность")
pyplot.legend(loc="best")

pyplot.show() 