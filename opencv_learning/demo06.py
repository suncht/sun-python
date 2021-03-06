import numpy as np
import cv2
from util.show_plot import showPlot

img = cv2.imread('Images/Smog.jpg', 0)

kernel = np.ones((5,5),np.uint8)
#腐蚀
img_erode = cv2.erode(img, kernel=kernel,iterations=1)
#膨胀
img_dilate = cv2.dilate(img_erode, kernel=kernel, iterations=1)

#开运算 = 先腐蚀 + 再膨胀
img_open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel=kernel)
#闭运算 = 先膨胀 + 再腐蚀
img_close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel=kernel)
#梯度 = 膨胀 - 腐蚀
img_gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel=kernel)
#礼帽 = 开运算 - 原图
img_tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel=kernel)
#黑帽 = 闭运算 - 原图
img_blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel=kernel)

images = [img, img_erode, img_dilate, img_open, img_close, img_gradient, img_tophat, img_blackhat]
titles = [u'原图', u'腐蚀', u'膨胀', u'开运算', u'闭运算', u'梯度', u'礼帽', u'黑帽']
showPlot(images, titles)