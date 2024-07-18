def get_matrix(n,m,value):
    matrix = []
    vmatrix = []
    for j in range(m):
        vmatrix.append(value)

    for i in range(n):
        matrix.append(vmatrix)
    return matrix
print(get_matrix(3,4,15))

