from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title='students data'
ws.append(['name','age','cource','year','code'])
wb.save('collagedata.xlsx')