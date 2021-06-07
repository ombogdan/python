import csv
import json
from datetime import datetime

from dateutil import parser



with open('./Земельний/Ічнянська міська рада/Ічнянська міська рада _ 26.05.2021 12_26_34 - довiдки.json', encoding='utf8') as File:
    reader = list(File)
    jsonList = json.loads(reader[0])
    arr = []
    arr_kad = []
    right1_fio = []
    right2_fio = []
    rows = []
    for i in range(len(jsonList)):
        d = {}
        fio_arr = []
        ownershipList = []
        ownership = {}
        owner = {}
        irps = None
        if (jsonList[i]['RrpAdvanced'] != None and jsonList[i]['RrpAdvanced']['realty'] != None and len(jsonList[i]['RrpAdvanced']['realty'])>0):
            RrpAdvanced = jsonList[i]['RrpAdvanced']['realty'][0]
            # все шо в ірпс це right2
            if (RrpAdvanced['irps'] != None and len(RrpAdvanced['irps'])>0):
                irps = RrpAdvanced['irps'][0]

        OwnershipInfoList = []
        if (jsonList[i]['Plot']['dzkLandInfo'] != None and jsonList[i]['Plot']['dzkLandInfo']['OwnershipInfo'] != None):
            OwnershipInfoList = jsonList[i]['Plot']['dzkLandInfo']['OwnershipInfo']
        for o in range(len(OwnershipInfoList)):
            item = OwnershipInfoList[o]

            right1_number = None
            right1_date_reestration = None
            name = item['NameFo']

            ownership["right1_fio"] = name
            ownership["right1_inn"] = None
            ownership["right1_date_reestration"] = item['DateRegRight']
            ownership["right1_number"] = item['EntryRecordNumber']
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
            ownership["percent"] = geoJsonList['features'][i]['properties']['dzkPercnOwn']
            ownershipList.append(ownership)
            d["ownership"] = ownershipList
            ownership = {}

        # if (jsonList[i]['CadastrNumber'] == '5322681100:00:007:0009'):
        pecuniary_valuation = ''
        if (pecuniary_valuation == ''):
            pecuniary_valuation = None
        # else:
        # pecuniary_valuation = pecuniary_valuation.replace(',', '')

        contract_date_to = jsonList[i]

        # Purpose Id
        if (jsonList[i]['Plot']['dzkLandInfo'] != None and jsonList[i]['Plot']['dzkLandInfo']['Purpose'] != None):
            purpose = jsonList[i]['Plot']['dzkLandInfo']['Purpose']
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
        # ------------------------------

        # ---------irps------------------
        right2_number = None
        contract_date_reestration = None
        contract_date_to = None
        if (irps != None):
            right2_number = irps['rnNum']
            contract_date_reestration = parser.isoparse(irps['regDate']).date().strftime('%d.%m.%Y')
            if (geoJsonList['features'][i]['properties']['endDate'] != None):
                contract_date_to = datetime.strptime(geoJsonList['features'][i]['properties']['endDate'],
                                                     '%d.%m.%Y:%H:%M:%S').strftime('%d.%m.%Y')

        right2_fio = None
        right2_reestration_organization = None
        right2_inn = None
        if (jsonList[i]['Plot']['dzkLandInfo'] != None and jsonList[i]['Plot']['dzkLandInfo']['SubjectRealRightLand'] != None):
            right2_fio = jsonList[i]['Plot']['dzkLandInfo']['SubjectRealRightLand'][0]['NameUo']
            right2_reestration_organization = jsonList[i]['Plot']['dzkLandInfo']['SubjectRealRightLand'][0]['NameUo']
            right2_inn = jsonList[i]['Plot']['dzkLandInfo']['SubjectRealRightLand'][0]['Edrpou']
        if (right2_fio == None):
            if (jsonList[i]['Plot']['rrpLandInfo']['subject'] != None):
                right2_fio = jsonList[i]['Plot']['rrpLandInfo']['subject'][0]['name']

        if (right2_inn == None):
            if (jsonList[i]['Plot']['rrpLandInfo']['subject'] != None):
                right2_inn = jsonList[i]['Plot']['rrpLandInfo']['subject'][0]['code']

        if (right2_fio == None):
            if (jsonList[i]['Plot']['dzkLandInfo'] !=None and jsonList[i]['Plot']['dzkLandInfo']['SubjectRealRightLand'] != None):
                right2_fio = jsonList[i]['Plot']['dzkLandInfo']['SubjectRealRightLand'][0]['NameFo']
        d["right2_number"] = right2_number
        d["bank_right2type_id"] = None
        d["right2_type"] = None
        d["right2_fio"] = right2_fio
        d["right2_inn"] = right2_inn
        d["right2_date_reestration"] = None
        d["right2_reestration_organization"] = None
        # -------------------------------
        # exit(0)
        d['kadastr_number'] = jsonList[i]['CadastrNumber']
        d['pecuniary_valuation'] = None
        # pecuniary_valuation це нго ngo
        d["square"] = round(jsonList[i]['Plot']['area'], 2)
        d["square_count"] = None
        d['bank_region_id'] = None
        d['bank_district_id'] = None
        d['geozone_id'] = None
        d["organization_id"] = None
        d["bank_city_id"] = None
        contract_date = None
        if (irps != None):
            supplementary = False
            for l in range(len(irps['causeDocuments'])):
                if (irps['causeDocuments'][l]['cdType'] == 'договір оренди землі'):
                    contract_date = parser.isoparse(irps['causeDocuments'][l]['docDate']).date().strftime('%d.%m.%Y')

                if (irps['causeDocuments'][l]['cdTypeExtension'] == 'додаткова угода'):
                    supplementary = True

            if (supplementary == True):
                for l in range(len(irps['causeDocuments'])):
                    if (irps['causeDocuments'][l]['cdTypeExtension'] == 'додаткова угода'):
                        contract_date = parser.isoparse(irps['causeDocuments'][l]['docDate']).date().strftime(
                            '%d.%m.%Y')

        d["contract_number"] = None
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
        d["bank_purpose_id"] = purposeId
        d["bank_ownership_id"] = None
        d["ownership_document"] = None
        d["bank_village_council_id"] = None
        d["size"] = None
        d["koatuu"] = jsonList[i]['Plot']['koatuu']
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
        for h in range(len(geoJsonList['features'][i]['geometry']['coordinates'][0])):
            item = geoJsonList['features'][i]['geometry']['coordinates'][0][h]

            for c in range(len(item)):
                coordinates.append({'lat': item[c][1],
                                    'lon': item[c][0]})
        # exit(0)

        d["coordinates"] = coordinates
        if (d['right2_inn'] == None):
            print(d)
        arr.append(d)
    # print(len(arr))
    # print('len(arr)')
    file = open("./Земельний/Ічнянська міська рада/result.json", "w", encoding="utf-8")
    file.write(json.dumps(arr, ensure_ascii=False))
    file.close()
