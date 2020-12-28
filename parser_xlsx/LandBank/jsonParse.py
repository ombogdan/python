import csv
import json
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
        percent = round(eval(percentStr2))*100
        return percent
    else:
        percent = round(eval(percentStr1))*100
        return percent


with open('../parser/data.csv', encoding='utf8') as File:
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
        owershipList = []
        owership = {}
        owner = {}

        record_id = str("add id")
        kadastr_number = str(rows[i][8])
        square = str(rows[i][9])
        pecuniary_valuation = str(rows[i][19])
        if(pecuniary_valuation==''):
            pecuniary_valuation = None
        else:
            pecuniary_valuation = pecuniary_valuation.replace(',', '')
        contract_date = str(rows[i][20])
        contract_date_reestration = str(rows[i][21])
        contract_number = str(rows[i][22])
        right2_date_reestration = str(rows[i][23])
        if(right2_date_reestration==''):
            right2_date_reestration = None
        contract_date_to = str(rows[i][25])


        d['kadastr_number'] = kadastr_number
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
        d["right2_inn"] = None
        d["right2_date_reestration"] = right2_date_reestration
        d["right2_number"] = None
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

        right1_fio = str(rows[i][2])
        right1_inn = str(rows[i][3])
        right1_passport = str(rows[i][4])
        right1_phone = None
        right1_address = str(rows[i][5])
        ownership_document_data = getOwnershipDocument(str(rows[i][7]))
        percent = getPercent(str(rows[i][14]), str(rows[i][12]))
        # print(percent)

        owership["right1_fio"] = right1_fio
        owership["right1_inn"] = right1_inn
        owership["right1_date_reestration"] = ownership_document_data[1]
        owership["right1_number"] = None
        owership["right1_reestration_organization"] = None
        owership["right1_passport"] = right1_passport
        owership["right1_address"] = right1_address
        owership["right1_phone"] = right1_phone
        owership["right1_note"] = None
        owership["birthday"] = None
        owership["gender"] = None
        owership["ownership_document"] = ownership_document_data[0]
        owership["ownership_type_detail"] = None
        owership["bank_share_id"] = None
        owership["percent"] = percent
        d["owership"] = owership

        arr.append(d)

    print(json.dumps(arr, ensure_ascii=False))
