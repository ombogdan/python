import csv

import xlrd


def csv_from_excel():
    wb = xlrd.open_workbook('./Озеряне МЧ.xls', encoding_override='cp1252')
    sh = wb.sheet_by_name('Sheet1')
    your_csv_file = open('data.csv', 'w', encoding='utf-8')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()
    delete_blank_deadlines()


def delete_blank_deadlines():
    csv = open('data.csv', encoding='utf-8')
    string = csv.readlines()
    csv.close()
    file = open("data.csv", "w", encoding="utf-8")
    for i in string:
        if not i.isspace():
            str = i.replace('\n', '')
            print(str)
            file.write(str+"\n")
    file.close()

csv_from_excel()
