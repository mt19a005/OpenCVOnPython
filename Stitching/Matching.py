#-*- coding:utf-8 -*-
import cv2
import time
import concurrent.futures as confu
import numpy as np

#-   -   -   -   特徴点マッチング    -   -   -   - #
    def Feature(img1, img2):
        kp1, des1 = akaze.detectAndCompute(img1, None)
        kp2, des2 = akaze.detectAndCompute(img2, None)
        match = cv2.BFMatcher()
        matches = match.knnMatch(des2, des1, k=2)
        goods = []
        for m, n in matches:
            if m.distance < 0.7 * n.distance:
                goods.append(m)
        cv2.imshow('Matches', cv2.drawMatches(img2, kp2, img1, kp1, goods, None))
        return len(goods)