import xlrd

file_loc = "C:\\Users\\ROHAN\\Desktop\\Automation.xlsx"
wb = xlrd.open_workbook(file_loc)
ws = wb.sheet_by_index(0)
wc = ws.cell_value(0,0)
print(wc)





