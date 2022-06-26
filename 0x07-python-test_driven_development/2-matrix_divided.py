#!/usr/bin/python3
"""My function: matrix_divided
     divide matrix elements with a given number
     Return:
         A new matrix
"""


def matrix_divided(matrix, div):
    """

    """
    if not all(type(i) in [int, float] for row in matrix for i in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[eval("{:.2f}".format(num / div)) for num in row]for row in matrix]
    return new_matrix
