import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 20)
# Додаємо випадкові відхилення (шум)
noise = np.random.normal(0, 5, 20)
y = np.linspace(-10, 100, 20) + noise
n = len(x)
m = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x**2) - np.sum(x)**2)
b = (np.sum(y) - m * np.sum(x)) / n
print(f"Розрахунок: m = {m:.2f}, b = {b:.2f}")
y_pred = m * x + b
plt.scatter(x, y, color='red', label='Дані')
plt.plot(x, y_pred, color='blue', label=f'Лінія: y={m:.2f}x + {b:.2f}')
plt.legend()
plt.title("Метод найменших квадратів")
plt.show()