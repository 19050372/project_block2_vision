import numpy as np
import cv2

cap = cv2.VideoCapture(1)
#ret,frame = cap.read() # return a single frame in variable `frame`


while(True):
    ret,frame = cap.read() # return a single frame in variable `frame`
    cv2.imshow('Video 1',frame) #display the captured image
    if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
        cv2.imwrite('images/c1.png',frame)
        cv2.destroyAllWindows()
        break

cap.release()