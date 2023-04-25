import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# setting for x,y,z
x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x)
z = np.exp(y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z)
ax.set_title("3D Plot of y = sinx and z = e^y")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.show()
