import cv2
import numpy as np

img = cv2.imread("1.jpg", cv2.IMREAD_GRAYSCALE)  # shape: (960, 960)
# print grayscale image
cv2.imwrite('11.jpg', img)


equalized_img = cv2.equalizeHist(img)
cv2.imwrite('111.jpg', equalized_img)