import csv
import json
import re
from datetime import datetime

with open('../parser_xlsx/parser/data.csv', encoding='utf8') as File:
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
        kadastr_number = str(rows[i][7])

        right1_fio = str(rows[i][2])
        right1_inn = str(rows[i][3]).replace(".0", "")
        # exit(0)
        right1_passport = str(rows[i][4])
        right1_address = str(rows[i][5])
        right1_phone = None
        if (right1_phone == ''):
            right1_phone = None
        ownership_document_data = str(rows[i][6])


        right1_number = None
        right1_date_reestration = None
        square = str(rows[i][8])
        if(str(rows[i][19])!=""):
            if(str(rows[i][19])==str(rows[i-1][19])):
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

            pecuniary_valuation = str(rows[i][16])
            if (pecuniary_valuation == ''):
                pecuniary_valuation = None
            # else:
            # pecuniary_valuation = pecuniary_valuation.replace(',', '')
            contract_dateSTR = str(rows[i][17])
            if contract_dateSTR == '':
                contract_date = None
            else:
                findDate = re.findall('\d{2}.\d{2}.\d{4}', str(contract_dateSTR))
                if (len(findDate) > 0):
                    contract_date = findDate[0]
                else:
                    dt = datetime.fromordinal(
                        datetime(1900, 1, 1).toordinal() + int(str(contract_dateSTR).replace(".0", "")) - 2)
                    contract_date = dt.strftime('%d.%m.%Y')

            contract_date_reestrationSTR = rows[i][20]
            if contract_date_reestrationSTR == '':
                contract_date_reestrationSTR = rows[i][18]
            else:
                findDate = re.findall('\d{2}.\d{2}.\d{4}', str(contract_date_reestrationSTR))
                if len(findDate) > 0:
                    contract_date_reestration = findDate[0]
                else:
                    dt = datetime.fromordinal(
                        datetime(1900, 1, 1).toordinal() + int(str(contract_date_reestrationSTR).replace(".0", "")) - 2)
                    contract_date_reestration = dt.strftime('%d.%m.%Y')

            if (contract_date_reestration == ''):
                contract_date_reestration = None

            contract_number = str(rows[i][19]).replace('.0', '')
            # contract_number = None
            if (contract_number == ''):
                contract_number = None
            else:
                contract_number = contract_number

            right2_date_reestration = None

            if (right2_date_reestration == ''):
                right2_date_reestration = None

            contract_date_toSTR = str(rows[i][22])

            if (contract_date_toSTR == ''):
                contract_date_to = None
            else:
                findDate = re.findall('\d{2}.\d{2}.\d{4}', str(contract_date_toSTR))
                if (len(findDate) > 0):
                    contract_date_to = findDate[0]
                else:
                    dt = datetime.fromordinal(
                        datetime(1900, 1, 1).toordinal() + int(str(contract_date_toSTR).replace(".0", "")) - 2)
                    contract_date_to = dt.strftime('%d.%m.%Y')

            right2_fio = None
            right2_inn = None

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

            arr.append(d)

    file = open("data.json", "w", encoding="utf-8")
    file.write(json.dumps(arr, ensure_ascii=False))
    file.close()
    # print(json.dumps(arr, ensure_ascii=False))
