import xlrd

#  Read from the excel file
excel_path = ".\..\..\data\\excel_files\\test.xlsx"

def main():

    book = xlrd.open_workbook(excel_path)
    print(book.nsheets)
    print(book.sheet_names())
    first_sheet = book.sheet_by_name('TestResult')
    first_sheet = book.sheet_by_index(0)
    print(first_sheet.row_values(3))
    print(first_sheet.cell(2,2))
    print(first_sheet.cell(2,2).value)
    for row in range(5):
        print("\n")
        for column in range(5):
            cell = first_sheet.cell(row, column)
            print(cell.value, end=' ')


if __name__ == "__main__":
    main()
