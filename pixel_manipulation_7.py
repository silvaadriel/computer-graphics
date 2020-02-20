import cv2 as cv

image = cv.imread('./donald-knuth.jpeg')

image[30:50, :] = (255, 0, 0)
image[100:150, 50:100] = (0, 0, 255)
image[:, 200:220] = (0, 255, 255)
image[150:300, 250:350] = (0, 255, 0)
image[300:400, 50:150] = (255, 255, 0)
image[250:350, 300:400] = (255, 255, 255)
image[70:100, 300:450] = (0, 0, 0)

cv.imshow('Changed Image', image)
cv.imwrite('./changed-image.jpeg', image)
cv.waitKey(0)
