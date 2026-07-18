import numpy as np
import matplotlib.pyplot as plt
import math

def lagrange_interpolation(x, y, xp):

    n = len(x)
    result = 0
    
    for i in range(n):
        # Calculate L_i(xp)
        term = y[i]
        for j in range(n):
            if i != j:
                term = term * (xp - x[j]) / (x[i] - x[j])
        result += term
    
    return result

# Your data
x_data = [0, 1, 2, 3, 4]
y_data = [1, 2, 4, 8, 16]

# Test
xp = 2.5
result = lagrange_interpolation(x_data, y_data, xp)
print(f"Lagrange Interpolation at x = {xp}: {result:.4f}")
print(f"Actual value (2^{xp}): {2**xp:.4f}")
print(f"Error: {abs(result - 2**xp):.4f}")

# Generate smooth curve
x = np.linspace(0, 4, 400)
y = [lagrange_interpolation(x_data, y_data, xi) for xi in x]

# Plot
plt.plot(x, y, 'g-', linewidth=2, label='Lagrange Interpolation')
plt.plot(x_data, y_data, 'ko', markersize=8, label='Data points')
plt.plot(xp, result, 'ro', markersize=10, label=f'Result at x={xp}')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagrange Interpolation')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()