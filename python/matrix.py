def matrix(A, B):
    rowsofa = len(A)
    colsofa = len(A[0])
    colsofb = len(B[0])
    result = [[0 for k in range(colsofb)] for k in range(rowsofa)]
    for i in range(rowsofa):
        for j in range(colsofb):
            for k in range(colsofa):
                result[i][j] += A[i][k] * B[k][j]
    return result

def matrix_power(A, M):
    if len(A) != len(A[0]):
        print("Input must be a square matrix.")
    elif M <= 0:
        print("M must be a positive integer.")
    result = [[int(i == j) for i in range(len(A))] for j in range(len(A))]

    for k in range(M):
        result = matrix(result, A)
    return result

A = [[1, 2], [3, 4]]
M = int(input("Enter power of the matrix"))
result = matrix_power(A, M)

print(f"A^{M} = ")
for row in result:
    print(row)
