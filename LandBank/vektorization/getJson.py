import csv
import json
import math

import numpy


def getCoords(x, y):
    lon = (x / 20037508.34) * 180
    lat = (y / 20037508.34) * 180
    lat = 180 / math.pi * (2 * math.atan(math.exp(lat * math.pi / 180)) - math.pi / 2)
    return round(lat, 7), round(lon, 7)

with open('./Мичурина/get-object-info.txt', encoding='utf8') as File:
    reader = File.readlines()
    arr = []
    arr_kad = []
    right1_fio = []
    right2_fio = []
    rows = []

    for row in reader:
        rows.append(row)
    for i in range(len(rows)):

        result = rows[i].split(sep=";")
        resultJson = json.loads(result[1])

        d = {}
        fio_arr = []
        ownershipList = []
        ownership = {}
        owner = {}
        kadastr_number = str(result[0])


        ownership["right1_fio"] = None
        ownership["right1_inn"] = None
        ownership["right1_date_reestration"] = None
        ownership["right1_number"] = None
        ownership["right1_reestration_organization"] = None
        ownership["right1_passport"] = None
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

        #/////////////
        # print(type(resultJson[0]))
        purpose = resultJson[0]['purpose']
        purposeId = None
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
        #/////////////

        d['kadastr_number'] = kadastr_number
        d['pecuniary_valuation'] = None
        # pecuniary_valuation це нго ngo
        d["square"] = resultJson[0]['area']
        d["square_count"] = None
        d['bank_region_id'] = None
        d['bank_district_id'] = None
        d['geozone_id'] = None
        d["organization_id"] = None
        d["bank_right2type_id"] = None
        d["bank_city_id"] = None
        d["right2_type"] = None
        d["right2_fio"] = None
        d["right2_inn"] = None
        d["right2_date_reestration"] = None
        d["right2_number"] = None
        d["right2_reestration_organization"] = None
        d["contract_number"] = None
        d["contract_date"] = None
        d["contract_date_reestration"] = None
        d["contract_date_to"] = None
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
        d["koatuu"] = resultJson[0]['koatuu']
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
        with open('./Мичурина/find-parcel.txt', encoding='utf8') as Fil:
            center_data = {}
            read = Fil.readlines()

            for rowq in read:
                rowsq.append(rowq)
            for l in range(len(rowsq)):
                res = rowsq[l].split(sep=";")
                # print(res[0])
                if kadastr_number == res[0]:
                    try:
                        coord = eval(res[1])

                        x_max, y_max = getCoords(float(coord['st_xmax']), float(coord['st_ymax']))
                        x_min, y_min = getCoords(float(coord['st_xmin']), float(coord['st_ymin']))
                        coords = (x_max, x_min, y_max, y_min)

                        centerx, centery = (numpy.average(coords[:2]), numpy.average(coords[2:]))
                        center_data['lat'] = centerx
                        center_data['lon'] = centery
                        d["coordinates"] = [center_data]
                        # print(kadastr_number)
                        # print('kadastr_number')
                    except:
                        print(res[1])
                        d["coordinates"] = None

                    # coords = json.loads(res[2])
                    # print(coords)
                    # d["coordinates"] = coords

        arr.append(d)
    # print(arr)
    file = open("result1Мичурина.json", "w", encoding="utf-8")
    file.write(json.dumps(arr, ensure_ascii=False))
    file.close()
    # print(json.dumps(arr, ensure_ascii=False))
