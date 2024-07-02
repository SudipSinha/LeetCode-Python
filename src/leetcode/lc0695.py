"""Max Area of Island

Link: https://leetcode.com/problems/max-area-of-island/

You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value `1` in the island.

Return the maximum area of an island in grid. If there is no island, return `0`.
"""

directions = {(-1, 0), (0, -1), (1, 0), (0, 1)}  # Up, left, down, right.


def _search(grid: list[list[int]], row: int = 0, col: int = 0) -> int:
    rows = len(grid)
    cols = len(grid[0])
    if row < 0 or row > rows - 1 or col < 0 or col > cols - 1:
        return 0  # Out of range.
    if grid[row][col] == 0 or grid[row][col] == -1:
        return 0  # No island or visited.
    grid[row][col] = -1  # Mark visited.
    options = [_search(grid, row + δ_row, col + δ_col) for (δ_row, δ_col) in directions]
    return 1 + sum(options)


def maxAreaOfIsland(grid: list[list[int]]) -> int:
    """Time complexity: O(n^2), space complexity: O(n^2)."""
    if not grid:
        return 0
    rows = len(grid)
    cols = len(grid[0])

    size__max = 0
    for row in range(rows):
        for col in range(cols):
            size__cur = _search(grid, row, col)
            size__max = max(size__cur, size__max)

    return size__max
