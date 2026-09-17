def matrixmul(
    a: list[list[int | float]], b: list[list[int | float]]
) -> list[list[int | float]] | int:

    a1 = len(a)  # Number of rows in A
    a2 = len(a[0])  # Number of columns in A

    b1 = len(b)  # Number of rows in B
    b2 = len(b[0])  # Number of columns in B

    if a2 != b1:
        return -1

    c = [[0 for _ in range(b2)] for _ in range(a1)]

    for i in range(a1):
        for j in range(b2):
            for k in range(a2):
                c[i][j] += a[i][k] * b[k][j]

    return c