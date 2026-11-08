import numpy as np
from scipy.integrate import quad, dblquad
import matplotlib.pyplot as plt

def f1(x):
    return x * np.sin(x)

def f2(y, x):
    return x + y

def border_min(x):
    return 0

def border_max(x):
    return x

integral1 = quad(f1, 0, np.pi)[0]
print(f"1. Интеграл: {integral1:.6f}")
print(f"Погрешность : {abs(integral1 - np.pi):.6f}")

integral2 = dblquad(f2, 0, 1, border_min, border_max)[0]
print(f"\n2. Двойной интеграл: {integral2:.6f}")
print(f"Погрешность (должно быть 0.5): {abs(integral2 - 0.5):.6f}")

print("\n3. Метод Монте-Карло:")
N_list = [1000, 10000, 100000, 1000000]
errors = []

for N in N_list:
    x = np.random.rand(N)
    y = np.random.rand(N) * x
    mc_value = np.mean(x + y) * 0.5
    error = abs(mc_value - 0.5)
    errors.append(error)
    print(f"   Для N={N} результат: {mc_value:.6f}, ошибка: {error:.6f}")

plt.figure(figsize=(10, 5))
plt.loglog(N_list, errors, 'bo-')
plt.title("Зависимость ошибки от N")
plt.xlabel("N ")
plt.ylabel("Ошибка")
plt.grid(True)
plt.show()
