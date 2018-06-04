import numpy as np
import cv2
from matplotlib import pyplot as plt

#显示图片
img = cv2.imread('Images/Penguins.jpg',0)
height, width = img.shape[:2]  #获取图片的高度和宽度

# 中值滤波
#img = cv2.medianBlur(img,5)
#img = cv2.blur(img,(5,5)) #平均模糊
#img = cv2.GaussianBlur(img, (5,5), 0) #高斯模糊
img = cv2.bilateralFilter(img, 9, 75,75) #双边滤波, 9 邻域直径，两个75 分别是空间高斯函数标准差，灰度值相似性高斯函数标准差

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#11 为Block size, 2 为C 值
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
titles = ['Original Image', 'Global Thresholding (v = 127)',
'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()