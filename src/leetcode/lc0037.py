"""Sudoku Solver

Link: https://leetcode.com/problems/sudoku-solver/description/

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.
"""

board_empty = [["."] * 9] * 9


class Solution:
    board: list[list[str]]

    def __init__(self, board: list[list[str]] = board_empty) -> None:
        self.board = board

    def _valid_insertion(self, value: str, row: int, col: int) -> bool:
        not_in_row = value not in self.board[row]
        not_in_column = value not in [self.board[row][col] for row in range(9)]
        not_in_box = value not in [
            self.board[r][c]
            for r in range(row // 3 * 3, row // 3 * 3 + 3)
            for c in range(col // 3 * 3, col // 3 * 3 + 3)
        ]
        return not_in_row and not_in_column and not_in_box

    def _solve_backtracking(self, row: int = 0, col: int = 0) -> bool:
        if row == 9:  # Done.
            return True
        elif col == 9:  # Wrap around.
            return self._solve_backtracking(row=row + 1, col=0)
        elif self.board[row][col] != ".":  # Fixed cell; move on.
            return self._solve_backtracking(row=row, col=col + 1)
        else:
            for i in map(str, range(1, 10)):
                if self._valid_insertion(value=i, row=row, col=col):
                    self.board[row][col] = i
                    if self._solve_backtracking(row=row, col=col + 1):
                        return True
                    else:
                        self.board[row][col] = "."
            return False

    def solveSudoku(self, board: list[list[str]], row: int = 0, col: int = 0) -> None:
        """
        Do not return anything, modify board in-place instead.

        Solution idea from: https://gist.github.com/syphh/62e6140361feb2d7196f2cb050c987b3

        Time complexity: ?
        """
        self.board = board
        self._solve_backtracking(row=0, col=0)
