import numpy as np
import matplotlib.pyplot as plt
# -----------------------
# x values
# -----------------------

x = np.linspace(0,1,100)

# -----------------------
# Picard Approximations
# -----------------------

y0 = 1

y1 = 1 + x + (x**2)/2

y2 = 1 + x + x**2 + (x**3)/6

# -----------------------
# Print value at x = 1
# -----------------------

print("y0 =", y0)
print("y1 =", 1 + 1 + (1**2)/2)
print("y2 =", 1 + 1 + 1**2 + (1**3)/6)

# -----------------------
# Graph
# -----------------------

plt.plot(x,y1,label="1st Approximation")
plt.plot(x,y2,label="2nd Approximation")

plt.scatter(1,y2[-1],color="red")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Picard's Method")

plt.grid(True)
plt.legend()

plt.show()