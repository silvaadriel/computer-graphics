import cv2 as cv

image = cv.imread('./donald-knuth.jpeg')

for y in range(0, image.shape[0], 10):
  for x in range(0, image.shape[1], 10):
    image[y:y+5, x:x+5] = (0, 255, 255)

cv.imshow('Image modified', image)
cv.waitKey()
