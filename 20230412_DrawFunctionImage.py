# 绘制函数 f(x,y)=x^2+y^2
# numpy 和 matplotlib.pyplot 库
# 分别用于生成坐标点和绘制函数图像

import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return x ** 2 + y ** 2


# numpy.linspace 函数生成一组坐标点
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
# 100 表示在 x, y 轴上均匀地生成 100个坐标点

# 将这两组坐标点转化为网格坐标点
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# 创建一个 8 x 8 英寸大小的图形，并添加一个 3D 坐标系
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='plasma')
plt.show()
