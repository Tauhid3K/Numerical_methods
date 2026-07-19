import numpy as np
import matplotlib.pyplot as plt

# -----------------------
# Data
# -----------------------

x = np.array([20,30,40,50,60,70,80,90],dtype=float)
y = np.array([2,2.5,3,4,6,9,13,18],dtype=float)

# -----------------------
# Required Sums
# -----------------------

n = len(x)

sx = np.sum(x)
sx2 = np.sum(x**2)
sx3 = np.sum(x**3)
sx4 = np.sum(x**4)

sy = np.sum(y)
sxy = np.sum(x*y)
sx2y = np.sum((x**2)*y)

print("Σx =", sx)
print("Σx² =", sx2)
print("Σx³ =", sx3)
print("Σx⁴ =", sx4)
print("Σy =", sy)
print("Σxy =", sxy)
print("Σx²y =", sx2y)

# -----------------------
# Matrix
# -----------------------

A = np.array([
    [n, sx, sx2],
    [sx, sx2, sx3],
    [sx2, sx3, sx4]
])

B = np.array([
    sy,
    sxy,
    sx2y
])

# Solve
coef = np.linalg.solve(A,B)

a = coef[0]
b = coef[1]
c = coef[2]

print("\nEquation")
print(f"y = {a:.4f} + {b:.4f}x + {c:.6f}x²")

# -----------------------
# Graph
# -----------------------

x_new = np.linspace(min(x),max(x),100)

y_new = a + b*x_new + c*x_new**2

plt.scatter(x,y,color="red",label="Data")
plt.plot(x_new,y_new,label="Polynomial Curve")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Polynomial Regression")
plt.grid(True)
plt.legend()

plt.show()