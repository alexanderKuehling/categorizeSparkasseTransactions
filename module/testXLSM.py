from openpyxl import *
wb = load_workbook("default.xlsm")
print(wb.worksheets[0].cell(1,1).value)