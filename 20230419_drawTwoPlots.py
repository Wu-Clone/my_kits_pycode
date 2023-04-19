import matplotlib.pyplot as plt
import numpy as np

# Generate some data for the plots
x = np.linspace(0.1, 20, 1000)

# 定义对数函数
y1 = np.log(x)  # 基于自然对数
y2 = np.log10(x)

y3 = np.log(x) / np.log(0.9)
y4 = np.log(x) / np.log(0.1)

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

# Plot the data on the first subplot
ax1.plot(x, y1, label="log_e(x)")
ax1.plot(x, y2, label="log_10(x)")
ax1.legend()
ax1.set_title('gt 1')

# Plot the data on the second subplot
ax2.plot(x, y3, label="log_0.9(x)")
ax2.plot(x, y4, label="log_0.1(x)")
ax2.legend()
ax2.set_title('lt 1')

# Show the plots
plt.show()
