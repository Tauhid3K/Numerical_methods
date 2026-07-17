import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 2*x - 5  # Root ≈ 2.0946

def g(x):
    # Rearrange f(x) = 0 to x = g(x)
    # From x³ - 2x - 5 = 0
    # x³ = 2x + 5
    # x = (2x + 5)^(1/3)
    return (2*x + 5)**(1/3)

def fixed_point_iteration(g, a, esp_abs, max_iter):
    print('Fixed-Point Iteration Results:')
    print("Iter\t\t x\t\t g(x)\t\t |x - x_old|")
    print("-" * 70)

    iteration = 0
    x_old = a

    while iteration < max_iter:
        x = g(x_old)

        print(f"{iteration}\t\t {x:.6f}\t {g(x):.6f}\t {abs(x - x_old):.6f}") 

        if abs(x - x_old) < esp_abs:
            print(f"Converged after {iteration + 1} iterations.")
            return x
        
        x_old = x
        iteration += 1
    
    print("Max iterations reached.")
    return x

# Initial guess
a = 2.0
esp_abs = 0.001
max_iter = 4
root = fixed_point_iteration(g, a, esp_abs, max_iter)

print(f"\nRoot found: x = {root:.8f}")
print(f"f(root) = {f(root):.6e}")

# Plot
x = np.linspace(1, 5, 400)
y = f(x)

plt.plot(x, y, 'b-', linewidth=2, label='f(x)')
plt.plot(root, f(root), 'ro', markersize=8, label=f'Root = {root:.5f}')
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(root, color='red', linestyle='--', linewidth=0.8)  
plt.title('Fixed-Point Iteration Method: x³ - 2x - 5 = 0')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()