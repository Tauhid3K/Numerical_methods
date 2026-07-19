import numpy as np

# x1, x2
X = np.array([
    [1,2],
    [2,1],
    [3,4],
    [4,3],
    [5,5]
])

# y
Y = np.array([4,5,9,10,13])

# Add column of 1
X = np.c_[np.ones(len(X)), X]

# Coefficient
B = np.linalg.inv(X.T @ X) @ X.T @ Y

print("b0 =", B[0])
print("b1 =", B[1])
print("b2 =", B[2])