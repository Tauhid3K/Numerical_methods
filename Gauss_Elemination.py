A = [
    [2.0, 1.0, -1.0],
    [-3.0, -1.0, 2.0],
    [-2.0, 1.0, 2.0]
]

B = [8.0, -11.0, -3.0]

n = 3


# Forward Elimination

for i in range(n):

    for j in range(i + 1, n):

        factor = A[j][i] / A[i][i]

        for k in range(n):
            A[j][k] = A[j][k] - factor * A[i][k]

        B[j] = B[j] - factor * B[i]


# Back Substitution

x = [0] * n

x[2] = B[2] / A[2][2]

x[1] = (B[1] - A[1][2] * x[2]) / A[1][1]

x[0] = (B[0] - A[0][1] * x[1] - A[0][2] * x[2]) / A[0][0]


print("Solution")

print("x =", x[0])
print("y =", x[1])
print("z =", x[2])