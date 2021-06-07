import csv
import json
import re
from datetime import datetime


def getDate(rows):
    day_to = str(rows[i][11]).replace('"', '').replace('.0', '')
    month_to = str(rows[i][12]).replace('"', '').replace('.0', '')
    year_to = str(rows[i][13]).replace('"', '').replace('.0', '')

    date_to_str = year_to + '-' + month_to + '-' + day_to

    contract_reestration_date = ""
    if (len(year_to) == 1):
        contract_date_to = ""
    elif (len(day_to) != 0 and len(month_to) == 0 and len(year_to) == 0):
        print(day_to)
        dt = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + int(day_to) - 2)
        contract_date_to = dt.strftime('%Y-%m-%d')
    elif (len(day_to) != 0 and len(month_to) != 0 and len(year_to) != 0):
        contract_date_to = datetime.strptime(date_to_str, '%Y-%m-%d').date()
    else:
        contract_date_to = ""


def getOwnershipDocument(data):
    array = data.split(' від ')
    return array


def getPercent(percentStr1, percentStr2):
    if (percentStr1 == ''):
        # percent = round(eval(percentStr2))*100
        return None
    else:
        percent = round(eval(percentStr1))
        return percent


def floatHourToTime(fh):
    h, r = divmod(fh, 1)
    m, r = divmod(r * 60, 1)
    return (
        int(h),
        int(m),
        int(r * 60),
    )


with open('kadastrList.txt', encoding='utf8') as File:
    reader = list(csv.reader(File, skipinitialspace=True))
    arr = []
    arr_kad = []
    right1_fio = []
    right2_fio = []
    rows = []
    z =1;
    for row in reader:
        rows.append(row)
    for i in range(len(rows)):
        # print(rows[i])
        print(rows[i][0])
        result = rows[i][0].split(sep=" ")
        # print(result)

        d = {}
        fio_arr = []
        ownershipList = []
        ownership = {}
        owner = {}

        d['lat'] = result[1]
        d['lon'] = result[0]
        # d['name'] = '{z}'.format(z=z)
        arr.append(d)
        z = z + 1
    # print(arr)

    file = open("result.json", "w", encoding="utf-8")
    file.write(json.dumps(arr, ensure_ascii=False))
    file.close()
    # print(json.dumps(arr, ensure_ascii=False))
