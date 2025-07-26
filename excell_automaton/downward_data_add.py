from openpyxl import Workbook,load_workbook
wb=Workbook()
ws=wb.active
ws.append(['ashis','20','bca','3','bca_new'])
ws.append(['mohit','19','bca','3','bca_new'])
ws.append(['pawan','18','bca','3','bca_new'])
ws.append(['nikhli','17','bca','3','bca_new'])
wb.save(r'C:\Users\ashis\OneDrive\Desktop\Data Automation\collagedata.xlsx')