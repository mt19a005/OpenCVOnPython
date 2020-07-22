#-*- coding:utf-8 -*-
import cv2
import numpy 
import time

cap = cv2.VideoCapture(0)

img1 = cap.read()[1]
img2 = cap.read()[1]
img3 = cap.read()[1]
# row,col,ch = img1

while(cap.isOpened()):
    # 画像の入れ替え
    img3 = img2
    img2 = img1
    # 撮影
    img1 = cap.read()[1]
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    # チャンネルが1（グレースケール）だったら
    if img3[2] == 1:
        cv2.absdiff(img2, img1,)

    cv2.imshow("imgNew", img1)
    cv2.imshow("imgCurrent", img2)
    cv2.imshow("imgOld", img3)
    time.sleep(1)
    # xキーが押されたら途中終了
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    time.sleep



cap.release()
cv2.destroyAllWindows()