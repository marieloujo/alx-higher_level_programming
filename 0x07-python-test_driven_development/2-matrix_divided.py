#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
The 2-matrix_divided module supplies one function, matrix_divided(matrix, div).
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of the matrix, rounded to 2 decimal places

    Args:
        matrix ((list of lists) of integers/floats):
            is the two dimentionnal list of int or float
        div (int/foat): is the value of divider

    Return
        new matrix contains each element of matrix divide by div
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) \
            of integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) \
                of integers/floats")
        for col in row:
            if type(col) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) \
                    of integers/floats")
    if len(matrix) > 0:
        if any(len(lst) != len(matrix[0]) for lst in matrix[1:]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(x / div, 2) for x in row] for row in matrix]
