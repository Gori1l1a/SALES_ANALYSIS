import numpy as np

A = np.array([
    [4, -1.5, 2, 0.5],
    [1, 5, -2, 1.2],
    [-2, 1, 6, -1],
    [0.5, 2, -1, 7]
])

B = np.array([11.05, -6.82, 11.5, -0.5])

det = np.linalg.det(A)
print(f"Определитель: {det:.4f}")

cond = np.linalg.cond(A)
print(f"Число обусловленности: {cond:.4f}")

A_inv = np.linalg.inv(A)
X1 = A_inv @ B
print("Решение через обратную матрицу:", X1)

X2 = np.linalg.solve(A, B)
print("Решение через solve():", X2)

print("Разница между методами:", np.linalg.norm(X1 - X2))

print("Проверка A*X - B:", np.linalg.norm(A @ X2 - B))

print("Итоговый ответ (округленный):", np.round(X2, 1))