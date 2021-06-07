A = []
file = open('kadastr_number.txt', encoding='utf8')
string = file.readlines()
for str in string:
    # A.append(str)
    A.append(str.replace("\n", "").replace("\ufeff", '').replace("\xa0", ''))
    # print(str)
# print(A)
counter = {}

for elem in A:
    # print(elem)
    counter[elem] = counter.get(elem, 0) + 1

doubles = {element: count for element, count in counter.items() if count > 1}

print(doubles)