#!/usr/bin/python3
"""

    This module has a function to divide all elements of a matrix by a number

"""

def matrix_divided(matrix, div):
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
        
    mat_div = []
    for i in range(len(matrix)):
        if i != len(matrix) - 1:
            if len(matrix[i]) != len(matrix[i + 1]):
                raise TypeError('Each row of the matrix must have the same size')
        mat_div.append([])
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], int) and not isinstance(matrix[i][j], float):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            mat_div[i].append(float("{0:.2f}".format(matrix[i][j] / div)))

    return (mat_div)
