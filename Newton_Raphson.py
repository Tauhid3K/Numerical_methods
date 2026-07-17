import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 2*x - 5  # Root ≈ 2.0946

def f_prime(x):
    return 3*x**2 - 2

def newton_raphson(f, f_prime, a, esp_abs):
    print('Result')
    print("Iter\t\t x\t\t f(x)\t\t |x-x_old|")

    iteration = 0
    x_old = a

    while True:
        x = x_old - f(x_old)/f_prime(x_old)

        print(f"{iteration}\t\t {x:.6f}\t {f(x):.6f}\t {abs(x - x_old):.6f}") 

        if abs(x-x_old) < esp_abs:
            print(f"Converged after {iteration + 1} iterations.")
            return x
        
        x_old = x
        iteration += 1

a = 2.0
esp_abs = 0.001
root = newton_raphson(f, f_prime, a, esp_abs)

print(f"\nRoot x = {root:.6f}")
print(f"\nf(root) x = {f(root):.6e}")

# Plot
x = np.linspace(1, 5, 400)
y = f(x)

plt.plot(x, y, 'b-', linewidth=2)
plt.plot(root, f(root), 'ro', markersize=8)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(root, color='red', linestyle='--', linewidth=0.8)  
plt.title('Newton-Raphson Method Root Finding')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()
plt.show()