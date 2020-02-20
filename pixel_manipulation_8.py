import cv2 as cv
import numpy as np

image = cv.imread('./donald-knuth.jpeg')
red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)

cv.line(image, (0, 0), (100, 200), green)
cv.line(image, (300, 200), (150, 150), red, 5)
cv.rectangle(image, (20, 20), (120, 120), blue, 10)
cv.rectangle(image, (200, 50), (255, 125), green, -1)
(x, y) = (image.shape[1] // 2, image.shape[0] // 2)

for radius in range(0, 175, 15):
  cv.circle(image, (x, y), radius, red)

cv.imshow('Drawing on Image', image)
cv.waitKey(0)
