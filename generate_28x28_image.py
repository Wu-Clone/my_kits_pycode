import cv2
import numpy as np
import random

# 定义图片宽度和高度
width, height = 280, 280

# 创建一个灰度渐变条纹图像
img = np.zeros((height, width), dtype=np.uint8)

# 设置每个区域的灰度值
for i in range(280):
    for j in range(280):
        img[i,j] = random.randint(0,255)

cv2.imshow('colorful image', img)
cv2.waitKey(0)
