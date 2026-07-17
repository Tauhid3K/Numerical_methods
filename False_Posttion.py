import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**4 - 0.165*x**2 + 3.993e-4

def false_position(f, a, b, esp_step, esp_abs, max_iter):
    if f(a) * f(b) >= 0:
        print("Must be defferent signed")
        return None 
    
    print("Iteration result ")
    print("Iter\t\t a\t\t b\t\t c\t\t f(c)\t\t ea(%)")

    iteration = 0
    c_old = a
    
    while iteration < max_iter:
        c = (a*f(b)-b*f(a))/(f(b)-f(a))
        fc = f(c)

        if iteration == 0:
            ea = "---"
        else:
            ea = abs((c-c_old)/c) *  100

        print(f"{iteration}\t {a:.6f}\t {b:.6f}\t {c:.6f}\t {fc:.6e}\t {ea}")

        if abs(b-a) < esp_step or abs(c - c_old) < esp_abs:
            print(f"\nConverged after {iteration + 1} iterations.")
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
 
        iteration += 1
        c_old = c

a = 0.02
b = 0.05
esp_step = 0.0001
esp_abs = 0.0001
max_iter = 3
root = false_position(f, a, b, esp_step, esp_abs, max_iter)

print(f"\nRoot found: x = {root:.8f} m")
print(f"Depth in cm: {root*100:.4f} cm")
print(f"f(root) = {f(root):.6e}")

# Plot
x = np.linspace(0.01, 0.06, 400)
y = f(x)

plt.plot(x, y, 'b-', linewidth=2)
plt.plot(root, f(root), 'ro', markersize=8, label=f'Root = {root:.5f} m')
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(root, color='red', linestyle='--', linewidth=0.8)  
plt.title('False Position Method: Floating Ball Submerged Depth')
plt.xlabel('Depth x (m)')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()