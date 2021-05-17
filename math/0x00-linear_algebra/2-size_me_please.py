#!/usr/bin/env python3
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
