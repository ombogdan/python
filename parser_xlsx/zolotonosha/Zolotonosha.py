import csv
import json
from datetime import datetime
from decimal import Decimal


def check_value(value):
    ngo_f = None
    try:
        ngo_f = float(value)
        return ngo_f
    except ValueError:
        ngo_s = str(ngo_f)
        if (ngo_f == None or value != ngo_s):
            value = 0
            return float(value)

def check_value_inn(value):
    ngo_f = None
    try:
        ngo_f = int(value)
        return ngo_f
    except ValueError:
        ngo_s = str(ngo_f)
        if (ngo_f == None or value != ngo_s):
            value = 0
            return int(value)


def check_string_value(value):
    if (len(value) != 0):
        return value
    else:
        return ''


def floatHourToTime(fh):
    h, r = divmod(fh, 1)
    m, r = divmod(r * 60, 1)
    return (
        int(h),
        int(m),
        int(r * 60),
    )


with open('data_zolot_file.csv', encoding='utf8') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
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
        kadastr_number = str(rows[i][4]).replace('"', '')

        fio = str(rows[i][1]).replace('"', '')
        inn_str = str(rows[i][48]).replace('"', '').replace('.0', '')
        series = str(rows[i][44]).replace('"', '')
        date_of_issue = str(rows[i][46]).replace('"', '').replace('.0', '')
        issued_by = str(rows[i][47]).replace('"', '')
        passport_number = str(rows[i][45]).replace('"', '').replace('.0', '')
        address_of_residence1 = str(rows[i][49]).replace('"', '')
        try:
            address_of_residence2 = str(rows[i][50]).replace('"', '')
        except:
            address_of_residence2 = ''

        ngo = str(rows[i][6]).replace('"', '')
        square = str(rows[i][5]).replace('"', '')
        percent_str = str(rows[i][34]).replace('"', '')
        bank_village = str(rows[i][35]).replace('"', '')
        right2_number = str(rows[i][29]).replace('"', '').replace('.0', '')#right2_number - № запису про ІРП
        # number = str(rows[i][22]).replace('"', '').replace('.0', '')
        number = str(rows[i][28]).replace('"', '').replace('.0', '')
        contract_number = str(rows[i][27]).replace('"', '').replace('.0', '')#ownership_document - Реєстраційний № обєкта переробив на contract_number

        day_reestration = str(rows[i][23]).replace('"', '').replace('.0', '')
        month_reestration = str(rows[i][24]).replace('"', '').replace('.0', '')
        year_reestration = str(rows[i][25]).replace('"', '').replace('.0', '')

        if (len(day_reestration) == 0 and len(month_reestration) == 0 and len(year_reestration) != 0):
            month_reestration = '1'
            day_reestration = '1'
            date_reestration_str = year_reestration + '-' + month_reestration + '-' + day_reestration
        else:
            date_reestration_str = year_reestration + '-' + month_reestration + '-' + day_reestration

        day_to = str(rows[i][31]).replace('"', '').replace('.0', '')
        month_to = str(rows[i][32]).replace('"', '').replace('.0', '')
        year_to = str(rows[i][33]).replace('"', '').replace('.0', '')
        right2_fio = str(rows[i][3]).replace('"', '')

        date_to_str = year_to + '-' + month_to + '-' + day_to
        print(fio)
        if (len(year_reestration) != 0 and len(day_reestration) != 0 and len(month_reestration) != 0):
            contract_reestration_date = datetime.strptime(date_reestration_str, '%Y-%m-%d').date()
            contract_date_to = datetime.strptime(date_to_str, '%Y-%m-%d').date()

        if (len(percent_str) != 0):
            percent_d = Decimal(percent_str) * 100
            percent = float(percent_str)

        if (len(day_reestration) == 0 and len(month_reestration) == 0 and len(year_reestration) != 0):
            day_reestration = "1"
            month_reestration = "1"

        if (len(bank_village) != 0):
            bank_village_council = bank_village
        else:
            bank_village_council = ''

        if (len(right2_number) != 0):
            right2_number = right2_number
        else:
            right2_number = ''

        if (len(date_of_issue) != 0):
            print(date_of_issue)

            dt = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + int(date_of_issue) - 2)
            date_of_issue = dt.strftime('%Y-%m-%d')
        else:
            date_of_issue = ''


        if(len(date_of_issue)==0 and len(issued_by)==0):
            passport = series + " " + passport_number
        elif (len(issued_by)!=0 and len(series)==0):
            passport = date_of_issue + " " + issued_by
        elif (len(issued_by)==0):
            passport = series + "" + passport_number + ", " + date_of_issue
        elif (len(date_of_issue)==0):
            passport = series + "" + passport_number + ", " + issued_by
        else:
            passport = series + " " + passport_number + ", " + date_of_issue + ", " + issued_by

        if(len(address_of_residence2)==0 and len(address_of_residence1)==0):
            address = ""
        elif(len(address_of_residence2)==0):
            address = address_of_residence1
        elif (len(address_of_residence1) == 0):
            address = address_of_residence2
        else:
            address = address_of_residence1 + "," + address_of_residence2

        inn = check_value_inn(inn_str)

        if (len(kadastr_number) == 0):
            # arr[-1]["ownershipList"][0]["right1_fio"].append(fio)
            owership["fio"] = fio
            owership["number"] = check_string_value(number)
            owership["passport"] = passport
            owership['inn'] = inn
            owership['address'] = address
            arr[-1]["ownershipList"].append(owership)
            continue
        elif len(arr)>0 and arr[-1]["kadastr_number"] == kadastr_number:
            owership["fio"] = fio
            owership["number"] = check_string_value(number)
            owership["passport"] = passport
            owership['inn'] = inn
            owership['address'] = address
            arr[-1]["ownershipList"].append(owership)
            continue
        elif (len(fio) == 0):
            fio = arr[-1]["ownershipList"][0]["fio"]
            d['kadastr_number'] = kadastr_number
            owership["fio"] = fio
            owership["number"] = check_string_value(number)
            owership["passport"] = passport
            owership['inn'] = inn
            owership['address'] = address
            owershipList.append(owership)
            d["ownershipList"] = owershipList
            d['ngo'] = check_value(ngo)
            d['square'] = check_value(square)
            d['contract_reestration_date'] = str(contract_reestration_date)
            d['contract_date_to'] = str(contract_date_to)
            d['percent'] = percent
            d['bank_village_council'] = bank_village_council
            d['right2_number'] = right2_number
            d['right2_fio'] = check_string_value(right2_fio)
            d["contract_number"] = check_string_value(contract_number)

        else:
            fio_arr.append(fio)
            right1_fio.append(fio_arr)
            owership["fio"] = fio
            owership["number"] = check_string_value(number)
            owership["passport"] = passport
            owership['inn'] = inn
            owership['address'] = address
            owershipList.append(owership)
            d["ownershipList"] = owershipList
            d['kadastr_number'] = kadastr_number
            d["ngo"] = check_value(ngo)
            d["square"] = check_value(square)
            d["contract_reestration_date"] = str(contract_reestration_date)
            d["contract_date_to"] = str(contract_date_to)
            d['percent'] = percent
            d['bank_village_council'] = bank_village_council
            d['right2_number'] = right2_number
            d['right2_fio'] = check_string_value(right2_fio)
            d["contract_number"] = check_string_value(contract_number)
        arr.append(d)
        right1_fio.append(fio_arr)
    print(arr)
    print(json.dumps(arr, ensure_ascii=False))
