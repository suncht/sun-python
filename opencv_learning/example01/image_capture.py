import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
isVideoCapture = True
if not ret:
    print('获取不到视频')
    isVideoCapture = False
    cap.release()

while(isVideoCapture):
    ret, frame = cap.read()
    cv2.imshow("image", frame)

    key = cv2.waitKey(1)
    if key == ord('s'):
        millis = int(round(time.time() * 1000))
        filename = '../Images/' + str(millis) +'.jpg'
        cv2.imwrite(filename, frame)
        print('截取视频图片['+filename +']成功')
    if key == ord('q'):
        print('退出视频')
        break

cap.release()
cv2.destroyAllWindows()