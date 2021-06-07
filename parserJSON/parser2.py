import json
from datetime import datetime

from dateutil import parser
with open('forParsing.geojson', 'r', encoding='utf8') as j:
    contents = json.loads(j.read())
    print(contents['type'])
    arr = []
    for i in range(len(contents['features'])):
        jsonList = contents['features']
        d = {}
        fio_arr = []
        ownershipList = []
        ownership = {}
        owner = {}
        irps = None



        right1_number = None
        right1_date_reestration = None
        fio = str(jsonList[i]['properties']['rrpOwnName']).split(sep=';')

        for f in range(len(fio)):
            if(fio[f] != ''):
                ownership["right1_fio"] = str(fio[f])
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
                ownership["percent"] = jsonList[i]['properties']['dzkPercnOw']
                ownershipList.append(ownership)
            elif(fio[f] == 'None'):
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
                ownership["percent"] = jsonList[i]['properties']['dzkPercnOw']
                ownershipList.append(ownership)
        d["ownership"] = ownershipList
        ownership = {}

        # if (jsonList[i]['CadastrNumber'] == '5322681100:00:007:0009'):
        # ---------irps------------------
        right2_number = None
        contract_date_reestration = str(jsonList[i]['properties']['regDzkDate']).replace(";", '')
        contract_date_to = str(jsonList[i]['properties']['defEndDate']).replace(':00:00:00','').replace(";", '')
        if(contract_date_to=='01.01.0001'):
            contract_date_to = str(jsonList[i]['properties']['endDate']).replace(':00:00:00','').replace(";", '')

        right2_fio = jsonList[i]['properties']['holder']
        right2_reestration_organization = None
        right2_inn = None

        d["right2_number"] = right2_number
        d["bank_right2type_id"] = None
        d["right2_type"] = None
        d["right2_edrpou"] = jsonList[i]['properties']['code']
        d["right2_fio"] = right2_fio
        d["right2_inn"] = right2_inn
        d["right2_date_reestration"] = None
        d["right2_reestration_organization"] = None
        # -------------------------------
        # exit(0)
        d['kadastr_number'] = jsonList[i]['properties']['cadasrNumb']
        d['pecuniary_valuation'] = jsonList[i]['properties']['ngoPrice']
        # pecuniary_valuation це нго ngo
        d["square"] = jsonList[i]['properties']['areaPkku']
        d["square_count"] = None
        d['bank_region_id'] = None
        d['bank_district_id'] = None
        d['geozone_id'] = None
        d["organization_id"] = None
        d["bank_city_id"] = None
        contract_date = str(jsonList[i]['properties']['signDate']).replace(':00:00:00','').replace(";", '')

                # Purpose Id
        purpose = jsonList[i]['properties']['purpose']
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



        d["contract_number"] = None
        if(contract_date=='01.01.0001'):
            d["contract_date"] = None
        if(contract_date!='None'):
            d["contract_date"] = contract_date
        else:
            d["contract_date"] = None

        if (contract_date_reestration == "None"):
            d["contract_date_reestration"] = None
        elif(contract_date_reestration!=';'):
            d["contract_date_reestration"] = contract_date_reestration
        else:
            d["contract_date_reestration"] = None

        if(contract_date_to == ';'):
            d["contract_date_to"] = None
        if (contract_date_to != 'None'):
            d["contract_date_to"] = contract_date_to
        else:
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

        coordinates = []
        # print(jsonList[i]['geometry'])
        # print('jsonList')
        for h in range(len(jsonList[i]['geometry']['coordinates'][0])):
            item = jsonList[i]['geometry']['coordinates'][0][h]
            for c in range(len(item)):
                coordinates.append({'lat': item[c][1],
                                    'lon': item[c][0]})
                # print(coordinates)
        # exit(0)

        d["coordinates"] = coordinates
        arr.append(d)
    print('write')
    file = open("data.json", "w", encoding="utf-8")
    file.write(json.dumps(arr, ensure_ascii=False))
    file.close()
