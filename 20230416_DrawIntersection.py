import matplotlib.pyplot as plt
import numpy as np

# 生成x轴坐标的数组
x = np.linspace(0.01, 100, 1000)

# 分别计算以2和5为底的对数函数的y轴坐标
y1 = np.log2(x)
y2 = np.log10(x)

# 绘制对数函数的曲线
fig, ax = plt.subplots()
ax.plot(x, y1, label='log2(x)')
ax.plot(x, y2, label='log10(x)')

# 绘制x=2和y=3表示的直线
ax.axvline(x=2, color='r')
ax.axhline(y=3, color='g')

# 标注交点
intersection_x = 2
intersection_y1 = np.log2(intersection_x)
intersection_y2 = np.log10(intersection_x)
ax.scatter(intersection_x, intersection_y1, color='r')
ax.annotate('({}, {})'.format(intersection_x, round(intersection_y1, 2)),
            (intersection_x, intersection_y1), textcoords="offset points", xytext=(0, 10), ha='center')
ax.scatter(intersection_x, intersection_y2, color='r')
ax.annotate('({}, {})'.format(intersection_x, round(intersection_y2, 2)),
            (intersection_x, intersection_y2), textcoords="offset points", xytext=(0, 10), ha='center')

ax.legend()
plt.show()
