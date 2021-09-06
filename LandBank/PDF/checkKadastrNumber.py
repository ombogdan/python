base_kadastr_number = []
my_kadastr_number = []
with open('./base_kadastr.txt', encoding='utf8') as Base:
    reader1 = Base.readlines()
    for row in reader1:
        base_kadastr_number.append(row)
with open('./kadastr_number.txt', encoding='utf8') as My:
    reader2 = My.readlines()
    for row1 in reader2:
        my_kadastr_number.append(row1)
for my_kadastr in my_kadastr_number:
    exist = False
    for base_kadastr in base_kadastr_number:
        if (base_kadastr == my_kadastr):
            exist = True
    if (exist == False):
        kadastr = open("exist_kadastr_number.txt", "a", encoding="utf-8")
        kadastr.write("'" + my_kadastr.replace("\n", "") + "',")
        kadastr.close()
