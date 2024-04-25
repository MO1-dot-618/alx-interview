#!/usr/bin/python3
"""
0-pascal_triangle.py
"""

def pascal_triangle(n):
    if n <= 0:
        return []
    else:
        triangle = [[1]]
        # i is the row index, j is the column index
        for i in range(1, n):
            row = []
            for j in range (len(triangle[i - 1]) + 1):
                value1 = triangle[i - 1][j - 1] if j - 1 >= 0 else 0
                value2 = triangle[i - 1][j] if j < len(triangle[i - 1]) else 0
                row.append(value1 + value2)
            triangle.append(row)
        return triangle
            