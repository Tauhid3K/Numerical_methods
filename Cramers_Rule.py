import numpy as np 

def Cramers_Rule(A, b):
    n = len(b)
    det_A = np.linalg.det(A)

    if det_A == 0:
        print("no unique answer")
        return None
    
    x = np.zeros(n)
    for i in range(n):
        Ai = np.array(A, dtype = float)
        Ai[:, i] = b
        x = np.linalg.det(Ai) / det_A
    return x

A = [[1,1,1],
     [.02,.03,.06],
     [1,1,-1]]
b = [8500, 380, 0]

x = Cramers_Rule(A ,b)

print(f" x = {x[0]:.2f}")

print(f"investment {x[0]+x[1]+x[2]}")
