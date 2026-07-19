import numpy as np
import matplotlib.pyplot as plt

# -----------------------
# Function
# -----------------------

def f(x):
    return 0.2+25*x-200*x**2+675*x**3-900*x**4+400*x**5

# Interval
a = 0
b = 0.8

# Trapezoidal Rule
h = b - a

result = (h/2) * (f(a) + f(b))

print("Integral =", result)

# -----------------------
# Graph
# -----------------------

x = np.linspace(a, b, 100)
y = f(x)

plt.plot(x, y, label="f(x)")

# Trapezoid
plt.fill([a, a, b, b],
         [0, f(a), f(b), 0],
         alpha=0.6,
         label="Trapezoid")

plt.scatter([a, b], [f(a), f(b)], color="red")

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Trapezoidal Rule")
plt.grid(True)
plt.legend()

plt.show()