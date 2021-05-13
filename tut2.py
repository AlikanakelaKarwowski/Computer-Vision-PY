import cv2
import random
img = cv2.imread('assets/loki.jpg',-1)
img = cv2.resize(img, (0,0), fx=0.3,fy=0.3)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()