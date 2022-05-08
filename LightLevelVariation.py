import cv2
import numpy as np
def change_brightness(img, alpha, beta):
    img_new = np.asarray(alpha*img + beta, dtype=int)   # cast pixel values to int
    img_new[img_new>255] = 255
    img_new[img_new<0] = 0
    return img_new
img = cv2.imread("1.jpg")
img1 = change_brightness(img, 0.5, 20)
cv2.imwrite("11.jpg", img1)

