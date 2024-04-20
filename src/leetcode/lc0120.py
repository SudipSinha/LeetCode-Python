"""Triangle

Link: https://leetcode.com/problems/triangle/

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index `i` on the current row, you may move to either index `i` or index `i + 1` on the next row.
"""

from copy import deepcopy
from functools import cache


def minimumTotal_recur_inner(triangle: list[list[int]]) -> int:
    """Time complexity: O(n), space complexity: O(n)."""

    @cache
    def path_sum__min(row: int = 0, col: int = 0) -> int:
        if row == len(triangle) - 1:
            return triangle[row][col]
        return triangle[row][col] + min(
            path_sum__min(row=row + 1, col=col), path_sum__min(row=row + 1, col=col + 1)
        )

    return path_sum__min()


@cache
def minimumTotal_recur_1fn(
    triangle: tuple[tuple[int]], row: int = 0, col: int = 0
) -> int:
    """Time complexity: O(n), space complexity: O(n)."""
    if row == len(triangle) - 1:
        return triangle[row][col]
    return triangle[row][col] + min(
        minimumTotal_recur_1fn(triangle=triangle, row=row + 1, col=col),
        minimumTotal_recur_1fn(triangle=triangle, row=row + 1, col=col + 1),
    )


def minimumTotal_iter(triangle: list[list[int]]) -> int:
    """Time complexity: O(n), space complexity: O(n).
    Space complexity can be reduced to O(1) by modifying `triangle` in-place.
    """
    path_sum__min = deepcopy(triangle)
    for i in range(len(triangle) - 2, -1, -1):
        for j, _ in enumerate(path_sum__min[i]):
            path_sum__min[i][j] += min(
                path_sum__min[i + 1][j], path_sum__min[i + 1][j + 1]
            )

    return path_sum__min[0][0]
