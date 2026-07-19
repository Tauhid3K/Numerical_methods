import matplotlib.pyplot as plt

# -----------------------
# Function
# -----------------------

def f(x, y):
    return 0.5*(x+y)



# -----------------------
# Given Data
# -----------------------

h = 0.5

x=[0,0.5,1,1.5]
y=[2,2.636,3.595,4.968]

# -----------------------
# Calculate Slopes
# -----------------------

f0 = f(x[0], y[0])
f1 = f(x[1], y[1])
f2 = f(x[2], y[2])
f3 = f(x[3], y[3])

# -----------------------
# Predictor
# -----------------------

x4 = x[3] + h

y_pred = y[0] + (4*h/3) * (2*f1 - f2 + 2*f3)

print("Predicted Value =", round(y_pred, 6))

# -----------------------
# Corrector
# -----------------------

f4 = f(x4, y_pred)

y_corr = y[2] + (h/3) * (f2 + 4*f3 + f4)

print("Corrected Value =", round(y_corr, 6))

# -----------------------
# Add New Point
# -----------------------

x.append(x4)
y.append(y_corr)

# -----------------------
# Graph
# -----------------------

plt.plot(x, y, marker="o", label="Milne Solution")

plt.scatter(x4, y_corr,
            color="red",
            s=100,
            label="Predicted/Corrected Point")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Milne's Predictor-Corrector Method")
plt.grid(True)
plt.legend()

plt.show()