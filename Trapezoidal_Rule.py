import numpy as np
import matplotlib.pyplot as plt

def trapezoidal(f, a, b):
    return (b - a) / 2 * (f(a) + f(b)) 

# Example function
def f(t):
    return 200 * np.log(140000 / (140000 - 2100*t)) - 9.8*t

a, b = 8, 30
result = trapezoidal(f, a, b)

print(f"Trapezoidal Rule: {result:.6f}")

# Plot
t = np.linspace(a, b, 100)
plt.plot(t, f(t), 'b-', linewidth=2)
plt.fill_between([a, b], 0, [f(a), f(b)], alpha=0.3, color='green')
plt.plot([a, b], [f(a), f(b)], 'ro', markersize=8)
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('Trapezoidal Rule')
plt.grid(True)
plt.show()