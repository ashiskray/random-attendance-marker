from openpyxl import Workbook
import random
from datetime import datetime
employe=["ashis","rahul","rohit","mohit","bikas"]
today= datetime.today().strftime('%d-%m-%y')
wb=Workbook()
ws=wb.active
ws.title=("employe attendence")
# today= datetime.today().strftime('%d-%m-%y')
# ws.append([f"date:{today}"])
# ws.append([])
ws.append(["name","status","date"])
for employee in employe:
    status=random.choice(["Present","Absent"])
    ws.append([employee,status,today])

filename = f"attendence_{today}.xlsx"
wb.save("empattendence.xlsx")
# print(f"attendence file saved as {empattendence.xlsx}")