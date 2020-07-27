#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
import numpy as np

def Trim(img):
    # 画像読み込み
    imgSrc1 = cv2.imread('2.jpg')
    minX = 100000
    minY = 100000
    maxX = -100000
    maxY = -100000

    imgSrc1Rows, imgSrc1Cols, imgSrc1Ch = imgSrc1.shape
    # ピクセルにアクセス
    for y in range(imgSrc1Rows):
        for x in range(imgSrc1Cols):
            # print(x)
            img = imgSrc1[y,x]
            # それが黒じゃなかったら
            if img[0] + img[1] + img[2] != 0:
                #サイズを変換
                if minX > x:
                    minX = x
                elif maxX < x:
                    maxX = x
                if minY > y:
                    minY = y
                elif maxY < y:
                    maxY = y

    imgDst = imgSrc1.copy()
    size = (maxX - minX, maxY - minY)
    H = np.float32([[1,0,0 - minX],[0,1,0 - minY]])
    imgDst = cv2.warpAffine(imgSrc1,H,(size[0], size[1]))
    
    return imgDst