#!/usr/bin/python3


"""
This module contains a function that divides the numbers of a matrix.
"""


def matrix_divided(matrix, div):
    """Divide the integer or float numbers of a matrix by a given number.

    Args:
        matrix (list[list[int, float]]): The matrix of numbers.
        div (int, float): The number by which to divide the matrix.

    Returns:
        A new matrix with the result of the division.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
                   or if the division number is not an integer or float.
        ZeroDivisionError: If the division number is zero.
        TypeError: If the rows of the matrix do not have the same size.

    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError(error_msg)

    row_size = len(matrix[0])
    result_matrix = []

    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError(error_msg)

        result_row = [round(num / div, 2) for num in row]
        result_matrix.append(result_row)

    return result_matrix

