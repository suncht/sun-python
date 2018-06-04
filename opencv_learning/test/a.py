import numpy as np
import cv2

cv2.namedWindow("test")#命名一个窗口
classfier=cv2.CascadeClassifier("../data/haarcascade_frontalface_alt.xml")#定义分类器
color = (255,0,0)
cap = cv2.VideoCapture(0)
success, frame = cap.read()#读取一桢图像，前一个返回值是是否成功，后一个返回值是图像本身
while(success):
    success, image = cap.read()
    #image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    h, w = image.shape[:2]
    divisor = 8
    minSize = (int(w / divisor), int(h / divisor))
    faceRects = classfier.detectMultiScale(image, 1.2, 2, cv2.CASCADE_SCALE_IMAGE, minSize)
    if len(faceRects) > 0:
        for faceRect in faceRects:
            x, y, w, h = faceRect
            cv2.rectangle(image, (x, y), (x + w, y + h), color)

    cv2.imshow('test', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()