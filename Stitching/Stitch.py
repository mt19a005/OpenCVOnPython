#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np


src1 = cv.imread('1.jpg')
src2 = cv.imread('2.jpg')
#グレースケール化
src1Gray = cv.cvtColor(src1, cv.COLOR_BGR2GRAY)
src2Gray = cv.cvtColor(src2, cv.COLOR_BGR2GRAY)

# 特徴点  kp1, kp2
# 特徴量記述子  des1, des2
akaze = cv.AKAZE_create()
kp1, des1 = akaze.detectAndCompute(src1Gray, None)
kp2, des2 = akaze.detectAndCompute(src2Gray, None)

# 特徴量をBFMatcher（総当り）でマッチング。
# knnMatchで上位k = 3つのマッチング結果をmatchesに格納
match = cv.BFMatcher()
matches = match.knnMatch(des2, des1, k=2)

# 1つのmに対する2つのマッチング結果(n)同士の距離(distance)が離れていれば、良点(good)とする。
goods = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        goods.append(m)

# ホモグラフィ計算 よくわからん
MIN_MATCH_COUNT = 4
if len(goods) > MIN_MATCH_COUNT:
    src_pts = np.float32([ kp2[m.queryIdx].pt for m in goods ])
    dst_pts = np.float32([ kp1[m.trainIdx].pt for m in goods ])
    H = cv.findHomography(src_pts, dst_pts, cv.RANSAC, 5.0)[0]
else:
    print('Not enought matches are found - {}/{}'.format(len(goods), MIN_MATCH_COUNT))
    exit(1)

# ホモグラフィ行列で画像(src2)を移動
# 画像を拡大し、射影変換に対応する
src2_warped = cv.warpPerspective(src2, H, (src1.shape[1] + src2.shape[1], src1.shape[0] + src2.shape[0]))

img_stitched = src2_warped.copy()
# img_stitchedの(0 ~ src1.width, 0 ~ src1.height) にsrc1を貼り付ける。 copyToみたいな？
img_stitched[0:src1.shape[0], 0:src1.shape[1]] = src1


# 特徴点を出力
# cv.imwrite('drawKeypoints.jpg', cv.drawKeypoints(src2, kp2, None))

# マッチング結果を出力
cv.imwrite('drawMatches.jpg', cv.drawMatches(src2, kp2, src1, kp1, goods, None))
# 何故か出来ない
# cv.imwrite('drawMatches.jpg', cv.drawMatches(src1, kp1, src2, kp2, goods, None))

# ホモグラフィ行列で移動したsrc2を出力
cv.imwrite('drawsrc2_warped.jpg', src2_warped)

# 結合結果を出力
cv.imwrite('drawimg_stitched.jpg', img_stitched)

cv.waitKey(0)