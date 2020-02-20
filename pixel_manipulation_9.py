import cv2 as cv
import numpy as np

image = cv.imread('./donald-knuth.jpeg')

px = image[100, 100]
print(px)

blue = image[100, 100, 0]
print(blue)

image[100, 100] = [255, 255, 255]
print(image[100, 100])

image.item(10, 10, 2)
image.itemset((10, 10, 2), 100)
image.item(10, 10, 2)

print(image.shape)
print(image.size)
print(image.dtype)

ball = image[280:340, 330:390]
image[273:333, 100:160] = ball

cv.imshow('Window', image)
cv.waitKey(0)
