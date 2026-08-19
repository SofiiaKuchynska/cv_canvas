import numpy as np
matrix = np.random.randint(0, 5, size=(10, 10))

print("Оригінальна матриця 10x10:")
print(matrix)

result = matrix * 2

print("Матриця, де кожен елемент помножено на 2:")
print(result)