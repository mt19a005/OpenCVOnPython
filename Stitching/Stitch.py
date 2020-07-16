#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np

img1 = cv.imread('a.jpg')
img2 = cv.imread('b.jpg')

img1_gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
img2_gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

img1_gauss = cv.GaussianBlur(img1_gray, (3, 3), 1.3)
img2_gauss = cv.GaussianBlur(img2_gray, (3, 3), 1.3)
cv.imwrite('drawgauss3.jpg',img2_gauss)

# 特徴点 Key Points kp1, kp2
# 特徴量記述子 Feature Description des1, des2
sift = cv.AKAZE_create()
kp1, des1 = sift.detectAndCompute(img1_gauss, None)
kp2, des2 = sift.detectAndCompute(img2_gauss, None)

# 特徴量を総当たりでマッチングします。
# マッチング度合いが高い順に二つ (k=2) 取得します。
match = cv.BFMatcher()
matches = match.knnMatch(des2, des1, k=2)

# マッチング結果に閾値を設定します。
# 取得した結果二つのうち、一つをもう一つの閾値として利用しています。
good = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
    # if m.distance < 0.75 * n.distance:
        good.append(m)

# ホモグラフィの計算には理論上 4 つの点が必要です。実際にはノイズの影響もあるため更に必要です。
MIN_MATCH_COUNT = 4
if len(good) > MIN_MATCH_COUNT:
    src_pts = np.float32([ kp2[m.queryIdx].pt for m in good ])
    dst_pts = np.float32([ kp1[m.trainIdx].pt for m in good ])
    H = cv.findHomography(src_pts, dst_pts, cv.RANSAC, 5.0)[0]
else:
    print('Not enought matches are found - {}/{}'.format(len(good), MIN_MATCH_COUNT))
    exit(1)

# ホモグラフィ行列で img2 を変換します。
img2_warped = cv.warpPerspective(img2, H, (img1.shape[1] + img2.shape[1], img1.shape[0]))

# img1 と結合します。
img_stitched = img2_warped.copy()
img_stitched[:img1.shape[0], :img1.shape[1]] = img1


# 特徴点を可視化して確認します。
# cv.imwrite('drawKeypoints.jpg', cv.drawKeypoints(img2, kp2, None))

# マッチング結果を可視化して確認します。
draw_params = dict(matchColor=(0,255,0),
                   singlePointColor=None,
                   flags=2)

cv.imwrite('drawMatches.jpg', cv.drawMatches(img2, kp2, img1, kp1, good, None, **draw_params))
cv.imwrite('drawimg2_warped.jpg', img2_warped)
cv.imwrite('drawimg_stitched.jpg', img_stitched)
#cv.imwrite('img_stitched_trimmed.jpg', img_stitched_trimmed)
cv.waitKey(0)