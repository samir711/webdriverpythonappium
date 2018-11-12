import xlwt
 
#----------------------------------------------------------------------
def main():
    #""""""
    book = xlwt.Workbook()
    sheet1 = book.add_sheet("PySheet1")
 
    for num in range(5): #rows
        row = sheet1.row(num)
        for index in range(5):  #cols
            value=(num)*10
            row.write(index, value) #index is where we want to write in the row, and value is the data created
 
    book.save("D:\\Eclipse\\workspace\\PythonWithAppium\\PythonProject\\datasets\\test.xlsx")
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    main()