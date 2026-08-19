import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-3, 3, 0.1)
y = np.arange(-3, 3, 0.1)
X, Y = np.meshgrid(x, y)
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
Z = np.sinh(X) * np.cos(Y)
ax.plot_surface(X, Y, Z, cmap='coolwarm')
ax.set_xlabel('Ось X')
ax.set_ylabel('Ось Y')
ax.set_zlabel('Ось Z')
plt.show()