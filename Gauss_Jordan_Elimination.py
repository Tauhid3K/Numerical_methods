import numpy as np

def gauss_jordan(A, b):
    n = len(b)
    
    # Create augmented matrix correctly
    aug = np.zeros((n, n+1), dtype=float)
    for i in range(n):
        for j in range(n):
            aug[i][j] = A[i][j]
        aug[i][n] = b[i]
    
    for i in range(n):
        # Make pivot = 1
        pivot = aug[i][i]
        for j in range(i, n+1):
            aug[i][j] = aug[i][j] / pivot
        
        # Eliminate all other rows
        for k in range(n):
            if k != i:
                factor = aug[k][i]
                for j in range(i, n+1):
                    aug[k][j] = aug[k][j] - factor * aug[i][j]
    
    return aug[:, n]

# Given system
A = [[3, -0.1, -0.2],
     [0.1, 7, -0.3],
     [0.3, -0.2, 10]]

b = [7.85, -19.3, 71.4]

x = gauss_jordan(A, b)

print("Solution:")
print(f"x1 = {x[0]:.6f}")
print(f"x2 = {x[1]:.6f}")
print(f"x3 = {x[2]:.6f}")

# Verify
print("\nVerification:")
print(f"Eq1: {3*x[0] - 0.1*x[1] - 0.2*x[2]:.8f} (Expected: 7.85)")
print(f"Eq2: {0.1*x[0] + 7*x[1] - 0.3*x[2]:.8f} (Expected: -19.3)")
print(f"Eq3: {0.3*x[0] - 0.2*x[1] + 10*x[2]:.8f} (Expected: 71.4)")