import numpy as np
import matplotlib.pyplot as plt
import math  # Add this import

# Simple interpolation for equally spaced data
def interp_forward(x, y, xp):
    """Forward interpolation - use when xp is near start"""
    n = len(x)
    h = x[1] - x[0]
    u = (xp - x[0]) / h
    result = y[0]
    
    for i in range(1, n):
        term = 1
        for j in range(i):
            term *= (u - j)
        result += (term * np.diff(y, n=i)[0]) / math.factorial(i)  # Changed here
    
    return result

def interp_backward(x, y, xp):
    """Backward interpolation - use when xp is near end"""
    n = len(x)
    h = x[1] - x[0]
    u = (xp - x[-1]) / h
    result = y[-1]
    
    for i in range(1, n):
        term = 1
        for j in range(i):
            term *= (u + j)
        result += (term * np.diff(y, n=i)[-1]) / math.factorial(i)  # Changed here
    
    return result

# Your data
x_data = [0, 1, 2, 3, 4]
y_data = [1, 2, 4, 8, 16]

# Test
xp = 2.5
forward_result = interp_forward(x_data, y_data, xp)  # Store the result
backward_result = interp_backward(x_data, y_data, xp)  # Store the result

print(f"Forward: {forward_result:.4f}")
print(f"Backward: {backward_result:.4f}")
print(f"Actual: {2**xp:.4f}")

# Generate curve
x = np.linspace(0, 4, 400)
y_forward = [interp_forward(x_data, y_data, xi) for xi in x]

# Plot
plt.plot(x, y_forward, 'b-', linewidth=2, label='Forward Interpolation')
plt.plot(x_data, y_data, 'ko', markersize=8, label='Data points')
plt.plot(xp, forward_result, 'ro', markersize=10, label=f'Result = {forward_result:.4f}')

plt.grid(True, alpha=0.3)
plt.legend()
plt.show()