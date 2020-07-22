#-*- coding:utf-8 -*-
import cv2
import numpy as np
import time

frame = 0.5

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

    # チャンネルが無し（グレースケール）だったら
    try:
        img3.shape[2]
    except IndexError:
        # 絶対値差分　これによって、2画像の動きがわかる
        diff1 = cv2.absdiff(img2, img1)
        diff1 =  cv2.threshold(diff1, 10, 255,cv2.THRESH_BINARY)[1]
        diff2 = cv2.absdiff(img2, img3)
        diff2 =  cv2.threshold(diff2, 10, 255,cv2.THRESH_BINARY)[1]
        
        # 光の点滅を差分にしないためにオープニングをする
        kernel = np.ones((3, 3), np.uint8)
        diff1 = cv2.morphologyEx(diff1, cv2.MORPH_OPEN, kernel)
        
        # 2画像の白が重なっている部分だけを抽出
        diffbitwiseAnd = cv2.bitwise_and(diff1, diff2)

        # 膨張・収縮処理(方法2)
        cv2.imshow("diff1", diff1)
        cv2.imshow("diff2", diff2)
        cv2.imshow("diffbitwiseAnd", diffbitwiseAnd)


    cv2.imshow("img1", img1)
    cv2.imshow("img2", img2)
    cv2.imshow("img3", img3)
    time.sleep(frame)
    # xキーが押されたら途中終了
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()