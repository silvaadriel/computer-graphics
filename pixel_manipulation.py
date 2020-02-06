import cv2 as cv
import numpy
import os

array = bytearray(os.urandom(120000))
flatArray = numpy.array(array)

grayImage = flatArray.reshape(300, 400)
cv.imwrite('./randomGray.png', grayImage)

colorfullImage = flatArray.reshape(100, 400, 3)
cv.imwrite('./randomColor.png', colorfullImage)
