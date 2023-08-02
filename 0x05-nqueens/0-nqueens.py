#!/usr/bin/python3
"""Solves the N queens puzzle challenge"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
except ValueError:
    print("N must be a number")
    sys.exit(1)


def resolve_matrix_for(queen, matrix, positions):
    """
    Resolves/removes reachable range of queen from the matrix then
    recursively resolves for subsequent possible queen positions
    for the next row.
    """
    positions.append(queen)

    for cell in matrix[:]:
        if any([cell == queen, cell[0] == queen[0], cell[1] == queen[1],
                cell[0] - cell[1] == queen[0] - queen[1],
                cell[0] + cell[1] == queen[0] + queen[1]]):
            matrix.pop(matrix.index(cell))

    # if end of the recursion
    if len(matrix) == 0:
        if len(positions) == N:
            print(positions)
        return

    # else recursively check for possible queen positions
    for possible_queen_pos in [cell for cell in matrix
                               if cell[0] == matrix[0][0]]:
        resolve_matrix_for(possible_queen_pos, matrix[:], positions[:])


for i in range(N):
    resolve_matrix_for([0, i], [[x, y] for x in range(N)
                       for y in range(N)], [])
