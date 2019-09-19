#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy_matrix = []
    for x in matrix:
        copy_matrix.append(list(map(lambda y : y**2, x)))
    return(copy_matrix)
