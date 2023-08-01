#!/usr/bin/python3
"""
Module for 0x0C. N Queens.
Holberton School
Specializations - Interview Preparation ― Algorithms
"""
from sys import argv, exit


def solveNQueens(n):
    """Program that solves the N queens problem"""
    res = []
    queens = [-1] * n
    # queens is a one-dimension array, like [1, 3, 0, 2] means
    # index represents row no and value represents col no

    def dfs(index):
        """Recursively resolves the N queens problem"""
        if index == len(queens):  # n queens have been placed correctly
            res.append(queens[:])
            return  # backtracking
        for i in range(len(queens)):
            queens[index] = i
            if valid(index):  # pruning
                dfs(index + 1)

    # check whether nth queens can be placed
    def valid(n):
        """Method that checks if a position in the board is valid"""
        for i in range(n):
            if abs(queens[i] - queens[n]) == n - i:  # same diagonal
                return False
            if queens[i] == queens[n]:  # same column
                return False
        return True

    # given queens = [1,3,0,2] this function returns
    # [[0, 1], [1, 3], [2, 0], [3, 2]]

    def make_all_boards(res):
        """Method that builts the List that be returned"""
        actual_boards = []
        for queens in res:
            board = []
            for row, col in enumerate(queens):
                board.append([row, col])
            actual_boards.append(board)
        return actual_boards

    dfs(0)
    return make_all_boards(res)


if __name__ == "__main__":
    if len(argv) < 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        n = int(argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)
    else:
        result = solveNQueens(n)
        for row in result:
            print(row)
