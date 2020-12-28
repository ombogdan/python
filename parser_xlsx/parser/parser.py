import csv

import xlrd


def csv_from_excel():
    wb = xlrd.open_workbook('../data/СВК Струмок ОСГ (АТО).xlsx', encoding_override='utf-8')
    sh = wb.sheet_by_name('Чапаївська ')
    your_csv_file = open('../еуеі/data_Чапаївська_file1.csv', 'w', encoding='utf-8')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()
    # f1 = open("data_becon_file.csv", 'r', encoding='utf8')
    # f2 = open("data_becon_file1.csv", 'w', encoding='utf8')
    # for line in f1.readlines():
    #     if ''.join(line.split(',')):
    #         continue
    #     f2.write(line)


csv_from_excel()
