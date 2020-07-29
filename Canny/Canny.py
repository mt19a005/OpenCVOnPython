#-*- coding:utf-8 -*-
import cv2
import numpy as np

def main():
    # 入力画像を読み込み
    img = cv2.imread("input.png")

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    canny = cv2.Canny(gray, 20, 110)
    # 結果を出力
    cv2.imshow("Cannyed", canny)
    cv2.imwrite("output.jpg", canny)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()