import csv
import json

# import numpy
import math

import numpy


def getCoords(x, y):
    lon = (x / 20037508.34) * 180
    lat = (y / 20037508.34) * 180
    lat = 180 / math.pi * (2 * math.atan(math.exp(lat * math.pi / 180)) - math.pi / 2)
    return round(lat, 7), round(lon, 7)


with open('kadastrList.txt', encoding='utf8') as File:
    reader = list(csv.reader(File, skipinitialspace=True))
    arr = []
    arr_kad = []
    right1_fio = []
    right2_fio = []
    rows = []
    for row in reader:
        rows.append(row)
    for i in range(len(rows)):
        result = rows[i][0].split(sep=";")

        d = {}
        fio_arr = []
        ownershipList = []
        ownership = {}
        owner = {}
        kadastr_number = str(result[0])

        right1_fio = str(result[7])
        right1_inn = None
        # exit(0)
        right1_passport = None
        right1_address = None
        right1_phone = None
        if (right1_phone == ''):
            right1_phone = None
        ownership_document_data = None
        percent = None
        if (percent == '1/3'):
            percent = 33.3
        elif (percent == '1/2'):
            percent = 50
        else:
            percent = 100
        # percent = None
        # print(percent)
        right1_number = result[1]
        right1_date_reestration = None
        square = str(result[8])

        if len(arr) > 0 and arr[-1]["kadastr_number"] == kadastr_number:
            square = float(arr[-1]["square"]) + float(rows[i][8])
            arr[-1]["square"] = square
            ownership["right1_fio"] = right1_fio
            ownership["right1_inn"] = right1_inn
            ownership["right1_date_reestration"] = right1_date_reestration
            ownership["right1_number"] = right1_number
            ownership["right1_reestration_organization"] = None
            ownership["right1_passport"] = right1_passport
            ownership["right1_address"] = right1_address
            ownership["right1_phone"] = right1_phone
            ownership["right1_note"] = None
            ownership["birthday"] = None
            ownership["gender"] = None
            ownership["ownership_document"] = ownership_document_data
            ownership["ownership_type_detail"] = None
            ownership["bank_share_id"] = None
            ownership["percent"] = percent
            arr[-1]["ownership"].append(ownership)
            continue
        else:
            ownership["right1_fio"] = right1_fio
            ownership["right1_inn"] = right1_inn
            ownership["right1_date_reestration"] = right1_date_reestration
            ownership["right1_number"] = right1_number
            ownership["right1_reestration_organization"] = None
            ownership["right1_passport"] = right1_passport
            ownership["right1_address"] = right1_address
            ownership["right1_phone"] = right1_phone
            ownership["right1_note"] = None
            ownership["birthday"] = None
            ownership["gender"] = None
            ownership["ownership_document"] = ownership_document_data
            ownership["ownership_type_detail"] = None
            ownership["bank_share_id"] = None
            ownership["percent"] = percent
            ownershipList.append(ownership)
        d["ownership"] = ownershipList

        pecuniary_valuation = None
        if (pecuniary_valuation == ''):
            pecuniary_valuation = None
        # else:
        # pecuniary_valuation = pecuniary_valuation.replace(',', '')
        contract_date = result[5]
        if contract_date == '':
            contract_date = None

        contract_date_reestration = result[3]

        if (contract_date_reestration == ''):
            contract_date_reestration = None

        contract_number = result[4]
        # contract_number = None
        if (contract_number == ''):
            contract_number = None
        else:
            contract_number = contract_number

        right2_date_reestration = None

        if (right2_date_reestration == ''):
            right2_date_reestration = None

        contract_date_to = result[6]

        if (contract_date_to == ''):
            contract_date_to = None

        right2_fio = None
        right2_inn = None
        right2_number = result[2]

        d['kadastr_number'] = kadastr_number
        d['pecuniary_valuation'] = pecuniary_valuation
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
        d["right2_fio"] = right2_fio
        d["right2_inn"] = right2_inn
        d["right2_date_reestration"] = right2_date_reestration
        d["right2_number"] = right2_number
        d["right2_reestration_organization"] = None
        d["contract_number"] = contract_number
        d["contract_date"] = contract_date
        d["contract_date_reestration"] = contract_date_reestration
        d["contract_date_to"] = contract_date_to
        d["contract_supplementary_date"] = None
        d["contract_supplementary_date_reestration"] = None
        d["contract_supplementary_date_to"] = None
        d["valuation_type"] = None
        d["pecuniary_valuation"] = pecuniary_valuation
        d["bank_organization_id"] = None
        d["contract_status"] = None
        d["contract_status_comment"] = None
        d["ownership_type_detail"] = None
        d["bank_purpose_id"] = None
        d["bank_ownership_id"] = None
        d["ownership_document"] = None
        d["bank_village_council_id"] = None
        d["size"] = None
        d["koatuu"] = None
        d["birthday"] = None
        d["gender"] = None
        d["amount"] = None
        d["rent"] = None
        d["rent_full"] = None
        d["rent_pdfo"] = None
        d["rent_pay"] = None
        d["bank_share_from_square"] = None
        d["bank_tenant_id"] = None
        # d["coordinates"] = []
        rowsq = []
        with open('pointList.txt', encoding='utf8') as Fil:
            center_data = {}
            read = Fil.readlines()

            for rowq in read:
                rowsq.append(rowq)
            for l in range(len(rowsq)):
                res = rowsq[l].split(sep=";")
                if(kadastr_number=='4823380400:05:000:0715'):
                    print("titit")
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
                        d["coordinates"] = None

        arr.append(d)
    # print(arr)
    file = open("result.json", "w", encoding="utf-8")
    file.write(json.dumps(arr, ensure_ascii=False))
    file.close()
    # print(json.dumps(arr, ensure_ascii=False))

