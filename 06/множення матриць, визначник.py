import numpy as np
A = np.random.randint(0, 100, size=(67, 67))
B = np.random.randint(0, 20, size=(67, 67))
print("A - матриця\n", A, "\n")
print("B - матриця\n", B, "\n")
matrix = np.dot(A, B)
print("A*B\n", matrix)
det = np.linalg.det(matrix)
print("Визначник матриці A на B\n", round(det, 5))
if det != 0:
    inv = np.linalg.inv(matrix)
    print("Обернена до цієї ж\n", np.round(inv, 5))
    check = np.dot(matrix, inv)
    print("Перевірка оберненої\n", np.round(check))
else:
    print("Визначник = 0, оберненої матриці не існує")
