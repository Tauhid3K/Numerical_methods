import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x=sp.Symbol("x")
t=sp.Symbol("t")
y=1
y=1+sp.integrate(1+t*y,(t,0,x))
y1=sp.expand(y)
print(y1)

y=1+sp.integrate(1+t*y,(t,0,x))
y2=sp.expand(y)
print(y2)

y=1+sp.integrate(1+t*y,(t,0,x))
y3=sp.expand(y)
print(y3)

value=y.subs(x,0.1)
print(value)


print(y.subs(x, 0.1))
# Convert to Python Function
f1 = sp.lambdify(x, y1, "numpy")
f2 = sp.lambdify(x, y2, "numpy")
f3 = sp.lambdify(x, y3, "numpy")
X = np.linspace(0, 1, 100)

plt.plot(X, f1(X), label="1st Approximation")
plt.plot(X, f2(X), label="2nd Approximation")
plt.plot(X, f3(X), label="3nd Approximation")
plt.grid(True)
plt.legend()
plt.show()

# x = sp.Symbol("x")
# t = sp.Symbol("t")

# y = 1

# # Picard Iterations
# y = 1 + sp.integrate(1 + t * y, (t, 0, x))
# y1 = sp.expand(y)

# y = 1 + sp.integrate(1 + t * y.subs(x, t), (t, 0, x))
# y2 = sp.expand(y)
# y = 1 + sp.integrate(1 + t * y.subs(x, t), (t, 0, x))
# y3 = sp.expand(y)
# print(y2)
# print(y3)


