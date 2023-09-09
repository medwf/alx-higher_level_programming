#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            separated = " "
            if j == len(matrix[i]) - 1:
                separated = ""
            print("{:d}".format(matrix[i][j]), end=separated)
        print("".format())
