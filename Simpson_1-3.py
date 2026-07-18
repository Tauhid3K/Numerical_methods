import numpy as np
import matplotlib.pyplot as plt

def simpson_13(f, a, b):
    h = (b - a) / 2
    return (h / 3) * (f(a) + 4*f((a+b)/2) + f(b))

# Example function
def f(t):
    return 200 * np.log(140000 / (140000 - 2100*t)) - 9.8*t

a, b = 8, 30
result = simpson_13(f, a, b)

print(f"Simpson's 1/3 Rule: {result:.6f}")

# Plot
t = np.linspace(a, b, 100)
plt.plot(t, f(t), 'b-', linewidth=2)
x = [a, (a+b)/2, b]
y = [f(a), f((a+b)/2), f(b)]
plt.plot(x, y, 'ro', markersize=8)
plt.fill_between(t, 0, f(t), alpha=0.3)
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title("Simpson's 1/3 Rule")
plt.grid(True)
plt.show()