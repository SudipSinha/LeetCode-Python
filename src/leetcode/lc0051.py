"""N-Queens

Link: https://leetcode.com/problems/n-queens/

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
"""

import numpy
from numpy.typing import NDArray

CHAR_QUEEN = "Q"
CHAR_BLANK = "."


class Solution:
    def __init__(self) -> None:
        self.solutions: list[list[str]] = []

    @staticmethod
    def _format_solution(solution: NDArray) -> list[str]:
        """Return a list version of the 2D array."""
        return numpy.apply_along_axis(
            func1d=lambda row: "".join(row), axis=0, arr=solution
        ).tolist()  # type: ignore

    @staticmethod
    def _valid(n: int, board: NDArray, row: int, col: int) -> bool:
        """Check validity of inserting a queen at (`row`, `col`) of `board`."""
        valid_row = CHAR_QUEEN not in board[row, :]
        valid_col = CHAR_QUEEN not in board[:, col]
        valid_diag_major = CHAR_QUEEN not in [
            board[row + i, col + i]
            for i in range(-n + 1, n)
            if row + i in range(n) and col + i in range(n)
        ]
        valid_diag_minor = CHAR_QUEEN not in [
            board[row - i, col + i]
            for i in range(-n + 1, n)
            if row - i in range(n) and col + i in range(n)
        ]
        return valid_row and valid_col and valid_diag_major and valid_diag_minor

    def _solve(
        self,
        n: int,
        board: NDArray,
        queens_placed: int,
        search_rows: list[int],
        search_cols: list[int],
    ) -> None:
        """Auxillary method for solving using backtracking.
        Time complexity: O(n!), space complexity: O(n)."""

        if not search_rows or not search_cols:  # Base case.
            if queens_placed == n:  # Success.
                self.solutions.append(Solution._format_solution(board))
            return

        row = search_rows[0]
        for col in search_cols:
            if Solution._valid(n=n, board=board, row=row, col=col):
                #   Add queen.
                board[row, col] = CHAR_QUEEN
                queens_placed += 1
                #   Solve.
                self._solve(
                    n=n,
                    board=board,
                    queens_placed=queens_placed,
                    search_rows=[r for r in search_rows if r != row],
                    search_cols=[c for c in search_cols if c != col],
                )
                #   Remove queen.
                board[row, col] = CHAR_BLANK
                queens_placed -= 1

    def solveNQueens(self, n: int) -> list[list[str]]:
        self._solve(
            n=n,
            board=numpy.full(shape=(n, n), fill_value=CHAR_BLANK),
            queens_placed=0,
            search_rows=list(range(n)),
            search_cols=list(range(n)),
        )
        return self.solutions
