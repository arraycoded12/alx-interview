#!/usr/bin/python3
"""This module contains the function island_perimeter problem solution
"""


def island_perimeter(grid):
    """This function returns the perimeter of the island described in grid
    """

    if not grid:
        return 0  # empty grid has no perimeter
    perimeter = 0  # perimeter of the island
    for row in range(len(grid)):  # rows in grid
        for col in range(len(grid[row])):  # columns in grid
            """ if the cell is land (1) then check the perimeter of the cell
                and add it to the perimeter of the island described in grid
            """
            if grid[row][col] == 1:
                perimeter += 4
                # check top cell if exists
                if row > 0 and grid[row - 1][col] == 1:
                    # subtract 2 from perimeter if top cell is land
                    perimeter -= 2
                    # check left cell if exists
                if col > 0 and grid[row][col - 1] == 1:
                    # subtract 2 from perimeter if left cell is land
                    perimeter -= 2
    return perimeter  # return perimeter of the island
