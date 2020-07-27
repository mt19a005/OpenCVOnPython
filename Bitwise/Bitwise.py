#-*- coding:utf-8 -*-
import cv2
import numpy as np

def main():
    # 入力画像を読み込み
    img1 = cv2.imread("a.png")
    img2 = cv2.imread("b.png")

# -   -   -   -   四則演算    -   -   -   - #
    imgAdd = img1 + img2
    imgSub = img1 - img2
    imgmulti = img1 * img2
    # 計算できない
    # imgdiv = img1 / img2
    imgdiff = cv2.absdiff(img1, img2)

# -   -   -   -   bitwise    -   -   -   - #
    bitwiseAnd = cv2.bitwise_and(img1, img2)
    bitwiseNot = cv2.bitwise_not(img1)
    bitwiseXor = cv2.bitwise_xor(img1, img2)
    bitwiseOr = cv2.bitwise_or(img1, img2)

# -   -   -   -   出力    -   -   -   - #
    cv2.imwrite("imgAdd.jpg", imgAdd)
    cv2.imwrite("imgSub.jpg", imgSub)
    cv2.imwrite("imgmulti.jpg", imgmulti)
    # cv2.imwrite("imgdiv.jpg", imgdiv)
    cv2.imwrite("imgdiff.jpg", imgdiff)
    cv2.imwrite("imgAbsSub.jpg", imgAbsSub)

    cv2.imwrite("bitwiseAnd.jpg", bitwiseAnd)
    cv2.imwrite("bitwiseNot.jpg", bitwiseNot)
    cv2.imwrite("bitwiseXor.jpg", bitwiseXor)
    cv2.imwrite("bitwiseOr.jpg", bitwiseOr)

    

if __name__ == "__main__":
    main()