#!/usr/bin/python3
"""This module defines matrix_divided, which divides every matrix element."""


def matrix_divided(matrix, div):
    """Returns a new matrix with every element divided by div.

    Results are rounded to 2 decimal places. The matrix must be a list of
    lists of integers or floats with rows of the same size, and div must be
    a non-zero number.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list) or not matrix or
            not all(isinstance(row, list) and row for row in matrix) or
            not all(isinstance(x, (int, float))
                    for row in matrix for x in row)):
        raise TypeError(msg)
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(x / div, 2) for x in row] for row in matrix]
