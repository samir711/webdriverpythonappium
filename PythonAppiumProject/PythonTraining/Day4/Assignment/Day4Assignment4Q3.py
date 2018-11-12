# Q3. Find out the pypi module available which can be used to perform the following activity -
#
# a. read and write excel file
# b. generate logs.

# Excel packages packages such as pandas, openpyxl, xlrd, xlutils and pyexcel.
# https://www.geeksforgeeks.org/reading-excel-file-using-python/


import xlrd  # a. read and write excel file

# location of the file

loc = ".\..\..\data\data.xlsx"

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# For row 0 and column 0
print(sheet.cell_value(0, 0))
