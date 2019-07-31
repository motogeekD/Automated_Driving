import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("test_image.jpg.png")
lane_image = np.copy(image)
gray = cv2.cvtColor("lane_image", cv2.COLOR_RGB2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
