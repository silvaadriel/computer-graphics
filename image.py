import cv2 as cv 

image = cv.imread('./donald-knuth.jpeg', 0)
cv.imshow('Window title', image)
cv.waitKey(0)
