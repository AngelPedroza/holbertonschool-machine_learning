#!/usr/bin/env python3
"""Add 2 arrays 1D"""


def get_shape(lst, shape):
    """
    Get the len recursively in a matrix
    :param lst: The first element en the previous list
    :param shape: List with save the len in each dimension
    :return: A list with the len of each dimension
    """
    if isinstance(lst, int) or isinstance(lst, float):
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


def add_arrays(arr1, arr2):
    """
    Sum 2 arrays. 1d
    :param arr1: Array 1
    :param arr2: Array 2
    :return: An array sum
    """
    if not (isinstance(arr1, list) and isinstance(arr2, list)):
        return None

    if len(arr1) != len(arr2):
        return None

    final = []
    for i in range(len(arr1)):
        res = arr1[i] + arr2[i]
        final.append(res)

    return final
