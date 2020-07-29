#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2, os
import numpy as np
from PIL import Image



# 指定されたpath内の画像を取得
def get_images_and_labels(path):
    # 画像を格納する配列
    images = []
    # ラベルを格納する配列
    labels = []
    # ファイル名を格納する配列
    files = []
    for fileName in os.listdir(path):
        # 画像のパス
        image_path = os.path.join(path, fileName)
        # グレースケール
        imgSrc = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        # カスケードで顔検知
        faces = faceCascade.detectMultiScale(imgSrc, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))
        # 検出した顔領域の処理
        for (x, y, w, h) in faces:

            # 顔領域を取得して200x200(pix)にリサイズ
            cascadeRoi = cv2.resize(imgSrc[y: y + h, x: x + w], (200, 200), interpolation=cv2.INTER_LINEAR)
            # 画像を配列に格納
            images.append(cascadeRoi)
            # ファイル名からラベルを取得
            labels.append(int(fileName[7:9]))
            
            # ファイル名を配列に格納
            files.append(fileName)
            # テスト画像の結果出力　理由：テスト画像が不適切な可能性があるから。
            if(path == test_path):
                cv2.rectangle(imgSrc, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
                cv2.imwrite("./TestResult/cascade.png", imgSrc)
                cv2.imwrite("./TestResult/cascadeRoi.png", cascadeRoi)

    return images, labels, files

# トレーニング画像
train_path = './Png'

# テスト画像
test_path = './test'

# Haar-like特徴分類器
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

# EigenFace
# recognizer = cv2.face.EigenFaceRecognizer_create()
# FisherFace
recognizer = cv2.face.FisherFaceRecognizer_create()

# トレーニング画像を取得
images, labels, files = get_images_and_labels(train_path)

# トレーニング実施
recognizer.train(images, np.array(labels))

# テスト画像を取得
test_images, test_labels, test_files = get_images_and_labels(test_path)

i = 0
while i < len(test_labels):
    # テスト画像に対して予測実施
    label, confidence = recognizer.predict(test_images[i])
    # 予測結果をコンソール出力
    print("Test Image: {}, Predicted Label: {}, Confidence: {}".format(test_files[i], label, confidence))
    # テスト画像を表示
    cv2.imshow("test image", test_images[i])
    cv2.waitKey(0)
    i += 1

# 終了処理
cv2.destroyAllWindows()