import numpy as np
import cv2
from time import sleep

print("initializing camera...");
# Connecting to camera
cap = cv2.VideoCapture(1)

print("camera initialyzed!")

ret,frame = cap.read() # return a single frame in variable `frame`
# display previouly frame
cv2.imshow('Video 1',frame)
# not shure yet but is nesecery
cv2.waitKey(1)
cv2.imwrite('images/c2.png',frame)
sleep(5)

cap.release()