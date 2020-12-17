import cv2
import cv2 as cv

# def loading_displaying_saving():
import cv2
import numpy as np
import cv2

# img = cv2.imread('2.png', 0)
# kernel = np.ones((5, 5), np.hsplit)
# erosion = cv2.erode(img, kernel, iterations=1)
# cv.imwrite('gray.jpg', img)



# 3793722.5878498666%25836119.983629778%2C3796168.572754992%2C5838565.968534904
x_max = 3820241.74586235
x_min = 3819392.7599407
y_max = 5817332.77901273
y_min = 5816385.55007244

x_max_result = x_max+9.554628536
x_min_result = x_min-9.554628536
y_max_result = y_max+9.554628536
y_min_result = y_min-9.554628536

w = (x_max_result-x_min_result)/9.554628536*2
h = (y_max_result-y_min_result)/9.554628536*2
url = 'https://m1.land.gov.ua/geowebcache/service/wms?tiled=true&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&FORMAT=image%2Fpng&TRANSPARENT=true&LAYERS=kadastr&TILED=true&STYLES=&SRS=EPSG%3A900913&WIDTH={w}&HEIGHT={h}&CRS=EPSG%3A900913&BBOX={x_min_result}%2C{y_min_result}%2C{x_max_result}%2C{y_max_result}'\
    .format(x_max_result=x_max_result, x_min_result = x_min_result, y_max_result=y_max_result, y_min_result = y_min_result, h=np.math.ceil(h), w=np.math.ceil(w))
print(url)