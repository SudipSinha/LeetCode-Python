"""Valid Sudoku

Link: https://leetcode.com/problems/valid-sudoku/

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
"""

# mypy: ignore-errors
import numpy


def _has_unique_elements(obj) -> bool:
    _, counts = numpy.unique(obj, return_counts=True)
    return (counts[1:] <= 1).flatten().all()


def isValidSudoku_naive(board: list[list[str]]) -> bool:
    """Time complexity: O(n^2), space complexity: O(n), where size of the board = n × n"""
    board_np = numpy.array(board)
    valid_cols = numpy.apply_along_axis(
        func1d=_has_unique_elements, axis=0, arr=board_np
    )
    valid_rows = numpy.apply_along_axis(
        func1d=_has_unique_elements, axis=1, arr=board_np
    )
    valid_blocks = numpy.full((3, 3), False)
    for i in range(3):
        for j in range(3):
            valid_blocks[i, j] = _has_unique_elements(
                board_np[3 * i : 3 * i + 3, 3 * j : 3 * j + 3]
            )
    return valid_rows.all() and valid_cols.all() and valid_blocks.all()


def isValidSudoku_clever(board: list[list[str]]) -> bool:
    """Solution from https://leetcode.com/problems/valid-sudoku/solutions/3277043/beats-96-78-short-7-line-python-solution-with-detailed-explanation"""
    res = []
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if x != ".":
                res += [(i, x), (x, j), (i // 3, j // 3, x)]
    return len(res) == len(set(res))
