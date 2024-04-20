"""Maximal Square

Link: https://leetcode.com/problems/maximal-square/

Given an `m × n` binary matrix filled with `0`'s and `1`'s, find the largest square containing only `1`'s and return its area.
"""
# mypy: ignore-errors

import numpy


def maximalSquare_naive(matrix: list[list[str]]) -> int:
    """Time complexity: O(n^3), space complexity: O(1)."""
    if not matrix:
        return 0
    matrix = numpy.array(matrix, int)
    (rows, cols) = matrix.shape
    side__max = 0
    for row in range(rows - side__max):
        for col in range(cols - side__max):
            while (
                matrix[row : row + side__max + 1, col : col + side__max + 1] == 1
            ).all():
                if row + side__max + 1 > rows or col + side__max + 1 > cols:
                    break
                side__max += 1
    return side__max * side__max


def maximalSquare_dp(matrix: list[list[str]]) -> int:
    """Idea: https://leetcode.com/problems/maximal-square/solutions/600149/python-thinking-process-diagrams-dp-approach
    Time complexity: O(n^2), space complexity: O(n^2).
    """
    if not matrix:
        return 0
    side__max = 0
    (rows, cols) = (len(matrix), len(matrix[0]))
    memo = [[0] * (cols + 1) for _ in range(rows + 1)]
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "1":
                memo[row + 1][col + 1] = 1 + min(
                    memo[row][col], memo[row + 1][col], memo[row][col + 1]
                )
                side__max = max(memo[row + 1][col + 1], side__max)
    return side__max * side__max
