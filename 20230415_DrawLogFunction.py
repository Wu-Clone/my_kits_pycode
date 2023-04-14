import matplotlib.pyplot as plt
import numpy as np

# 定义自变量 x 的范围
x = np.linspace(0.1, 10, 1000)

# 定义两个不同的对数函数
y1 = np.log(x)  # 基于自然对数
y2 = np.log2(x)  # 基于二进制对数
y3 = np.log10(x)

# 绘制两条对数函数的图像
plt.plot(x, y1, label="log_e(x)")
plt.plot(x, y2, label="log_2(x)")
plt.plot(x, y3, label="log_3(x)")

# 添加图例、坐标轴标签等
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Logarithmic Functions")

# 显示图像
plt.show()
