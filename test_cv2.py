# load numpy abd cv2
# initialize maze
# load image , iamread("檔案路徑")
# resize image
# assign resized image to 正確的 位置


import numpy as np
import cv2

# 開一個這樣的視窗，只有最一開始需要
# canvas = np.zeros((600, 800, 3))
image = cv2.imread("./test.jpg")
resize_image = cv2.resize(image, (100, 100))
x, y = 300-100, 400-100
canvas[x:x+100, y:y+100, :] = resize_image
print(resize_image)
