import cv2

img = cv2.imread('assets/loki.jpg', -1)
img = cv2.resize(img, (0,0), fx=0.3,fy=0.3)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()