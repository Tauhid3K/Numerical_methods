import numpy as np

def cholesky(A):
    n = len(A)
    L = np.zeros((n, n))
    
    for i in range(n):
        for j in range(i+1):
            if i == j:  # Diagonal elements
                sum_val = 0
                for k in range(j):
                    sum_val += L[j][k] ** 2
                L[j][j] = np.sqrt(A[j][j] - sum_val)
            else:  # Off-diagonal elements
                sum_val = 0
                for k in range(j):
                    sum_val += L[i][k] * L[j][k]
                L[i][j] = (A[i][j] - sum_val) / L[j][j]
    
    return L

# Symmetric Positive Definite Matrix
A = [[4, 12, -16],
     [12, 37, -43],
     [-16, -43, 98]]

L = cholesky(A)

print("Cholesky Decomposition:")
print("L =")
print(L)
print("\nL * L^T =")
print(np.dot(L, L.T))