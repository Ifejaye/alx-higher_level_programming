def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in range(len(i)):
            print("matrix[i][j])")
        print("{}".format('\n'))


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix_integer(matrix)