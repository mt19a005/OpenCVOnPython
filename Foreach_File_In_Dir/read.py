import os

path = ".\\png2"
# path = ".\\test"



for fileName in os.listdir(path):
    # フルパス
    print(os.path.join(path, fileName))
    # 文字列取得
    print(fileName[7:9])