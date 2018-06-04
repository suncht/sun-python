import cv2
import numpy as np

#用摄像头获取视频
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
isVideoCapture = True
if not ret:
    print('获取不到视频')
    isVideoCapture = False
    cap.release()

while(isVideoCapture):
    #获取每一帧
    ret, frame = cap.read()
    if not ret:
        print('获取不到视频')
        continue
    #转换到HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #设定蓝色的阈值
    lower_blue = np.array([110, 0, 0])
    upper_blue = np.array([130, 255, 255])

    # 根据阈值构建掩模
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # 对原图像和掩模进行位运算
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # 显示图像
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()