import numpy as np
import matplotlib.pyplot as plt

# ----------------------
# Data
# ----------------------

X = np.array([
    [1,2],
    [2,1],
    [3,4],
    [4,3],
    [5,5]
], dtype=float)

Y = np.array([4,5,9,10,13], dtype=float)

# ----------------------
# Initial Values
# ----------------------

b0 = 0
b1 = 0
b2 = 0

lr = 0.01
epochs = 1000

n = len(Y)

# ----------------------
# Gradient Descent
# ----------------------

for i in range(epochs):

    db0 = 0
    db1 = 0
    db2 = 0

    for j in range(n):

        y_pred = b0 + b1*X[j][0] + b2*X[j][1]

        error = Y[j] - y_pred

        db0 += (-2/n) * error
        db1 += (-2/n) * X[j][0] * error
        db2 += (-2/n) * X[j][1] * error

    b0 = b0 - lr * db0
    b1 = b1 - lr * db1
    b2 = b2 - lr * db2

# ----------------------
# Result
# ----------------------

print("b0 =", round(b0,4))
print("b1 =", round(b1,4))
print("b2 =", round(b2,4))

print(f"\nEquation:")
print(f"y = {b0:.4f} + {b1:.4f}x1 + {b2:.4f}x2")

# ----------------------
# 3D Graph
# ----------------------

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

# Original Data
ax.scatter(X[:,0], X[:,1], Y, color="red", label="Data")

# Regression Plane
x1 = np.linspace(min(X[:,0]), max(X[:,0]), 10)
x2 = np.linspace(min(X[:,1]), max(X[:,1]), 10)

X1, X2 = np.meshgrid(x1, x2)

Z = b0 + b1*X1 + b2*X2

ax.plot_surface(X1, X2, Z, alpha=0.5)

ax.set_xlabel("x1")
ax.set_ylabel("x2")
ax.set_zlabel("y")

plt.title("Multiple Linear Regression")
plt.legend()

plt.show()