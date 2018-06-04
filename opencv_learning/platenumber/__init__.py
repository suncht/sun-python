import numpy as np
import cv2

def colorDetect(image,option=0):
    name = np.random.randint(0,99)
    img = cv2.imread(image)
    colorImage = img.copy()
    _colorImage = img.copy()
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #cv2.imshow("hsv",hsv)
    #高斯模糊
    img = cv2.GaussianBlur(img,(5,5),0)
    #cv2.imshow("hsv",hsv)
    # 设定蓝色的阈值
    if(option == 0):
        lower=np.array([100,50,50])
        upper=np.array([140,255,255])
    else:
        #黄色
        lower=np.array([15,50,50])
        upper=np.array([40,255,255])

    # 根据阈值构建掩模
    mask=cv2.inRange(hsv,lower,upper)
    # 对原图像和掩模进行位运算
    res=cv2.bitwise_and(img,img,mask=mask)
    gray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
    #二值化
    ret,thresh1 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #cv2.imshow('gray',gray)
    #闭操作
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(17, 3))
    closed = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernel)
    #cv2.imshow('closed',closed)
    (cnts, _) = cv2.findContours(closed.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    boxes = choose(cnts)
    #cv2.drawContours(img,cnts,-1,(0,0,255),1)
    imgRs = []
    i = 0
    for cnt in cnts:
        rect = cv2.minAreaRect(cnt)
        x,y,w,h = cv2.boundingRect(cnt)
        if(w<50 or h < 15 or w>h < 1.0):
            continue
        #cv2.rectangle(_colorImage,(x,y),(x+w,y+h),(0,255,0),1)
        #imgCrop = _colorImage[y:y+h,x:x+w]
        imgRs.append((x,y,w,h,rect[2]))
        rs = img[y:y+h,x:x+w]
        #cv2.imshow("============="+str(name),rs)

    #cv2.drawContours(_colorImage, [_box], -1, (0,0,255), 1)
    #cv2.imshow("_colorImage",_colorImage)

    return imgRs