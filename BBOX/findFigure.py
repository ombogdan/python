import cv2
import numpy as np

# img = cv2.imread('findFill3.png')
# # img = cv2.resize(img, (400, 400))
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, gray = cv2.threshold(gray, 127, 255, 0)
# gray2 = gray.copy()
# mask = np.zeros(gray.shape, np.uint8)
# contours, hier = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# for cnt in contours:
#     if 100 < cv2.contourArea(cnt) < 20000:
#         cv2.drawContours(img, [cnt], 0, (0, 255, 0), 2)
#         cv2.drawContours(mask, [cnt], 0, 255, -1)
# cv2.imwrite("findFigure3.png", mask)
# cv2.waitKey(0)

img1 = cv2.imread('findFigure3.png', 0)

kernel = np.ones((3, 3), np.uint8)
erosion = cv2.erode(img1, kernel, iterations=1)
dilation = cv2.dilate(img1, kernel, iterations=2)
opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, kernel)
cv2.imwrite("erosion5.png", erosion)
cv2.waitKey(0)
