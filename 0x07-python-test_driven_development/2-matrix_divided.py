#!/usr/bin/python3

"""
A function that divides all element of a matrix

The function takes two parameter
"""


def matrix_divided(matrix, div):
    """
    Divides all the elements of a mtrix

    matrix(param): the matrix parameter
    div(param): divisor of the matrix.
    return: a new matrix which is the result of the division.

    """
    if not (isinstance(matrix, list) and all(isinstance(row, list)
            and all(isinstance(num, (int, float))
            for num in row) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists)\
                        of integers/floats")
    if any(len(row) != len(matrix[0]) for row in matrix[1:]):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            new_element = round(num / div, 2)
            new_row.append(new_element)
        new_matrix.append(new_row)

    return new_matrix
