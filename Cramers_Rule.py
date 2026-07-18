import numpy as np

def cramers_rule(A, b):
    n = len(b)
    det_A = np.linalg.det(A)
    
    if det_A == 0:
        print("No unique solution")
        return None
    
    x = np.zeros(n)
    for i in range(n):
        A_i = np.array(A, dtype=float)
        A_i[:, i] = b
        x[i] = np.linalg.det(A_i) / det_A
    
    return x

# Equations: x + y + z = 8500
#            0.02x + 0.03y + 0.06z = 380
#            x + y - z = 0

A = [[1, 1, 1],
     [0.02, 0.03, 0.06],
     [1, 1, -1]]

b = [8500, 380, 0]

# Solve
x = cramers_rule(A, b)

# Display results

print("\nINVESTMENT SOLUTION")
print("="*50)
print(f"Amount at 2% (x) = {x[0]:.2f} taka")
print(f"Amount at 3% (y) = {x[1]:.2f} taka")
print(f"Amount at 6% (z) = {x[2]:.2f} taka")

# Verification
print("\nVERIFICATION")
print("="*50)
print(f"Total Investment: {x[0]+x[1]+x[2]:.2f} taka")
print(f"Total Interest: {0.02*x[0] + 0.03*x[1] + 0.06*x[2]:.2f} taka")
print(f"6% = Sum of others: {x[2]:.2f} = {x[0]:.2f} + {x[1]:.2f}")