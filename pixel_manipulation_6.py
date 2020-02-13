import cv2 as cv
import numpy as np

def none(x):
  pass

image = np.zeros((300, 512, 3), np.uint8)

cv.namedWindow('Image')

cv.createTrackbar('R', 'Image', 0, 255, none)
cv.createTrackbar('G', 'Image', 0, 255, none)
cv.createTrackbar('B', 'Image', 0, 255, none)

swipe = '0: OFF \n 1: ON'
cv.createTrackbar(swipe, 'Image', 0, 1, none)

while(True):
  cv.imshow('Image', image)
  key = cv.waitKey()
  if key == 27:
    break
  redTrackbarPos = cv.getTrackbarPos('R', 'Image')
  greenTrackbarPos = cv.getTrackbarPos('G', 'Image')
  blueTrackbarPos = cv.getTrackbarPos('B', 'Image')
  swipeTrackbarPos = cv.getTrackbarPos(swipe, 'Image')
  if swipeTrackbarPos == 0:
    image[:] = 0
  else:
    image[:] = [blueTrackbarPos, greenTrackbarPos, redTrackbarPos]

cv.destroyAllWindows()
