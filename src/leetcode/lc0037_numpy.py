"""Sudoku Solver

Link: https://leetcode.com/problems/sudoku-solver/description/

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.
"""

import numpy

board_empty = [["."] * 9] * 9


class Solution:
    grid: numpy.ndarray

    def __init__(self, board: list[list[str]] = board_empty) -> None:
        self.grid = numpy.array(board)

    def _fill_grid(self, board: list[list[str]]) -> None:
        for row in range(9):
            for col in range(9):
                self.grid[row, col] = board[row][col]

    def _valid_insertion(self, value: str, row: int, col: int) -> bool:
        not_in_row = value not in self.grid[row, :]
        not_in_column = value not in self.grid[:, col]
        not_in_box = (
            value
            not in self.grid[
                row // 3 * 3 : row // 3 * 3 + 3, col // 3 * 3 : col // 3 * 3 + 3
            ]
        )
        return not_in_row and not_in_column and not_in_box

    def _solve_backtracking(self, row: int = 0, col: int = 0) -> bool:
        if row == 9:  # Done.
            return True
        elif col == 9:  # Wrap around.
            return self._solve_backtracking(row=row + 1, col=0)
        elif self.grid[row, col] != ".":  # Fixed cell; move on.
            return self._solve_backtracking(row=row, col=col + 1)
        else:
            for i in map(str, range(1, 10)):
                if self._valid_insertion(value=i, row=row, col=col):
                    self.grid[row, col] = i
                    if self._solve_backtracking(row=row, col=col + 1):
                        return True
                    else:
                        self.grid[row, col] = "."
            return False

    def solveSudoku(self, board: list[list[str]], row: int = 0, col: int = 0) -> None:
        """
        Do not return anything, modify board in-place instead.

        Solution idea from: https://gist.github.com/syphh/62e6140361feb2d7196f2cb050c987b3

        Time complexity: ?
        """

        if (self.grid == ".").all():
            self._fill_grid(board=board)

        self._solve_backtracking(row=0, col=0)

        for row in range(9):
            for col in range(9):
                board[row][col] = self.grid[row, col]
