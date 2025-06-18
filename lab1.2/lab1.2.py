from matplotlib import pyplot
from openpyxl import load_workbook
import os

wb = load_workbook('/Users/sveta/Documents/p4ne/lab1.2/data_analysis_lab.xlsx') 


sheet = wb['Data']
sheet['A'][1:] 

def getvalue(x): 
    return x.value

list_x = list(map(getvalue, sheet['A'][1:]))

list_y = list(map(getvalue, sheet['C'][1:]))

list_z = list(map(getvalue, sheet['D'][1:]))

pyplot.plot(list_x, list_y, label="Относительная температура") 
pyplot.plot(list_x, list_z, label="Активность") 

pyplot.xlabel("Годы")
pyplot.ylabel("Показатели")
pyplot.legend(loc="best")

pyplot.show() 