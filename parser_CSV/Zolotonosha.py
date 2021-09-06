import csv
import json

with open('data-1629958361391.csv', encoding='utf8') as File:
    reader = csv.reader(File,
                        # delimiter=',',
                        # quotechar=',',
                        # quoting=csv.QUOTE_MINIMAL
                        )
    arr = []
    arr_kad = []
    right1_fio = []
    right2_fio = []
    rows = []
    for row in reader:
        rows.append(row)
    for i in range(len(rows)):
        print(rows[i][0])
        print(rows[i][1])
        print(rows[i][2])
        paramsJson = json.loads(rows[i][2])
        file = open("./result.csv", "a", encoding="utf-8")
        if (rows[i][3] == 'NULL'):
            file.write('"' + rows[i][0] + '";"' + rows[i][1] + '";"' + str(paramsJson['filter_dut']) + '";"' + str(
                paramsJson['refueling']) + '";"' +
                       str(paramsJson['drain']) + '";' + rows[i][3] + "\n")
        else:
            file.write('"' + rows[i][0] + '";"' + rows[i][1] + '";"' + str(paramsJson['filter_dut']) + '";"' + str(
                paramsJson['refueling']) + '";"' +
                       str(paramsJson['drain']) + '";"' + rows[i][3] + '"\n')
        file.close()
