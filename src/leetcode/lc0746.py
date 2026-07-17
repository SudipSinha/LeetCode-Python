"""Min Cost Climbing Stairs

Link: https://leetcode.com/problems/min-cost-climbing-stairs/

You are given an integer array `cost` where `cost[i]` is the cost of `i`th step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index `0`, or the step with index `1`.

Return the minimum cost to reach the top of the floor.
"""

from functools import cache
from sys import maxsize  # ∞


def minCostClimbingStairs_forward_cache(cost: list[int]) -> int:
    """Time complexity: O(n), space complexity: O(n)."""

    @cache
    def _cost(pos: int) -> int:
        """Minimum cost to reach the top of the stairs starting at position `i`."""
        if pos >= len(cost):
            return 0
        return cost[pos] + min(_cost(pos + 1), _cost(pos + 2))

    return min(_cost(0), _cost(1))


def minCostClimbingStairs_forward_array(cost: list[int]) -> int:
    """Time complexity: O(n), space complexity: O(n)."""
    cost__min = [maxsize] * (len(cost) + 2)

    def _cost(pos: int) -> int:
        nonlocal cost__min
        if cost__min[pos] != maxsize:
            return cost__min[pos]
        if pos >= len(cost):
            cost__min[pos] = 0
            return cost__min[pos]
        cost__min[pos] = cost[pos] + min(_cost(pos + 1), _cost(pos + 2))
        return cost__min[pos]

    return min(_cost(0), _cost(1))


def minCostClimbingStairs_backward_cache(cost: list[int]) -> int:
    """Time complexity: O(n), space complexity: O(n)."""

    @cache
    def _aux(pos: int) -> int:
        if pos <= 1:
            return 0
        return min(_aux(pos - 1) + cost[pos - 1], _aux(pos - 2) + cost[pos - 2])

    return _aux(len(cost))
