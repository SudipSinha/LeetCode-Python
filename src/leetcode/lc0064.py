"""Minimum Path Sum

Link: https://leetcode.com/problems/minimum-path-sum/

Given a `m × n` grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

from functools import cache


def minPathSum(grid: list[list[int]]) -> int:
    """Time complexity: O(mn), space complexity: O(mn)."""
    infinity = sum(sum(num for num in row) for row in grid) + 1
    (rows, cols) = (len(grid), len(grid[0]))

    @cache
    def minPathSum_aux(row: int = 0, col: int = 0) -> int:
        if row == rows - 1 and col == cols - 1:
            return grid[-1][-1]
        if row >= rows or col >= cols:
            return infinity
        sum_right = minPathSum_aux(row=row, col=col + 1)
        sum_down = minPathSum_aux(row=row + 1, col=col)
        return grid[row][col] + min(sum_right, sum_down)

    return minPathSum_aux()
