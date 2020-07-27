#-*- coding:utf-8 -*-
import cv2
import numpy as np
import time

# -   -   -   -   フレーム差分法    -   -   -   - #
def FlameDiff(img1, img2, img3):
    # 絶対値差分　これによって、2画像の動きがわかる
    diff1 = cv2.absdiff(img1, img2)
    diff1Gray = cv2.threshold(diff1, 10, 255,cv2.THRESH_BINARY)[1]
    diff2 = cv2.absdiff(img2, img3)
    diff2Gray = cv2.threshold(diff2, 10, 255,cv2.THRESH_BINARY)[1]




    # 2画像の白が重なっている部分だけを抽出（フレーム差分）
    flamediff = cv2.bitwise_and(diff1Gray, diff2Gray)

    #メディアンフィルター（モルフォロジー変換のオープニングみたいな処理）
    ksize=3
    flamediffBlur = cv2.medianBlur(flamediff, ksize)

    # -   -   -   -   出力    -   -   -   - #
    cv2.imshow("img1", img1)
    cv2.imshow("img2", img2)
    cv2.imshow("img3", img3)
    cv2.imshow("diff1", diff1)
    cv2.imshow("diff2", diff2)
    cv2.imshow("flamediff", flamediff)
    cv2.imshow("flamediffBlur", flamediffBlur)

    # cv2.imwrite("img1.jpg", img1)
    # cv2.imwrite("img2.jpg", img2)
    # cv2.imwrite("img3.jpg", img3)
    # cv2.imwrite("diff1.jpg", diff1)
    # cv2.imwrite("diff2.jpg", diff2)
    # cv2.imwrite("diff2.jpg", diff2)
    # cv2.imwrite("flamediffBlur.jpg", flamediffBlur)

    return flamediffBlur

# -   -   -   -   メイン    -   -   -   - #
def Main():

    cap = cv2.VideoCapture(0)
    print(cap.get(cv2.CAP_PROP_FPS))
    img1 = cap.read()[1]
    img2 = cap.read()[1]
    img3 = cap.read()[1]
    print(img3.size)

    while(cap.isOpened()):
        # 画像の入れ替え
        img3 = img2
        img2 = img1
        # 撮影
        img1 = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)

        # img3がチャンネルが無し（グレースケール）だったら
        try:
            img3.shape[2]
        except IndexError:
            #フレーム差分
            flamediffBlur = FlameDiff(img1, img2, img3)

            #動体検出
            countNonZero = cv2.countNonZero(flamediffBlur)
            if(countNonZero > img1.size / 5):
                print("detect anyone")

        # time.sleep(0.03)

        # xキーが押されたら終了
        if cv2.waitKey(1) & 0xFF == ord('x'):
            cap.release()
            cv2.destroyAllWindows()
            break

if __name__ == "__Main__":
    Main()

print(Main().__name__)