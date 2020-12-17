import cv2
import numpy as np
from matplotlib import pyplot as plt

filename = 'erosionImage.png'
img = cv2.imread(filename)

kernel = np.ones((5, 5), np.float32) / 25
dst1 = cv2.filter2D(img, -1, kernel)

plt.subplot(122), plt.imshow(dst1), plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()
cv2.imshow("im", dst1)
cv2.waitKey(0)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# result is dilated for marking the corners, not important
dst = cv2.dilate(dst, None)

# Threshold for an optimal value, it may vary depending on the image.
dst1[dst > 0.01 * dst.max()] = [0, 0, 255]

cv2.imshow('dst', dst1)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
