#!/usr/bin/env python3
"""Add 2 arrays 1D"""


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
