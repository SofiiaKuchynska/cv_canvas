
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-10, 10, 0.0001)
y = np.sin(x)
plt.plot(x, y)
plt.grid(True)
plt.axhline(y=-1, color='r', linestyle='--')
plt.axhline(y=1, color='r', linestyle='--')
plt.axvline(x=0, color='black')
plt.axhline(y=0, color='black')
plt.xlabel("Вісь X")
plt.ylabel("Вісь Y")
plt.show()




