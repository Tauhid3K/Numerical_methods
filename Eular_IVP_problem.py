import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    return y - 0.5*np.exp(0.5*t)*np.sin(5*t) + 5*np.exp(0.5*t)*np.cos(5*t)

def exact(t):
    return np.exp(0.5*t)*np.sin(5*t)

def euler(h):
    t = np.arange(0, 5+h, h)
    y = np.zeros(len(t))
    for i in range(len(t)-1):
        y[i+1] = y[i] + h*f(t[i], y[i])
    return t, y

h_values = [0.1, 0.05, 0.01, 0.005, 0.001]

# Print table in requested format
print("\nEULER'S METHOD")
print("="*100)
print("h \t\t t=1\t\t t=2\t\t t=3\t\t t=4\t\t t=5")
print("="*100)

for h in h_values:
    t, y = euler(h)
    vals = [y[int(tp/h)] for tp in [1,2,3,4,5]]
    print(f"{h:.3f} \t\t {vals[0]:.6f}\t {vals[1]:.6f}\t {vals[2]:.6f}\t {vals[3]:.6f}\t {vals[4]:.6f}")

exact_vals = [exact(tp) for tp in [1,2,3,4,5]]
print("-"*100)
print(f"Exact \t\t {exact_vals[0]:.6f}\t {exact_vals[1]:.6f}\t {exact_vals[2]:.6f}\t {exact_vals[3]:.6f}\t {exact_vals[4]:.6f}")
print("="*100)

# Plot
plt.figure(figsize=(10,5))
for h in h_values:
    t, y = euler(h)
    plt.plot(t, y, '--', label=f'h={h}')
plt.plot(np.linspace(0,5,1000), exact(np.linspace(0,5,1000)), 'k-', linewidth=2, label='Exact')
plt.xlabel('t')
plt.ylabel('y')
plt.title("Euler's Method")
plt.grid(True)
plt.legend()
plt.show()