import os

import shapefile

all_files = os.listdir("./Ivannucha")
files_dbf = filter(lambda x: x.endswith('.dbf'), all_files)
for dbf in files_dbf:
    new_directory = dbf.replace('.dbf', "").replace("№", "").replace(" ", '')
    # os.mkdir("./newDirectory/")
    sf = shapefile.Reader("./Ivannucha/" + dbf, encoding='ISO8859-1')
    # header = ("lon" + "," + "lat" + "," + "val\n")
    k = []
    z = ''
    # print(new_directory)
    with shapefile.Reader("./Ivannucha/" + dbf, encoding='ISO8859-1') as shp:
        K = open('./newDirectory/'+new_directory+".txt", 'w')
        for i in range(len(shp)):
            shapes = sf.shape(i)
            points_lon = shapes.points[0][0]
            points_lat = shapes.points[0][1]
            fields = sf.record(i)
            x = (str(new_directory)+";"+str(points_lon) + "," + str(points_lat) + ";" + str(fields[7])+ ";"+str(fields[8])+";"+str(fields[9])+";"+str(fields[10])+";"+str(fields[11])+";"+str(fields[12])+";"+str(fields[13])+"\n")
            z = z+ x
            # print(x)
        # print(z)
        K.write(z)
        # K.write(k)