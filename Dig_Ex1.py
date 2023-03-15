import cv2
A=cv2.imread("out.jpg",1)
cv2.imshow("212221230086",A)
cv2.waitKey(0)

A=cv2.imread("out.jpg",2)
cv2.imwrite("outer1.png",A)
cv2.imshow("212221230086",A)
cv2.waitKey(0)

import cv2
pic = cv2.imread('out.jpg',3)
print(pic.shape)

import random
import cv2
A=cv2.imread("out.jpg",4)
for i in range(100):
    for j in range(A.shape[1]):
        A[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
cv2.imshow("212221230086",A)
cv2.waitKey(0)

import random
import cv2
A=cv2.imread("out.jpg",5)
for i in range(100):
    for j in range(A.shape[1]):
        A[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
cv2.imshow("212221230086",A)
cv2.waitKey(0)

import cv2
A=cv2.imread("out.jpg",6)
tag=A[140:240,165:180]
A[25:125,50:65]=tag
cv2.imshow("212221230086",A)
cv2.waitKey(0)
