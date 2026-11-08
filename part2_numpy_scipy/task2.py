import numpy as np

while True:
    try:
        lengths = np.array([float(x) for x in input("Длины участков: ").split()])
        speeds = np.array([float(x) for x in input("Скорости: ").split()])
        k = int(input("k: "))
        p = int(input("p: "))
        t = float(input("t: "))

        if len(lengths) != len(speeds):
            print("Ошибка: размеры массивов не совпадают!")
        elif not (1 <= k <= p <= len(lengths)):
            print("Ошибка: неверные k или p!")
        else:
            break
    except ValueError:
        print("Ошибка: введите числа!")

L = lengths[k-1:p]
V = speeds[k-1:p]

times = L / V
S = L.sum()
T = times.sum()
avg_speed = S / T

print(f"S = {S} км, T = {T:.2f} ч, V = {avg_speed:.2f} км/ч")

if t >= T:
    print("Машина доехала до конца.")
else:
    cumulative = np.cumsum(times)
    i = np.searchsorted(cumulative, t)
    time_before = cumulative[i-1] if i > 0 else 0
    dist = (t - time_before) * V[i]

    print(f"Через {t} ч машина на участке {k + i}, {dist:.1f} км от начала")