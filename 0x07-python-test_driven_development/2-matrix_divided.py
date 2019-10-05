#!/usr/bin/python3

"""
Function that divides all elements of a matrix
Matrix must be formed by integers or floats
Matrix must be of the same size
"""


def matrix_divided(matrix, div):

    """
    Raise a TypeError is matrix is not of integers or floats
    Raise a TypeError if eash row of matrix are not of the same size
    Div must be a number and different to 0, else raise error
    Return new matrix
    """
    n_matrix = []
    if matrix == []:
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_lenght = len(matrix[0])
    for m_list in matrix:
        if not isinstance(m_list, list):
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
            if len(m_list) != row_lenght:
                raise TypeError("Each row of the matrix "
                                "must have the same size")
        for x in m_list:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")

        for row in matrix:
            n_matrix.append([round(m_list / div, 2) for m_list in row])
        return n_matrix
