"""Valid Sudoku

Link: https://leetcode.com/problems/valid-sudoku/description/

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
"""

# mypy: ignore-errors
import numpy


class Solution:
    @staticmethod
    def _has_unique_elements(obj) -> bool:
        _, counts = numpy.unique(obj, return_counts=True)
        return (counts[1:] <= 1).flatten().all()

    def isValidSudoku_naive(self, board: list[list[str]]) -> bool:
        """Time complexity: O(n^2), space complexity: O(n), where size of the board = n × n"""
        board_np = numpy.array(board)
        valid_cols = numpy.apply_along_axis(
            func1d=Solution._has_unique_elements, axis=0, arr=board_np
        )
        valid_rows = numpy.apply_along_axis(
            func1d=Solution._has_unique_elements, axis=1, arr=board_np
        )
        valid_blocks = numpy.full((3, 3), False)
        for i in range(3):
            for j in range(3):
                # print(board_np[3* i: 3*i+3, j: j+3])
                valid_blocks[i, j] = Solution._has_unique_elements(
                    board_np[3 * i : 3 * i + 3, 3 * j : 3 * j + 3]
                )
        return valid_rows.all() and valid_cols.all() and valid_blocks.all()

    def isValidSudoku_clever(self, board: list[list[str]]) -> bool:
        """Solution from https://leetcode.com/problems/valid-sudoku/solutions/3277043/beats-96-78-short-7-line-python-solution-with-detailed-explanation"""
        res = []
        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x != ".":
                    res += [(i, x), (x, j), (i // 3, j // 3, x)]
        return len(res) == len(set(res))


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(Solution().isValidSudoku_clever(board=board))
