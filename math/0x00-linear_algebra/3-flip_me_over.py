#!/usr/bin/env python3
"""Matrix Transpose"""


def get_shape(lst, shape):
    """
    Get the len recursively in a matrix
    :param lst: The first element en the previous list
    :param shape: List with save the len in each dimension
    :return: A list with the len of each dimension
    """
    if isinstance(lst, int):
        return None

    shape.append(len(lst))
    get_shape(lst[0], shape)
    return shape


def matrix_shape(matrix):
    """
    Call the recursive function
    :param matrix: Matrix to get the shape
    :return: A list with the matrix shape
    """
    return get_shape(matrix, [])


def zeros_matrix(rows, cols):
    """
    Creates a matrix filled with zeros.
    :param shape: the number of rows the matrix should have

    :return: list of lists that form the matrix
    """
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0)

    return M


def matrix_transpose(matrix):
    """
    Transpose a matrix
    :param matrix: Matrix to transpose
    :return: The transposed matrix
    """
    shape = matrix_shape(matrix)
    MT = zeros_matrix(rows=shape[1], cols=shape[0])

    rows = shape[0]
    cols = shape[1]

    for i in range(rows):
        for j in range(cols):
            MT[j][i] = matrix[i][j]

    return MT
