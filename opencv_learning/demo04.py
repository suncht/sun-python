import numpy as np
import cv2
from matplotlib import pyplot as plt

#显示图片
img = cv2.imread('Images/Penguins.jpg',0)
height, width = img.shape[:2]  #获取图片的高度和宽度

img1 = cv2.bilateralFilter(img, 9, 75,75)
img2 = cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
img3 = cv2.adaptiveThreshold(img2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

kernel = 1/25 * np.ones((5,5),np.uint8)
#腐蚀
img4 = cv2.erode(img3,kernel,iterations = 1)
#膨胀
img5 = cv2.dilate(img4,kernel,iterations = 1)

images = [img, img1, img2, img3, img4, img5]
for i in range(6):
    plt.subplot(3,2, i+1)
    plt.imshow(images[i], 'gray')
    plt.xticks([]), plt.yticks([])
plt.show()
cv2.destroyAllWindows()