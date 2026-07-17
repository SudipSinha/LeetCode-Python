"""Minimum Path Sum

Link: https://leetcode.com/problems/minimum-path-sum/

Given a `m × n` grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

from functools import cache
from sys import maxsize  # ∞


def minPathSum_forward(grid: list[list[int]]) -> int:
    """Time complexity: O(mn), space complexity: O(mn)."""
    (rows, cols) = (len(grid), len(grid[0]))

    @cache
    def _aux(row: int = 0, col: int = 0) -> int:
        if row == rows - 1 and col == cols - 1:
            return grid[-1][-1]
        if row >= rows or col >= cols:
            return maxsize
        sum_right = _aux(row=row, col=col + 1)
        sum_down = _aux(row=row + 1, col=col)
        return grid[row][col] + min(sum_right, sum_down)

    return _aux()


def minPathSum_backward(grid: list[list[int]]) -> int:
    """Time complexity: O(mn), space complexity: O(mn)."""
    (rows, cols) = (len(grid), len(grid[0]))

    @cache
    def _aux(row: int, col: int) -> int:
        if row < 0 or col < 0:
            return maxsize
        if row == 0 and col == 0:
            return grid[0][0]
        sum_up = _aux(row=row, col=col - 1)
        sum_left = _aux(row=row - 1, col=col)
        return grid[row][col] + min(sum_up, sum_left)

    return _aux(rows - 1, cols - 1)
