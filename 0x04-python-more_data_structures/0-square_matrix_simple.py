#!/usr/bin/python3
"""

This module has one function to compute the square value of a matrix values

"""


def square_matrix_simple(matrix=[]):
    """
    This function computes the square value of a matrix values

    Args: matrix - a 2D matrix

    Returns: A new 2D square matrix bassed off matrix elements

    """

    mat = []

    for i in range(len(matrix)):
        mat.append([])
        for j in range(len(matrix[i])):
            mat[i].append(matrix[i][j] ** 2)
    return (mat)
