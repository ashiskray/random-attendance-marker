# wap to print the value of perticular cell 
from openpyxl import workbook,load_workbook
EB=load_workbook(r"C:\Users\ashis\OneDrive\Desktop\Data Automation\excell_automaton\practice.xlsx")
ES=EB.active
print(ES['b1'].value)  #put the cell no. and you will get the value 
