A = [
    [2.0, 1.0, -1.0],
    [-3.0, -1.0, 2.0],
    [-2.0, 1.0, 2.0]
]

B = [8.0, -11.0, -3.0]

n = 3

# Gauss-Jordan Elimination
for i in range(n):

    # Make pivot equal to 1
    pivot = A[i][i]

    for j in range(n):
        A[i][j] = A[i][j] / pivot

    B[i] = B[i] / pivot

    # Make all other elements in the pivot column zero
    for k in range(n):

        if k != i:

            factor = A[k][i]

            for j in range(n):
                A[k][j] = A[k][j] - factor * A[i][j]

            B[k] = B[k] - factor * B[i]


print("Solution")

print("x =", B[0])
print("y =", B[1])
print("z =", B[2])