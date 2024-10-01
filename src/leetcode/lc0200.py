"""Number of Islands

Link: https://leetcode.com/problems/number-of-islands/

Given an `m x n` 2D binary grid grid which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""

from collections import deque
from typing import Literal

directions = {(-1, 0), (0, -1), (1, 0), (0, 1)}  # Up, left, down, right.


def _mark_visited_dfs_recursive(grid, row: int, col: int, islands: int = 0):
    """Depth-first search method to marks the visited nodes.
    Visited nodes are marked with `In`, where `n` is the island number.
    """
    if not (0 <= row < len(grid) and 0 <= col < len(grid[0])) or grid[row][col] != "1":
        return

    grid[row][col] = "I" + str(islands)  # Mark visited.
    for δ_row, δ_col in directions:
        _mark_visited_dfs_recursive(grid, row + δ_row, col + δ_col, islands)

    return


def _mark_visited_dfs_iterative(grid, row: int, col: int, islands: int = 0):
    """Depth-first search method to marks the visited nodes.
    Visited nodes are marked with `In`, where `n` is the island number.
    """
    if not (0 <= row < len(grid) and 0 <= col < len(grid[0])) or grid[row][col] != "1":
        return

    stack = []
    stack.append((row, col))
    grid[row][col] = "I" + str(islands)  # Mark visited.

    while stack:
        (row, col) = stack.pop()
        for δ_row, δ_col in directions:
            if (
                0 <= row + δ_row < len(grid)
                and 0 <= col + δ_col < len(grid[0])
                and grid[row + δ_row][col + δ_col] == "1"
            ):
                stack.append((row + δ_row, col + δ_col))
                grid[row + δ_row][col + δ_col] = "I" + str(islands)  # Visited.

    return


def _mark_visited_bfs(grid, row: int, col: int, islands: int = 0):
    """Breadth-first search method to marks the visited nodes.
    Visited nodes are marked with `In`, where `n` is the island number.
    """
    if not (0 <= row < len(grid) and 0 <= col < len(grid[0])) or grid[row][col] != "1":
        return

    queue: deque[tuple[int, int]] = deque()
    queue.append((row, col))
    grid[row][col] = "I" + str(islands)  # Visited.

    while queue:
        (row, col) = queue.popleft()
        for δ_row, δ_col in directions:
            if (
                0 <= row + δ_row < len(grid)
                and 0 <= col + δ_col < len(grid[0])
                and grid[row + δ_row][col + δ_col] == "1"
            ):
                queue.append((row + δ_row, col + δ_col))
                grid[row + δ_row][col + δ_col] = "I" + str(islands)  # Visited.

    return


def numIslands(grid: list[list[str]], method: Literal["DFS", "BFS"] = "DFS") -> int:
    if not grid:
        return 0
    rows = len(grid)
    if rows == 0:
        return 0
    cols = len(grid[0])
    if cols == 0:
        return 0

    strategy = {
        "DFS": _mark_visited_dfs_iterative,
        "BFS": _mark_visited_bfs,
    }
    islands = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1":
                islands += 1
                strategy[method](grid=grid, row=row, col=col, islands=islands)

    return islands
