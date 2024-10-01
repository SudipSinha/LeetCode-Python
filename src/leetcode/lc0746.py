"""Min Cost Climbing Stairs

Link: https://leetcode.com/problems/min-cost-climbing-stairs/

You are given an integer array `cost` where `cost[i]` is the cost of `i`th step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index `0`, or the step with index `1`.

Return the minimum cost to reach the top of the floor.
"""

from functools import cache


def minCostClimbingStairs_cache(cost: list[int]) -> int:
    """Time complexity: O(n), space complexity: O(n)."""

    @cache
    def _cost(pos: int) -> int:
        if pos >= len(cost):
            return 0
        return cost[pos] + min(_cost(pos + 1), _cost(pos + 2))

    return min(_cost(0), _cost(1))


def minCostClimbingStairs_array(cost: list[int]) -> int:
    """Time complexity: O(n), space complexity: O(n)."""
    infinity = sum(cost) + 1
    cost__min = [infinity] * (len(cost) + 2)

    def _cost(pos: int) -> int:
        nonlocal cost__min
        if cost__min[pos] != infinity:
            return cost__min[pos]
        if pos >= len(cost):
            cost__min[pos] = 0
            return cost__min[pos]
        cost__min[pos] = cost[pos] + min(_cost(pos + 1), _cost(pos + 2))
        return cost__min[pos]

    return min(_cost(0), _cost(1))
