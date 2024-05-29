#!/usr/bin/env python
""" This function is used to generate the output of the pascal triangle"""


def pascal_triangle(n):
    """ Generates the pascal triangle from the given number of points """
    if n == 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    else:
        triangle = pascal_triangle(n - 1)
        last_row = triangle[-1]
        new_row = [1]
        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])
        new_row.append(1)
        triangle.append(new_row)
    return triangle
