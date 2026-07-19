import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, ]
y = [2, 4, 6, ]

# Initial Values
m = 0
c = 0

learning_rate = 0.01
epochs = 1000

n = len(x)

# Gradient Descent
for i in range(epochs):

    dm = 0
    dc = 0

    for j in range(n):

        y_pred = m * x[j] + c

        dm += (-2/n) * x[j] * (y[j] - y_pred)
        dc += (-2/n) * (y[j] - y_pred)

    m = m - learning_rate * dm
    c = c - learning_rate * dc

print("Slope (m) =", round(m,4))
print("Intercept (c) =", round(c,4))

print(f"\nEquation: y = {m:.4f}x + {c:.4f}")

# -----------------------
# Graph
# -----------------------

y_line = []

for i in x:
    y_line.append(m*i + c)

plt.scatter(x, y, color="red", label="Data")
plt.plot(x, y_line, label="Regression Line")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Regression using Gradient Descent")
plt.grid(True)
plt.legend()

plt.show()