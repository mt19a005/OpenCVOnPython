#-*- coding:utf-8 -*-
import cv2
import numpy as np

cap = cv2.VideoCapture('srcMovie2.mp4')


fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    frame = cap.read()[1]
    # MOG
    frameMog = fgbg.apply(frame)
    
    #メディアンフィルター（モルフォロジー変換のオープニングみたいな処理）
    ksize=3
    frameMogBlur = cv2.medianBlur(frameMog, ksize)

    frameMogThresh = cv2.threshold(frameMogBlur, 10, 255, cv2.THRESH_BINARY)[1]

    # cv2.imshow('frame',frame)
    # cv2.imshow('frameMog',frameMog)
    # cv2.imshow('frameMogBlur',frameMogBlur)
    # cv2.imshow('frameMogThresh',frameMogThresh)

    # -   -   -   -   動体検出    -   -   -   - #
    contours, _ = cv2.findContours(frameMogThresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 900:
            continue
        # 矩形を描画
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # 動体検出
        cv2.putText(frame, "Detect Movement", (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 3)
    # cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)

    cv2.imshow("MOG", frame)

    k = cv2.waitKey(15) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()