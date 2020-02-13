import cv2 as cv

videoCapture = cv.VideoCapture('video.avi')

while(videoCapture.isOpened()):
  ret, frame = videoCapture.read()
  gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
  cv.imshow('Frame', gray)
  if (cv.waitKey(1) & 0xFF == ord('q')):
    break
  
videoCapture.release()
cv.destroyAllWindows()
