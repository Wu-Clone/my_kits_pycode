import cv2
import numpy as np

# 定义图片宽度和高度
width, height = 255 * 5, 200

# 创建一个灰度渐变条纹图像
img = np.zeros((height, width), dtype=np.uint8)

# 设置每个区域的灰度值
for i in range(255):
    img[:, i * 5: (i + 1) * 5] = i

# 保存图像为PNG文件
cv2.imshow('colorful image', img)
cv2.waitKey(0)
