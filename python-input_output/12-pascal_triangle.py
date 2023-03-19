#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        triangle = triangles[-1]
        triple = [1]
        for x in range(len(triangle) - 1):
            triple.append(triangle[x] + triangle[x + 1])
        triple.append(1)
        triangles.append(triple)
    return triangles
