import cv2 as cv

image = cv.imread('./donald-knuth.jpeg')

for y in range(0, image.shape[0]):
  for x in range(0, image.shape[1]):
    image[y, x] = (255, 0, 0)

cv.imshow('Image modified', image)
cv.waitKey()
