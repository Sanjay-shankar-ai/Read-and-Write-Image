# READ AND WRITE AN IMAGE
## AIM
To write a python program using OpenCV to do the following image manipulations.
i) Read, display, and write an image.
ii) Access the rows and columns in an image.
iii) Cut and paste a small portion of the image.

## Software Required:
Anaconda - Python 3.7
## Algorithm:
### Step1:
Choose an image and save it as a filename.jpg
### Step2:
Use imread(filename, flags) to read the file.
### Step3:
Use imshow(window_name, image) to display the image.
### Step4:
Use imwrite(filename, image) to write the image.
### Step5:
End the program and close the output image windows.
## Program:
### Developed By:
### Register Number: 
i) #To Read,display the image
```
 import cv2
A=cv2.imread("out.jpg",1)
cv2.imshow("212221230086",A)
cv2.waitKey(0) 

```
ii) #To write the image
```
A=cv2.imread("out.jpg",2)
cv2.imwrite("outer1.png",A)
cv2.imshow("212221230086",A)
cv2.waitKey(0)
```
iii) #Find the shape of the Image
```
import cv2
pic = cv2.imread('out.jpg',3)
print(pic.shape)
```
iv) #To access rows and columns

```
import random
import cv2
A=cv2.imread("out.jpg",5)
for i in range(100):
    for j in range(A.shape[1]):
        A[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
cv2.imshow("212221230086",A)
cv2.waitKey(0)


```
v) #To cut and paste portion of image
```
import cv2
A=cv2.imread("out.jpg",6)
tag=A[140:240,165:180]
A[25:125,50:65]=tag
cv2.imshow("212221230086",A)
cv2.waitKey(0)


```

## Output:

### i) Read and display the image
![Screenshot (19)](https://user-images.githubusercontent.com/94231938/225218139-af47cf92-45b9-4d56-9612-44fcdb673def.png)

### ii)Write the image
![Screenshot (19)](https://user-images.githubusercontent.com/94231938/225218256-6d3bda45-37bc-4082-8caa-9e803185f8f8.png)

### iii)Shape of the Image
![Screenshot (22)](https://user-images.githubusercontent.com/94231938/225218354-9c6025ae-5076-4701-9b09-2fa6429efd09.png)

### iv)Access rows and columns
![Screenshot (20)](https://user-images.githubusercontent.com/94231938/225218382-f5ae6763-00af-47ec-9bb4-1a68f412da17.png)

### v)Cut and paste portion of image
![Screenshot (21)](https://user-images.githubusercontent.com/94231938/225218445-1a6ee21f-ead5-41ea-86bb-25667dad1252.png)

## Result:
Thus the images are read, displayed, and written successfully using the python program.


