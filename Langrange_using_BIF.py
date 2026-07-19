import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

# Your data
x_data = [0, 1, 2, 3, 4]
y_data = [1, 2, 4, 8, 16]

# Using SciPy's built-in Lagrange interpolation
poly = lagrange(x_data, y_data)

# Test
xp = 2.5
result = poly(xp)

print(f"Lagrange Interpolation at x = {xp}: {result:.4f}")
print(f"Actual value (2^{xp}): {2**xp:.4f}")
print(f"Error: {abs(result - 2**xp):.4f}")

# Generate smooth curve
x = np.linspace(0, 4, 400)
y = poly(x)

# Plot
plt.plot(x, y, 'g-', linewidth=2, label='Lagrange Interpolation')
plt.plot(x_data, y_data, 'ko', markersize=8, label='Data points')
plt.plot(xp, result, 'ro', markersize=10, label=f'Result at x={xp}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagrange Interpolation (SciPy)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()