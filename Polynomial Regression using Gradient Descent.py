import numpy as np
import matplotlib.pyplot as plt

# -----------------------
# Data
# -----------------------

x = np.array([20, 30, 40, 50, 60, 70,80,90], dtype=float)
y = np.array([2, 2.5, 3, 4, 6,9,13,18], dtype=float)
x = x /100
y=y/100
# -----------------------
# Initial Values
# -----------------------

b0 = 0
b1 = 0
b2 = 0

learning_rate = 0.001
epochs = 10000

n = len(x)

# -----------------------
# Gradient Descent
# -----------------------

for i in range(epochs):

    db0 = 0
    db1 = 0
    db2 = 0

    mse = 0

    for j in range(n):

        # Prediction
        y_pred = b0 + b1 * x[j] + b2 * x[j]**2

        # Error
        error = y[j] - y_pred

        # MSE
        mse += error**2

        # Gradient
        db0 += (-2/n) * error
        db1 += (-2/n) * x[j] * error
        db2 += (-2/n) * x[j]**2 * error

    # Average MSE
    mse = mse / n

    # Update Parameters
    b0 = b0 - learning_rate * db0
    b1 = b1 - learning_rate * db1
    b2 = b2 - learning_rate * db2

    # Stop Condition
    if mse < 0.001:
        print("Converged!")
        break

# -----------------------
# Result
# -----------------------

print("\nEpoch =", i+1)
print("MSE =", round(mse, 6))

print("\nb0 =", round(b0, 4))
print("b1 =", round(b1, 4))
print("b2 =", round(b2, 4))

print(f"\nEquation:")
print(f"y = {b0:.4f} + {b1:.4f}x + {b2:.4f}x²")

# -----------------------
# Graph
# -----------------------

x_new = np.linspace(min(x), max(x), 100)
y_new = b0 + b1*x_new + b2*x_new**2

plt.scatter(x, y, color="red", label="Original Data")
plt.plot(x_new, y_new, color="blue", label="Polynomial Curve")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Polynomial Regression using Gradient Descent")
plt.grid(True)
plt.legend()

plt.show()