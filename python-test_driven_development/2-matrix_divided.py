#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.
    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """
    new_matrix = []
    mat = []
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a\
 matrix (list of lists) of integers/floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a\
 matrix (list of lists) of integers/floats")
    elif len(matrix) == 1:
        for item in matrix[0]:
            if type(item) not in [int, float]:
                raise TypeError("matrix must be a\
 matrix (list of lists) of integers/floats")
            mat.append(float("{:.2f}".format(item / div)))
        new_matrix.append(mat)
        return new_matrix
    else:
        length = len(matrix[0])
        for char in matrix:
            if not isinstance(char, list):
                raise TypeError("matrix must be a\
 matrix (list of lists) of integers/floats")
            if len(char) != length:
                raise TypeError("Each row of the matrix\
 must have the same size")
            for num in char:
                if type(num) not in [int, float]:
                    raise TypeError("matrix must be a\
 matrix (list of lists) of integers/floats")
                mat.append(float("{:.2f}".format(num / div)))
            new_matrix.append(mat)
            mat = []
        return new_matrix
