import math
import numpy as np
import matplotlib.pyplot as plt

# Function
def f(x):
    return 0.2+25*x-200*x**2+675*x**3-900*x**4+400*x**5

a = 0
b = 0.8

h = (b-a)/3

x0 = a
x1 = a+h
x2 = a+2*h
x3 = b

result = (3*h/8)*(f(x0)+3*f(x1)+3*f(x2)+f(x3))

print("Integral =", result)

# Graph
x = np.linspace(a,b,100)
y = f(x)

plt.plot(x,y,label="f(x)")
plt.scatter([x0,x1,x2,x3],
            [f(x0),f(x1),f(x2),f(x3)],
            color="red")

plt.fill_between(x,y,alpha=0.3)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Simpson's 3/8 Rule")
plt.grid(True)
plt.legend()

plt.show()