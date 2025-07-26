from openpyxl import workbook,load_workbook
eb=load_workbook(r"C:\Users\ashis\OneDrive\Desktop\Data Automation\excell_automaton\practice.xlsx")
es=eb.active
es['a1']='students name'
eb.save(r"C:\Users\ashis\OneDrive\Desktop\Data Automation\excell_automaton\practice.xlsx")
print(es['a1'].value)