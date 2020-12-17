import cv2
import numpy as np
from PIL import Image

image = Image.open("wms (4).png").convert('RGBA')
image.convert("RGBA")
canvas = Image.new('RGBA', image.size, (0, 0, 0, 0))  # Empty canvas colour (r,g,b,a)
canvas.paste(image, mask=image)  # Paste the image onto the canvas, using it's alpha channel as mask
canvas.save("canvastest.png", format="PNG")

# роблю чорно білим і заливаю фігуру яка мені треба білим
image = cv2.imread('canvastest.png', 0)
thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cv2.fillPoly(image, cnts, [255, 255, 255])
cv2.imwrite("fillImage.png", image)
# image = чорно біла картинка.
# тепер роблю там шоб з картінки брався тільки найбільший контур(може буть з прилеглими всякими)
fillImage = cv2.imread('fillImage.png')
gray = cv2.cvtColor(fillImage, cv2.COLOR_BGR2GRAY)
ret, gray = cv2.threshold(gray, 127, 255, 0)
gray2 = gray.copy()
mask = np.zeros(gray.shape, np.uint8)
contours, hier = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    if 0 < cv2.contourArea(cnt) < 20000:
        cv2.drawContours(fillImage, [cnt], 0, (0, 255, 0), 2)
        cv2.drawContours(mask, [cnt], 0, 255, -1)
cv2.imwrite("figureWithoutLines.png", mask)
# cv2.waitKey(0)

# mask = фігура де залишилось мало ліній лишніх
# тоді я роблю ерозію шоб постирались лінії які прилягають до фігури
figureWithoutLines = cv2.imread('figureWithoutLines.png', 0)
kernel = np.ones((3, 3), np.uint8)
erosion = cv2.erode(figureWithoutLines, kernel, iterations=1)
cv2.imwrite("erosionImage.png", erosion)

# шукаю самі угли і виводжу фотку
#замилення
filename = 'erosionImage.png'
img = cv2.imread(filename)
kernel = np.ones((5, 5), np.float32) / 25
dst1 = cv2.filter2D(img, -1, kernel)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None)
ret0, dst = cv2.threshold(dst, 0.01 * dst.max(), 255, 0)
dst = np.uint8(dst)

ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

# define the criteria to stop and refine the corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray, np.float32(centroids), (5, 5), (-1, -1), criteria)
# here u can get corners
print(corners[0])

for i in range(0, len(corners)):
    print(corners[i])
dst1[dst > 0.1 * dst.max()] = [0, 0, 255]
cv2.imshow('image', dst1)
cv2.waitKey(0)
# cv2.destroyAllWindows
