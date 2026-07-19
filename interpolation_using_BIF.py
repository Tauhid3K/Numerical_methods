import numpy as np
import matplotlib.pyplot as plt

# Your data
x_data = [0, 1, 2, 3, 4]
y_data = [1, 2, 4, 8, 16]

# Using NumPy's linear interpolation (built-in)
xp = 2.5
result = np.interp(xp, x_data, y_data)

print(f"NumPy Linear Interp Result: {result:.4f}")
print(f"Actual: {2**xp:.4f}")

# Generate curve
x = np.linspace(0, 4, 400)
y = np.interp(x, x_data, y_data)

# Plot
plt.plot(x, y, 'b-', linewidth=2, label='Linear Interpolation')
plt.plot(x_data, y_data, 'ko', markersize=8, label='Data points')
plt.plot(xp, result, 'ro', markersize=10, label=f'Result = {result:.4f}')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()