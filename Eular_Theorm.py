import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x + y

x0 = 0
y0 = 1
h = 0.1
n = 10

x_values = [x0]
y_values = [y0]

x = x0
y = y0

print("\nEULER'S METHOD")
print("="*70)
print("Itr \t\t x\t\t y")
print("="*70)
for i in range(n):
    y = y + h * f(x, y)
    x = x + h
    x_values.append(x)
    y_values.append(y)
    print(f"{i+1}\t\t {x:.4f}\t\t {y:.6f}")
print("="*70)

plt.plot(x_values, y_values, 'bo-', linewidth=2, markersize=8)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Euler's Method")
plt.grid(True)
plt.show()