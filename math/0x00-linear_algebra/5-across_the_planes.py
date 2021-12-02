#!/usr/bin/env python3
"""Add 2 arrays 2D"""


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


def add_matrices2D(mat1, mat2):
    """
    Sum 2 arrays. 2d
    :param arr1: Array 1
    :param arr2: Array 2
    :return: An array sum
    """
    if len(mat1) != len(mat2):
        return None

    final = []
    for i in range(len(mat1)):
        final.append(add_arrays(mat1[i], mat2[i]))

    if None in final:
        return None

    return final
