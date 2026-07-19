import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5])
y = np.array([2,3,5,4,6])

b, a = np.polyfit(x, y, 1)

print("Equation:")
print(f"y = {a:.2f} + {b:.2f}x")

plt.scatter(x, y)
plt.plot(x, a + b*x)

plt.grid(True)
plt.show()