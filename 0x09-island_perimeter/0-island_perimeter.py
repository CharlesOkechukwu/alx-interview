#!/usr/bin/python3
"""module to solve island perimeter problem"""


def island_perimeter(grid):
    """return the perimeter of the island described in grid"""
    perimeter = 0
    row = 0
    while row < len(grid):
        column = 0
        while column < len(grid[row]):
            if grid[row][column] == 1:
                perimeter += 4
                if row - 1 >= 0 and grid[row - 1][column] == 1:
                    perimeter -= 1
                if row + 1 < len(grid) and grid[row + 1][column] == 1:
                    perimeter -= 1
                if column - 1 >= 0 and grid[row][column - 1] == 1:
                    perimeter -= 1
                if column + 1 < len(grid[row]) and grid[row][column + 1] == 1:
                    perimeter -= 1
            column += 1
        row += 1
    return perimeter
