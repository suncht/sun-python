import cv2
import numpy as np
from util.show_plot import showPlot

img = cv2.imread('Images/Smog.jpg', cv2.IMREAD_GRAYSCALE)
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img.shape)
img_300x300 = cv2.copyMakeBorder(img, 50, 30, 10, 15,
                                       cv2.BORDER_CONSTANT,
                                       value=(0, 0, 0))
print(img_300x300.shape)


# 定义Gamma矫正的函数
def gamma_trans(img, gamma):
    # 具体做法是先归一化到1，然后gamma作为指数值求出新的像素值再还原
    gamma_table = [np.power(x / 255.0, gamma) * 255.0 for x in range(256)]
    gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)

    # 实现这个映射用的是OpenCV的查表函数
    return cv2.LUT(img, gamma_table)

# 执行Gamma矫正，小于1的值让暗部细节大量提升，同时亮部细节少量提升
img_corrected = gamma_trans(img, 0.5)


images = [img, img_300x300, img_corrected]
titles = [u'原图', u'加边框', u'修正']
showPlot(images, titles)