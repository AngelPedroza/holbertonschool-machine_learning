#!/usr/bin/env python3
def get_len(lst, shape):
    if isinstance(lst, int):
        return None

    shape.append(len(lst))
    get_len(lst[0], shape)
    return shape


def matrix_shape(matrix):
    return get_len(matrix, [])
