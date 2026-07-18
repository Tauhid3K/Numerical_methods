import numpy as np
import matplotlib.pyplot as plt

def simpson_38(f, a, b):
    h = (b - a) / 3
    return (3*h / 8) * (f(a) + 3*f(a+h) + 3*f(a+2*h) + f(b))

# Example function
def f(t):
    return 200 * np.log(140000 / (140000 - 2100*t)) - 9.8*t

a, b = 8, 30
result = simpson_38(f, a, b)

print(f"Simpson's 3/8 Rule: {result:.6f}")

# Plot
t = np.linspace(a, b, 100)
plt.plot(t, f(t), 'b-', linewidth=2)
h = (b - a) / 3
x = [a, a+h, a+2*h, b]
y = [f(xi) for xi in x]
plt.plot(x, y, 'ro', markersize=8)
plt.fill_between(t, 0, f(t), alpha=0.3)
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title("Simpson's 3/8 Rule")
plt.grid(True)
plt.show()