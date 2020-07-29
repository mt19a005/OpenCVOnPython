import cv2
 
# 分類器の読込
# https://github.com/opencv/opencv/tree/master/data/haarcascades
# から取得
cascade_path = "haarcascade_frontalface_default.xml"
 
# 画像ファイルの読込(結果表示に使用する)
img = cv2.imread('input1.jpg') #カラーで読込
 
# グレースケールに変換(顔検出に使用する)
gry_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# カスケード検出器の特徴量を取得する
cascade = cv2.CascadeClassifier(cascade_path)
 
# 顔検出の実行
facerect = cascade.detectMultiScale(gry_img, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))
 
# 矩形線の色
rectangle_color = (0, 255, 0) #緑色
 
# 顔を検出した場合
if len(facerect) > 0:
    for rect in facerect:
        cv2.rectangle(img, tuple(rect[0:2]),tuple(rect[0:2] + rect[2:4]), rectangle_color, thickness=2)

cv2.imshow("a", img)
cv2.waitKey(0)