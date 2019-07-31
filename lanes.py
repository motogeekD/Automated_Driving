import numpy as np
import cv2

image = cv2.imread("test_image.jpg.png")

cv2.imshow("result", image)
cv2.waitKey(0)
