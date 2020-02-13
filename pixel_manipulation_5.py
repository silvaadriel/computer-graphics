import cv2 as cv
import numpy as np

image = np.zeros((512, 512, 3), np.uint8)

image = cv.circle(image, (256, 256), 8, (255, 0, 0))
image = cv.circle(image, (256, 256), 16, (255, 0, 0))
image = cv.circle(image, (256, 256), 32, (255, 0, 0))
image = cv.circle(image, (256, 256), 32, (255, 0, 0))
image = cv.circle(image, (256, 256), 64, (255, 0, 0))
image = cv.circle(image, (256, 256), 128, (255, 0, 0))
image = cv.rectangle(image, (5, 128), (507, 384), (0, 255, 0))
image = cv.line(image, (256, 132), (256, 382), (0, 0, 255))
image = cv.line(image, (132, 256), (382, 256), (0, 0, 255))
image = cv.line(image, (168, 168), (344, 344), (0, 0, 255))
image = cv.line(image, (344, 168), (168, 344), (0, 0, 255))

cv.imshow('Window', image)
cv.waitKey()
