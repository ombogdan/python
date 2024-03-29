import csv
import json
import re
from datetime import datetime

import numpy
from numpy.lib import math

def getCoords(x, y):
    lon = (x / 20037508.34) * 180
    lat = (y / 20037508.34) * 180
    lat = 180 / math.pi * (2 * math.atan(math.exp(lat * math.pi / 180)) - math.pi / 2)
    return round(lat, 7), round(lon, 7)


with open('../Дані з ДРРП (pdf)/data.csv', encoding='utf8') as File:
    reader = list(csv.reader(File, skipinitialspace=True))
    arr = []
    arr_kad = []
    right1_fio = []
    right2_fio = []
    rows = []
    for row in reader:
        rows.append(row)
    for i in range(len(rows)):
        d = {}
        fio_arr = []
        ownershipList = []
        ownership = {}
        owner = {}
        rowsObjectInfo = []
        with open('../Дані з ДРРП (pdf)/get-object-info.txt', encoding='utf8') as ObjectInfo:
            reader1 = ObjectInfo.readlines()
            for row in reader1:
                rowsObjectInfo.append(row)

        kad_number = str(rows[i][0])
        if kad_number != " ":
            exist = False
            for o in range(len(arr)):
                if (kad_number == arr[o]['kadastr_number']):
                    ownership["right1_fio"] = str(rows[i][0])
                    ownership["right1_inn"] = str(rows[i][3])
                    ownership["right1_date_reestration"] = None
                    ownership["right1_number"] = str(rows[i][14])
                    ownership["right1_reestration_organization"] = None
                    ownership["right1_passport"] = str(rows[i][2])
                    ownership["right1_address"] = None
                    ownership["right1_phone"] = None
                    ownership["right1_note"] = None
                    ownership["birthday"] = None
                    ownership["gender"] = None
                    ownership["ownership_document"] = None
                    ownership["ownership_type_detail"] = None
                    ownership["bank_share_id"] = None
                    ownership["percent"] = None
                    arr[o]["ownership"].append(ownership)
                    exist = True
                    continue

            if exist == True:
                continue
            else:
                ownership["right1_fio"] = str(rows[i][0])
                ownership["right1_inn"] = str(rows[i][3])
                ownership["right1_date_reestration"] = None
                ownership["right1_number"] = str(rows[i][14])
                ownership["right1_reestration_organization"] = None
                ownership["right1_passport"] = str(rows[i][2])
                ownership["right1_address"] = None
                ownership["right1_phone"] = None
                ownership["right1_note"] = None
                ownership["birthday"] = None
                ownership["gender"] = None
                ownership["ownership_document"] = None
                ownership["ownership_type_detail"] = None
                ownership["bank_share_id"] = None
                ownership["percent"] = None
                ownershipList.append(ownership)
                d["ownership"] = ownershipList

            square = None
            koatuu = None
            purposeId = None
            purpose = None
            for q in range(len(rowsObjectInfo)):
                result = rowsObjectInfo[q].split(sep=";")
                resultJson = json.loads(result[1])
                if (result[0] == kad_number):
                    square = resultJson[0]['area']
                    koatuu = resultJson[0]['koatuu']
                    purpose = resultJson[0]['purpose']

            if (purpose == "01.01 Для ведення товарного сільськогосподарського виробництва"):
                purposeId = 1
            elif (purpose == "01.02 Для ведення фермерського господарства"):
                purposeId = 2
            elif (purpose == "01.03 Для ведення особистого селянського господарства"):
                purposeId = 3
            elif (purpose == "01.04 Для ведення підсобного сільського господарства"):
                purposeId = 4
            elif (purpose == "01.05 Для індивідуального садівництва"):
                purposeId = 5
            elif (purpose == "01.06 Для колективного садівництва"):
                purposeId = 6
            elif (purpose == "01.07 Для городництва"):
                purposeId = 7
            elif (purpose == "01.08 Для сінокосіння і випасання худоби"):
                purposeId = 8
            elif (purpose == "01.09 Для дослідних і навчальних цілей"):
                purposeId = 9

            d['kadastr_number'] = kad_number
            d['pecuniary_valuation'] = None
            # pecuniary_valuation це нго ngo
            d["square"] = square
            d["square_count"] = None
            d['bank_region_id'] = None
            d['bank_district_id'] = None
            d['geozone_id'] = None
            d["organization_id"] = None
            d["bank_right2type_id"] = None
            d["bank_city_id"] = None
            d["right2_type"] = None
            d["right2_fio"] = None
            d["right2_inn"] = 32232152
            d["right2_name"] = "ТОВ \"ВКФ \"Мелітопольська черешня"
            d["right2_date_reestration"] = None
            d["right2_number"] = None
            d["right2_reestration_organization"] = None
            d["contract_number"] = str(rows[i][5])
            contract_date = None
            if (str(rows[i][7]) != ""):
                contract_date_format1 = datetime.strptime(str(rows[i][7]), '%d.%m.%y')
                contract_date = datetime.strftime(contract_date_format1, "%m.%d.%Y")
                result_contract_date = datetime.strptime(contract_date, "%m.%d.%Y")
                str_contract_date = None
                if result_contract_date.year < 2000:
                    date_contract_date = result_contract_date.replace(year=result_contract_date.year + 100)
                    str_contract_date = datetime.strftime(date_contract_date, "%m.%d.%Y")

            if(str_contract_date==None):
                d["contract_date"] = contract_date
            else:
                d["contract_date"] = str_contract_date

            contract_date_reestration = None
            if (str(rows[i][7]) != ""):
                contract_date_reestration_format1 = datetime.strptime(str(rows[i][7]), '%d.%m.%y')
                contract_date_reestration = datetime.strftime(contract_date_reestration_format1, "%m.%d.%Y")
                date_contract_date_reestration = datetime.strptime(contract_date_reestration, "%m.%d.%Y")
                str_contract_date_reestration = None
                if date_contract_date_reestration.year < 2000:
                    date_contract_date = date_contract_date_reestration.replace(year=date_contract_date_reestration.year + 100)
                    str_contract_date_reestration = datetime.strftime(date_contract_date, "%m.%d.%Y")
            if (str_contract_date_reestration == None):
                d["contract_date_reestration"] = contract_date_reestration
            else:
                d["contract_date_reestration"] = str_contract_date_reestration



            contract_date_to = None

            if (str(rows[i][8]) != ""):
                contract_date_to_format1 = datetime.strptime(str(rows[i][8]), '%d.%m.%y')
                contract_date_to = datetime.strftime(contract_date_to_format1, "%m.%d.%Y")
                date_contract_date_to = datetime.strptime(contract_date_to, "%m.%d.%Y")
                str_contract_date_to = None
                if date_contract_date_to.year < 2000:
                    date_contract_date = date_contract_date_to.replace(year=date_contract_date_to.year + 100)
                    str_contract_date_to = datetime.strftime(date_contract_date, "%m.%d.%Y")
            if (str_contract_date_to == None):
                d["contract_date_to"] = contract_date_to
            else:
                d["contract_date_to"] = str_contract_date_to

            d["contract_supplementary_date"] = None
            d["contract_supplementary_date_reestration"] = None
            d["contract_supplementary_date_to"] = None
            d["valuation_type"] = None
            d["pecuniary_valuation"] = None
            d["bank_organization_id"] = None
            d["contract_status"] = None
            d["contract_status_comment"] = None
            d["ownership_type_detail"] = None
            d["bank_purpose_id"] = purposeId
            d["bank_ownership_id"] = None
            d["ownership_document"] = None
            d["bank_village_council_id"] = None
            d["size"] = None
            d["koatuu"] = koatuu
            d["birthday"] = None
            d["gender"] = None
            d["amount"] = None
            d["rent"] = None
            d["rent_full"] = None
            d["rent_pdfo"] = None
            d["rent_pay"] = None
            d["bank_share_from_square"] = None
            d["bank_tenant_id"] = None

            rowsq = []
            with open('../Дані з ДРРП (pdf)/find-parcel.txt', encoding='utf8') as Fil:
                center_data = {}
                read = Fil.readlines()

                for rowq in read:
                    rowsq.append(rowq)
                for l in range(len(rowsq)):
                    res = rowsq[l].split(sep=";")
                    if kad_number == res[0]:
                        try:
                            coord = eval(res[1])

                            x_max, y_max = getCoords(float(coord['st_xmax']), float(coord['st_ymax']))
                            x_min, y_min = getCoords(float(coord['st_xmin']), float(coord['st_ymin']))
                            coords = (x_max, x_min, y_max, y_min)

                            centerx, centery = (numpy.average(coords[:2]), numpy.average(coords[2:]))
                            center_data['lat'] = centerx
                            center_data['lon'] = centery
                            d["coordinates"] = [center_data]
                        except:
                            d["coordinates"] = None

            arr.append(d)

    file = open("./Новенский с ВЕСЬ МЧ.json", "w", encoding="utf-8")
    # print(arr)
    file.write(json.dumps(arr, ensure_ascii=False))
    file.close()
