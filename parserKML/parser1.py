import simplekml

with open('Zones_13_14_10_19.txt', encoding='utf8') as File:
    reader = list(File)
    kml = simplekml.Kml()
    for i in range(len(reader)):
        dataArray = str(reader[i]).split(';')

        coordsStr = str(dataArray[3]).replace('POLYGON ((', '').replace('))', '').split(',')
        coordsArr = []
        for c in range(len(coordsStr)):
            arr = coordsStr[c].split(' ')
            coordsArr.append((float(arr[0]), float(arr[1])))
        # document.id = dataArray[0]
        pol = kml.newpolygon()
        pol.name = dataArray[2]
        pol.outerboundaryis.coords = coordsArr
    kml.save("Zones_15_14_28_16.kml")
