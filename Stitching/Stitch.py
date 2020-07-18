#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
import numpy as np

imgSrc1 = cv2.imread('2.jpg')
imgSrc2 = cv2.imread('1.jpg')

row,col,ch = imgSrc1.shape
M = np.float32([[1,0,col],[0,1,row]])
marginedImgSrc1 = cv2.warpAffine(imgSrc1,M,(imgSrc1.shape[1] * 3, imgSrc1.shape[0] * 3))
marginedImgSrc2 = cv2.warpAffine(imgSrc2,M,(imgSrc2.shape[1] * 3, imgSrc2.shape[0] * 3))
cv2.imwrite('marginedImgSrc1.jpg', marginedImgSrc1)
cv2.imwrite('marginedImgSrc2.jpg', marginedImgSrc2)
#グレースケール化
imgSrc1Gray = cv2.cvtColor(marginedImgSrc1, cv2.COLOR_BGR2GRAY)
imgSrc2Gray = cv2.cvtColor(marginedImgSrc2, cv2.COLOR_BGR2GRAY)

# 特徴点  kp1, kp2
# 特徴量記述子  des1, des2
akaze = cv2.AKAZE_create()
kp1, des1 = akaze.detectAndCompute(imgSrc1Gray, None)
kp2, des2 = akaze.detectAndCompute(imgSrc2Gray, None)

# 特徴量をBFMatcher（総当り）でマッチング。
# knnMatchで上位k = 3つのマッチング結果をmatchesに格納
match = cv2.BFMatcher()
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
    H = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)[0]
else:
    print('Not enought matches are found - {}/{}'.format(len(goods), MIN_MATCH_COUNT))
    exit(1)


# ホモグラフィ行列で画像(imgSrc2)を移動
warpedImgSrc2 = cv2.warpPerspective(marginedImgSrc2, H, (marginedImgSrc2.shape[1], marginedImgSrc2.shape[0]))
# ホモグラフィ行列で移動したimgSrc2を出力
cv2.imwrite('warpedImgSrc2.jpg', warpedImgSrc2)

imgStitched = warpedImgSrc2.copy()
print(imgStitched.shape)
# img_stitchedの(0 ~ imgSrc1.width, 0 ~ imgSrc1.height) にimgSrc1を貼り付ける。 copyToみたいな？
# imgStitched[imgSrc2.shape[0]:imgSrc2.shape[0] + imgSrc1.shape[0], imgSrc2.shape[1]:imgSrc2.shape[1] + imgSrc1.shape[1]] = imgSrc1
imgStitched[row:row * 2, col:col * 2] = imgSrc1

# 特徴点を出力
# cv2.imwrite('drawKeypoints.jpg', cv2.drawKeypoints(imgSrc2, kp2, None))

# マッチング結果を出力
cv2.imwrite('Matches.jpg', cv2.drawMatches(marginedImgSrc2, kp2, marginedImgSrc1, kp1, goods, None))
# 何故か出来ない

# 結合結果を出力
cv2.imwrite('imgStitched.jpg', imgStitched)

cv2.waitKey(0)