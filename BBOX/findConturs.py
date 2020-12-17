import cv2
import numpy as np


def order_points_clockwise(pts):
    # sort the points based on their x-coordinates
    xSorted = pts[np.argsort(pts[:, 0]), :]

    # grab the left-most and right-most points from the sorted
    # x-roodinate points
    leftMost = xSorted[:2, :]
    rightMost = xSorted[2:, :]

    # now, sort the left-most coordinates according to their
    # y-coordinates so we can grab the top-left and bottom-left
    # points, respectively
    leftMost = leftMost[np.argsort(leftMost[:, 1]), :]
    (tl, bl) = leftMost

    # now, sort the right-most coordinates according to their
    # y-coordinates so we can grab the top-right and bottom-right
    # points, respectively
    rightMost = rightMost[np.argsort(rightMost[:, 1]), :]
    (tr, br) = rightMost

    # return the coordinates in top-left, top-right,
    # bottom-right, and bottom-left order
    return np.array([tl, tr, br, bl], dtype="int32")


image = cv2.imread('erosionImage.png')
original = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 120, 255, 1)

corners = cv2.goodFeaturesToTrack(canny, 4, 0.01, 50)
print(corners)

c_list = []
for corner in corners:
    x, y = corner.ravel()
    c_list.append([int(x), int(y)])
    cv2.circle(image, (x, y), 5, (255, 0, 0), -1)
cv2.imshow('image', image)

# corner_points = np.array([c_list[0], c_list[1], c_list[2], c_list[3]])
# ordered_corner_points = order_points_clockwise(corner_points)
# print(corner_points)
mask = np.zeros(image.shape, dtype=np.uint8)
# cv2.fillPoly(mask, [ordered_corner_points], (255, 255, 255))

mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

cv2.imshow('canny', canny)
cv2.imshow('image', image)
cv2.imshow('mask', mask)
cv2.waitKey()
