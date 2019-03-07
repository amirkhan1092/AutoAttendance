

import cv2

cam = cv2.VideoCapture(0)

while 1:
    reg,tf = cam.read()
    cv2.imshow('image',tf)

    cv2.waitKey(1)

cam.release()
cv2.destroyAllWindows()
