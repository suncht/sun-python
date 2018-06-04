import numpy as np
import cv2

#显示图片
img = cv2.imread('Images/Penguins.jpg',cv2.IMREAD_COLOR)
height, width = img.shape[:2]  #获取图片的高度和宽度
print(height, width)

#图片缩放为一半
#img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

#图片旋转
# 这里的第一个参数为旋转中心，第二个为旋转角度，第三个为旋转后的缩放因子
# 可以通过设置旋转中心，缩放因子，以及窗口大小来防止旋转后超出边界的问题
#M=cv2.getRotationMatrix2D((width/2,height/2),180,1)
# 第三个参数是输出图像的尺寸中心
#img=cv2.warpAffine(img,M,(width,height))

#仿射变换
# pts1=np.float32([[50,50],[200,50],[50,200]])   #旋转前三个点
# pts2=np.float32([[10,100],[200,50],[100,250]])  #旋转后三个点
# M=cv2.getAffineTransform(pts1,pts2)
# img=cv2.warpAffine(img,M,(width, height))

#透视变换
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M=cv2.getPerspectiveTransform(pts1,pts2)
img=cv2.warpPerspective(img,M,(width,height))

e1 = cv2.getTickCount()
#滤波
#for i in range(5,49,2):
img = cv2.medianBlur(img,5)

e2 = cv2.getTickCount()
#性能测试
time = (e2-e1) / cv2.getTickFrequency()
print(time)

#cv2.namedWindow('Penguins', cv2.WINDOW_NORMAL)
cv2.imshow('Penguins',img)


cv2.waitKey(0)
cv2.destroyAllWindows()