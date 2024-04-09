"""Equal Row and Column Pairs

Link: https://leetcode.com/problems/equal-row-and-column-pairs/

Given a `0`-indexed `n × n` integer matrix grid, return the number of pairs `(r_i, c_j)` such that row `r_i` and column `c_j` are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
"""

from collections import Counter


def equalPairs_naive(grid: list[list[int]]) -> int:
    """Slow. Time complexity: O(n^3), space complexity: O(1)."""
    n = len(grid)
    count = 0
    for row in range(n):
        for col in range(n):
            equal = True
            for pos in range(n):
                if grid[row][pos] != grid[pos][col]:
                    equal = False
                    break
            if equal:
                count += 1
    return count


def equalPairs_conjugate(grid: list[list[int]]) -> int:
    """Idea stolen from: https://leetcode.com/problems/equal-row-and-column-pairs/solutions/2328910/python3-3-lines-transpose-ctr-w-explanation-t-m-97-100
    Time complexity: O(n^3), space complexity: O(n^2).
    """
    conjugate = zip(*grid)
    count_grid = Counter(map(tuple, grid))
    count_conj = Counter(conjugate)
    return sum(count_conj[row] * count_grid[row] for row in count_conj)
