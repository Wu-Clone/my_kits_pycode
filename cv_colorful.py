import cv2
import numpy as np

# 创建一张200x200的黑色图片
img = np.zeros((200, 200, 3), dtype=np.uint8)

# 设置每个像素点的颜色规律
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img[i, j] = [i, j, (i+j) % 256]  # 颜色规律：(R, G, B) = (i, j, i+j)

# 显示图片
cv2.imshow('colorful image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
