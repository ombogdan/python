import csv

f1 = open("../LandBank/Земельний/Бурімка.csv", 'r', encoding='utf_8', errors='ignore')
f2 = open("data_csv_file.csv", 'r', encoding='utf8')

string = f1.readlines()
file = open("data.csv", "w", encoding="utf-8")
for i in string:
    if not i.isspace():
        str = i.replace('","', '","')
        print(i)
        file.write(str)
file.close()

# with open('../LandBank/Земельний/Бурімка.csv', 'r', encoding="utf-8", errors='ignore') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=';', header = None, sep='delimiter')
#     line_count = 0
#     for row in csv_reader:
#         # if line_count == 0:
#         #     print(f'Column names are {", ".join(row)}')
#         #     line_count += 1
#         # else:
#         # print(row[4])
#         # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#         line_count += 1
#     print(f'Processed {line_count} lines.')

# import xlrd
#
# workbook = xlrd.open_workbook('../LandBank/Земельний/Бурімка.xlsx', header = None, sep='delimiter')
# sheet = workbook.sheet_by_index(0)
#
# for rowx in range(sheet.nrows):
#     values = sheet.row_values(rowx)
#     print(values)
