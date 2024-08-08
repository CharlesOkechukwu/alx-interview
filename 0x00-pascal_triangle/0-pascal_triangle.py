#!/usr/bin/python3
"""module to create a pascal's triangle of n rows"""


def pascal_triangle(n):
    """create pascal triangle of n rows"""
    if n <= 0:
        return []
    p_arr = []
    i = 0
    while (i < n):
        arr = []
        if i == 0:
            arr.append(1)
            p_arr.append(arr)
        else:
            row = i + 1
            col = 0
            while col < row:
                if col == 0:
                    arr.append(1)
                elif col == (row - 1):
                    arr.append(1)
                else:
                    num = p_arr[i - 1][col - 1] + p_arr[i - 1][col]
                    arr.append(num)
                col += 1
            p_arr.append(arr)
        i += 1
    return p_arr
