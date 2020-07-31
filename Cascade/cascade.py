import cv2
 
cascadeDefPath = "haarcascade_frontalface_default.xml"
cascadeAltPath = "haarcascade_frontalface_alt.xml"
cascadeAlt2Path = "haarcascade_frontalface_alt2.xml"
cascadeTreePath = "haarcascade_frontalface_alt_tree.xml"
 

# 重複して認識する事がある
cascadeDef = cv2.CascadeClassifier(cascadeDefPath)
# Alt2の劣化版
# cascadeAlt = cv2.CascadeClassifier(cascadeAltPath)
# 一番いい
cascadeAlt2 = cv2.CascadeClassifier(cascadeAlt2Path)
# よくわからん
# cascadeTree = cv2.CascadeClassifier(cascadeTreePath)

def cascade(imSrc):
    imgGray = cv2.cvtColor(imSrc, cv2.COLOR_BGR2GRAY)
    # 顔検出の実行
    faceRectsDef = cascadeDef.detectMultiScale(imgGray, scaleFactor=1.1, minNeighbors=2, minSize=(50, 50))
    # faceRectsAlt = cascadeAlt.detectMultiScale(imgGray, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))
    faceRectsAlt2 = cascadeAlt2.detectMultiScale(imgGray, scaleFactor=1.1, minNeighbors=2, minSize=(50, 50))
    # faceRectsTree = cascadeTree.detectMultiScale(imgGray, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))
    
    # 矩形線の色
    rectangle_color = (0, 255, 0) #緑色
    
    clone1 = imSrc.copy()
    # clone2 = imSrc.copy()
    clone3 = imSrc.copy()
    # clone4 = imSrc.copy()
    # 顔を検出した場合
    if len(faceRectsDef) > 0:
        for rect in faceRectsDef:
            cv2.rectangle(clone1, tuple(rect[0:2]),tuple(rect[0:2] + rect[2:4]), rectangle_color, thickness=2)

    #    # 顔を検出した場合
    # if len(faceRectsAlt) > 0:
    #     for rect in faceRectsAlt:
    #         cv2.rectangle(clone2, tuple(rect[0:2]),tuple(rect[0:2] + rect[2:4]), rectangle_color, thickness=2)

       # 顔を検出した場合
    if len(faceRectsAlt2) > 0:
        for rect in faceRectsAlt2:
            cv2.rectangle(clone3, tuple(rect[0:2]),tuple(rect[0:2] + rect[2:4]), rectangle_color, thickness=2)
            
    #    # 顔を検出した場合
    # if len(faceRectsTree) > 0:
    #     for rect in faceRectsTree:
    #         cv2.rectangle(clone4, tuple(rect[0:2]),tuple(rect[0:2] + rect[2:4]), rectangle_color, thickness=2)

    cv2.imshow("def", clone1)
    # cv2.imshow("alt", clone2)
    cv2.imshow("alt2", clone3)
    # cv2.imshow("tree", clone4)



# cap = cv2.VideoCapture(0)
# while(cap.isOpened()):
#     frame = cap.read()[1]
#     cascade(frame)
    # if cv2.waitKey(15) & 0xFF == ord('q'):
    #     break

img = cv2.imread("input1.jpg")
cascade(img)
cv2.waitKey(0)