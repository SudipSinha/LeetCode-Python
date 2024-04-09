"""Unique Paths

Link: https://leetcode.com/problems/unique-paths/

There is a robot on an `m × n` grid. The robot is initially located at the top-left corner (i.e., `grid[0][0]`). The robot tries to move to the bottom-right corner (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

Given the two integers `m` and `n`, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
"""

from math import comb


def uniquePaths_math(m: int, n: int) -> int:
    return comb(m + n - 2, m - 1)


def uniquePaths_dp(m: int, n: int) -> int:
    if m == 1:
        return 1
    elif n == 1:
        return 1
    return uniquePaths_dp(m - 1, n) + uniquePaths_dp(m, n - 1)
