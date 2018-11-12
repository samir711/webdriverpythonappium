import xlwt

#  Works with only xls format not with xlsx format, Use openpyxl for xlsx
excel_path = ".\..\..\data\\excel_files\\test.xls"

def main():

    book = xlwt.Workbook()
    sheet1 = book.add_sheet("PySheet1")

    for num in range(5):
        row = sheet1.row(num)
        for column in range(5):
            value = num * 10
            row.write(column, value)

    book.save(excel_path)


if __name__ == "__main__":
    main()
