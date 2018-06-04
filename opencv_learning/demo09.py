import cv2
import numpy as np
from util.show_plot import showPlot

img = cv2.imread('Images/DSC02416.JPG')
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#img_blur = cv2.medianBlur(img,5) #中值滤波
img_blur = cv2.GaussianBlur(img, (5,5), 0) #高斯模糊
img_blur = cv2.bilateralFilter(img_blur, 9, 75,75) #双边滤波

kernel = 1/25 * np.ones((5,5),np.uint8)
#腐蚀
img_blur = cv2.erode(img_blur,kernel,iterations = 1)
#膨胀
img_blur = cv2.dilate(img_blur,kernel,iterations = 1)

#ret1, img_thresh1 = cv2.threshold(img, 155, 255, cv2.THRESH_BINARY)
ret2, img_thresh2 = cv2.threshold(img_blur, 127, 255, cv2.THRESH_BINARY +cv2.THRESH_OTSU)
#img_thresh2 = cv2.adaptiveThreshold(img_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,15,2) #换行符号 \

# images = [img, img_blur, img_thresh1, img_thresh2]
# titles = ['原图', '中值滤波', '阈值化', '阈值化']
images = [img, img_thresh2]
titles = ['原图', '处理后图片']
showPlot(images, titles)