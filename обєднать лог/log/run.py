import re

rows = []
rowsLogin = []
with open('login.txt', encoding='utf8') as FileTXT:
    readLogin = FileTXT.readlines()

    for row in readLogin:
        rowsLogin.append(row)
with open('collective_login.log', encoding='utf8') as File:
    read = File.readlines()
    for rowq in read:
        rows.append(rowq)
    for l in range(len(rows)):
        res = rows[l].split(sep="\n")
        # print(res)
        # exit(0)

        for l in range(len(rowsLogin)):
            resLogin = rowsLogin[l].replace("\"", "").split(sep="\n")

            if len(re.findall("login="+resLogin[0], res[0])) > 0 and len(re.findall("ERROR", res[0])) == 0:
                # exit(0)
                file = open("login.log", "a", encoding="utf-8")
                file.write(res[0] + "\n")
                file.close()
