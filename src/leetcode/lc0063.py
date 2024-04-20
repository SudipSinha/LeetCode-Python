"""Unique Paths II

Link: https://leetcode.com/problems/unique-paths-ii/

You are given an `m × n` integer array grid. There is a robot initially located at the top-left corner (i.e., `grid[0][0]`). The robot tries to move to the bottom-right corner (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

An obstacle and space are marked as `1` or `0` respectively in `grid`. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
"""


def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
    """Time complexity: O(mn), space complexity: O(mn)."""
    (rows, cols) = (len(obstacleGrid), len(obstacleGrid[0]))
    paths = [[-1] * cols for _ in range(rows)]
    if obstacleGrid[0][0] == 1:
        return 0
    paths[0][0] = 1

    def uniquePaths_aux(row: int = rows - 1, col: int = cols - 1) -> int:
        nonlocal paths
        if paths[row][col] != -1:
            return paths[row][col]
        if obstacleGrid[row][col] == 1:
            paths[row][col] = 0
            return paths[row][col]
        if row == 0:
            paths[row][col] = uniquePaths_aux(row=row, col=col - 1)
            return paths[row][col]
        if col == 0:
            paths[row][col] = uniquePaths_aux(row=row - 1, col=col)
            return paths[row][col]
        paths[row][col] = uniquePaths_aux(row=row - 1, col=col) + uniquePaths_aux(
            row=row, col=col - 1
        )
        return paths[row][col]

    return uniquePaths_aux()
