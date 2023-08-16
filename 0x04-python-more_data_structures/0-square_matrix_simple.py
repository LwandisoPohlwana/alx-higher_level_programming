#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix."""
    NewMatrix = matrix.copy()

    for i in range(len(matrix)):
        NewMatrix[i] = list(map(lambda x: x**2, matrix[i]))

    return (NewMatrix)
