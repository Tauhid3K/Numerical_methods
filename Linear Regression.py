import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, ]
y = [2, 4, 6, ]

n = len(x)

sum_x = sum(x)
sum_y = sum(y)

sum_xy = 0
sum_x2 = 0

for i in range(n):
    sum_xy += x[i] * y[i]
    sum_x2 += x[i] * x[i]

# Slope
b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)

# Intercept
a = (sum_y - b * sum_x) / n

print("a =", a)
print("b =", b)

print("\nRegression Equation")
print(f"y = {a:.2f} + {b:.2f}x")

# -----------------
# Graph
# -----------------

y_line = []

for i in x:
    y_line.append(a + b * i)

plt.scatter(x, y, color="red", label="Data")
plt.plot(x, y_line, label="Regression Line")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Regression")
plt.grid(True)
plt.legend()

plt.show()