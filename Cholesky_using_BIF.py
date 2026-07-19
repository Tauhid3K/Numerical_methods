import numpy as np

# Symmetric Positive Definite Matrix
A = np.array([
    [4, 12, -16],
    [12, 37, -43],
    [-16, -43, 98]
])

# Cholesky decomposition using NumPy
L = np.linalg.cholesky(A)

print("NumPy Cholesky Decomposition:")
print("="*50)
print("L =")
print(L)
print("\nVerification: L * L.T =")
print(np.dot(L, L.T))