import json
import datetime as dt

with open('./ivankov.json') as File:
    jsonData = json.load(File)
    arr = []
    arr_kad = []
    right1_fio = []
    right2_fio = []
    rows = []
    for i in range(len(jsonData['features'])):
        item = jsonData['features'][i]
        d = {}
        fio_arr = []
        ownershipList = []
        ownership = {}
        owner = {}
        irps = None

        right1_number = None
        right1_date_reestration = None
        if (item['properties']['PARCEL_IMB_1C.Vlasnuk'] != None):
            ownership["right1_fio"] = item['properties']['PARCEL_IMB_1C.Vlasnuk']
        else:
            ownership["right1_fio"] = item['properties']['pkku.DZK_owners']
        ownership["right1_inn"] = item['properties']['PARCEL_IMB_1C.Vlasnuk_INN']
        ownership["right1_date_reestration"] = None
        ownership["right1_number"] = item['properties']['PARCEL_IMB_1C.Reestr_nomer']
        ownership["right1_reestration_organization"] = item['properties'][
            'PARCEL_IMB_1C.Reestr_mesto']  # -----------------------------------------------
        ownership["right1_passport"] = None
        ownership["right1_address"] = None
        ownership["right1_phone"] = None
        ownership["right1_note"] = None
        ownership["birthday"] = None
        ownership["gender"] = None
        ownership["ownership_document"] = None
        ownership["bank_share_id"] = None
        ownership["percent"] = None
        ownershipList.append(ownership)
        d["ownership"] = ownershipList
        ownership = {}

        # Purpose Id

        purpose = item['properties']['pkku.DZK_cil_prizn']
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

        d["right2_number"] = None
        d["bank_right2type_id"] = None
        if (item['properties']['pkku.PKKY_type_doc'] != 'Інформація відсутня' and item['properties'][
            'pkku.PKKY_type_doc'] != None):
            rec = item['properties']['pkku.PKKY_type_doc'].split(sep=", \n")
            d["right2_type"] = rec[0]
        else:
            d["right2_type"] = None

        if (item['properties']['PARCEL_MS_.Typ_vidobraj'] != 'Інформація відсутня' and item['properties'][
            'PARCEL_MS_.Typ_vidobraj'] != None):
            rec = item['properties']['PARCEL_MS_.Typ_vidobraj'].split(sep=", \n")
            d["right2_fio"] = rec[0]
            d["right2_inn"] = rec[0]
        else:
            d["right2_fio"] = None
            d["right2_inn"] = None

        # if (item['properties']['pkku.DZK_user_code'] != 'Інформація відсутня' and item['properties'][
        #     'pkku.DZK_user_code'] != None):
        #     rec = item['properties']['pkku.DZK_user_code'].split(sep=", \n")
        #     d["right2_inn"] = rec[0]
        # else:
        #     d["right2_inn"] = None

        if item['properties']['pkku.DZK_user_date_reestr'] != "Інформація відсутня" and item['properties'][
            'pkku.DZK_user_date_reestr'] != None:
            rec = item['properties']['pkku.DZK_user_date_reestr'].split(sep=", \n")
            d["right2_date_reestration"] = rec[0]
        else:
            d["right2_date_reestration"] = None
        d["right2_reestration_organization"] = None  # -------------------------Треба шось поставить
        d['kadastr_number'] = item['properties']['PARCEL_MS_.Kadastr_dzr']
        if (item['properties']['PARCEL_IMB_1C.Area_1C'] != None):
            d["square"] = round(item['properties']['PARCEL_IMB_1C.Area_1C'], 4)
        elif item['properties']['pkku.PKKY_plosha'] != None:
            d["square"] = round(item['properties']['pkku.PKKY_plosha'], 4)
        else:
            d["square"] = 0
        d["square_count"] = 0
        d['bank_region_id'] = None
        d['bank_district_id'] = None
        d['geozone_id'] = None
        d["organization_id"] = None
        d["bank_city_id"] = None
        d["contract_number"] = None
        if (item['properties']['PARCEL_IMB_1C.Date_pidpus'] != None and item['properties'][
            'PARCEL_IMB_1C.Date_pidpus'] != "Інформація відсутня"):
            d["contract_date"] = dt.datetime.fromtimestamp(
                int(item['properties']['PARCEL_IMB_1C.Date_pidpus']) / 1000).strftime('%d.%m.%Y')
        else:
            d["contract_date"] = None
        if item['properties']['PARCEL_IMB_1C.Date_reestr'] != None and item['properties'][
            'PARCEL_IMB_1C.Date_reestr'] != "Інформація відсутня":
            d["contract_date_reestration"] = dt.datetime.fromtimestamp(
                int(item['properties']['PARCEL_IMB_1C.Date_reestr']) / 1000).strftime(
                '%d.%m.%Y')  # -------------------------Треба шось поставить
        else:
            d["contract_date_reestration"] = None
        if item['properties']['PARCEL_IMB_1C.Date_zakinch'] and item['properties'][
            'PARCEL_IMB_1C.Date_zakinch'] != "Інформація відсутня":
            d["contract_date_to"] = dt.datetime.fromtimestamp(
                int(item['properties']['PARCEL_IMB_1C.Date_zakinch']) / 1000).strftime('%d.%m.%Y')
        else:
            d["contract_date_to"] = None
        d["contract_supplementary_date"] = None
        d["contract_supplementary_date_reestration"] = None
        d["contract_supplementary_date_to"] = None
        d["valuation_type"] = None
        if (item['properties']['PARCEL_IMB_1C.NGO'] != 0 and item['properties']['PARCEL_IMB_1C.NGO'] != None):
            d['pecuniary_valuation'] = item['properties']['Harvest_Work.DBO.PKKU_NEW_30.PKKY_NGO']
        else:
            d['pecuniary_valuation'] = item['properties']['PARCEL_IMB_1C.NGO_2012']
        d["bank_organization_id"] = None
        d["contract_status"] = None
        d["contract_status_comment"] = None
        d["ownership_type_detail"] = None
        d["bank_purpose_id"] = purposeId
        d["bank_ownership_id"] = None
        d["ownership_document"] = None
        d["bank_village_council_id"] = None
        d["size"] = None
        d["koatuu"] = item['properties']['PARCEL_IMB_1C.COATYY']
        d["birthday"] = None
        d["gender"] = None
        d["amount"] = None
        d["rent"] = None
        d["rent_full"] = None
        d["rent_pdfo"] = None
        d["rent_pay"] = None
        d["bank_share_from_square"] = None
        d["bank_tenant_id"] = None
        ownership["percent"] = item['properties']['PARCEL_IMB_1C.Proc_arend_pl']

        coordinates = []
        # print(item['geometry']['coordinates'])
        try:
            for h in range(len(item['geometry']['coordinates'])):
                record = item['geometry']['coordinates'][h]
                for c in range(len(record)):
                    coordinates.append({'lat': record[c][1],
                                        'lon': record[c][0]})
            d["coordinates"] = coordinates
        except:
            print(item['properties'])

        arr.append(d)
    file = open("./result.json", "w", encoding="utf-8")
    file.write(json.dumps(arr, ensure_ascii=False))
    file.close()
