import cv2, os

path = ".\\png2"
# path = ".\\test"



for f in os.listdir(path):
    print(os.path.join(path, f))