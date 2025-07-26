from openpyxl import workbook, load_workbook
EB=load_workbook(r"C:\Users\ashis\OneDrive\Desktop\Data Automation\excell_automaton\practice.xlsx")
ES=EB.active   # this will return the nno. of active sheets in excel
print(ES)