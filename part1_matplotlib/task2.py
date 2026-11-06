import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(-8,8,1000)
y=4/(x**2-4)

y1=np.ma.masked_where(np.abs(x**2-4)<0.05,y)

plt.figure(figsize=(12,6))
           

plt.plot(x,y1,label='y(x)')

plt.axvline(x=2, color='r', linestyle='--', label='Асимптота x = 2')
plt.axvline(x=-2, color='r', linestyle='--', label='Асимптота x = -2')

plt.ylim(-10,10)
plt.title("График функции y(x)")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()

plt.tight_layout()
plt.savefig('part1_matplotlib/img/task2.png')
plt.show()

