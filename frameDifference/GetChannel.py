#-*- coding:utf-8 -*-
import cv2
import numpy 
import time


img1 = cv2.imread("input.png");
row,col,ch = img1.shape

print(ch)
print(img1.shape[2])