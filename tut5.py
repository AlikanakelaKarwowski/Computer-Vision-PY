import numpy as np
import cv2

font = cv2.FONT_HERSHEY_SIMPLEX
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([10,100,100])
    upper_blue = np.array([179,255,255])

    mask = cv2.inRange(hsv, lower_blue,upper_blue)

    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('frame', result)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()