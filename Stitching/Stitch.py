#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
import numpy as np

def main():
    imgSrc1 = cv2.imread('1.jpg')
    imgSrc2 = cv2.imread('2.jpg')

    src1Rows,src1Cols,src1Ch1 = imgSrc1.shape
    src2Rows,src2Cols,src1Ch2 = imgSrc2.shape

    # 余白が少ないと画像端の特徴点検出が行われないため、画像を任意の方向からくっつけるため余白を追加
    H = np.float32([[1,0,src1Cols],[0,1,src1Rows]])
    marginedImgSrc1 = cv2.warpAffine(imgSrc1,H,(src1Cols * 3, src1Rows * 3))
    marginedImgSrc2 = cv2.warpAffine(imgSrc2,H,(src2Cols * 3, src2Rows * 3))
    cv2.imwrite('marginedImgSrc1.jpg', marginedImgSrc1)
    cv2.imwrite('marginedImgSrc2.jpg', marginedImgSrc2)
    #グレースケール化
    imgSrc1Gray = cv2.cvtColor(marginedImgSrc1, cv2.COLOR_BGR2GRAY)
    imgSrc2Gray = cv2.cvtColor(marginedImgSrc2, cv2.COLOR_BGR2GRAY)

    # 特徴点  kp1, kp2
    # 特徴量記述子  des1, des2
    akaze = cv2.AKAZE_create()
    kp1, des1 = akaze.detectAndCompute(marginedImgSrc1, None)
    kp2, des2 = akaze.detectAndCompute(marginedImgSrc2, None)

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

    cv2.imwrite('Matches.jpg', cv2.drawMatches(marginedImgSrc2, kp2, marginedImgSrc1, kp1, goods, None))

    # ホモグラフィ行列で画像(imgSrc2)を移動
    warpedImgSrc2 = cv2.warpPerspective(marginedImgSrc2, H, (marginedImgSrc2.shape[1], marginedImgSrc2.shape[0]))
    cv2.imwrite('warpedImgSrc2.jpg', warpedImgSrc2)

    # 結合
    stitchedImg = warpedImgSrc2.copy()
    stitchedImg[src1Rows : src1Rows * 2, src1Cols :src1Cols * 2] = imgSrc1
    cv2.imwrite('stitchedImg.jpg', stitchedImg)

    #余分な部分を取り除く
    trimedImg = Trim(stitchedImg)
    cv2.imwrite('trimedImg.jpg', trimedImg)

    cv2.waitKey(0)

def Trim(imgSrc):
    # 画像読み込み
    minX = 100000
    minY = 100000
    maxX = -100000
    maxY = -100000

    imgSrcRows, imgSrcCols, imgSrcCh = imgSrc.shape
    # ピクセルにアクセス
    for y in range(imgSrcRows):
        for x in range(imgSrcCols):
            img = imgSrc[y,x]
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

    imgDst = imgSrc.copy()
    size = (maxX - minX, maxY - minY)
    H = np.float32([[1,0,0 - minX],[0,1,0 - minY]])
    imgDst = cv2.warpAffine(imgSrc,H,(size[0], size[1]))
    
    return imgDst

if __name__ == '__main__':
    main()