import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x)*(3.2*np.sin(x) - .5*np.cos(x))

def bisection(f, a, b, esp_step, esp_abs):
    if f(a) * f(b) >= 0:
        print("Must have different signs")
        return None

    print("Iteration results: ")
    print("Itr \t\t a\t\t b\t\t c\t\t f(c) \t\t |b-a|")
    print("-" * 75)

    iteration = 0
    c_old = a
    
    while True: 
        c = (a + b) /2
        fc = f(c)

        print(f"{iteration}\t {a:.6f}\t{b:.6f}\t {c:.6f}\t {fc:.6e}\t {abs(b-a):.6f}") 

        if (b-c)< esp_step or abs(fc) < esp_abs:
            print("-" * 75)
            print(f"Converged after {iteration + 1} iterations.")
            return c

        if f(a) * fc < 0:
            b = c
        else:   
            a = c   

        c_old = c
        iteration += 1

a = 3.0
b = 4.0
esp_step = 0.001
esp_abs = 0.001

root = bisection(f, a, b, esp_step, esp_abs)

print(f"Root found: {root:.6f}")
print(f"f(root) = {f(root):.6e}")

# Plot (small and simple)
x = np.linspace(2.5, 4.5, 400)
y = f(x)

plt.plot(x, y, 'b-', linewidth=2)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(root, color='r', linestyle='--', label=f'Root = {root:.6f}')
plt.plot(root, f(root), 'ro', markersize=8)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Root finding using Bisection Method')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show() 