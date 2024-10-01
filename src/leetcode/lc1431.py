"""Kids With the Greatest Number of Candies

Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

There are `n` kids with candies. You are given an integer array `candies`, where each `candies[i]` represents the number of candies the `i`th kid has, and an integer `extraCandies`, denoting the number of extra candies that you have.

Return a boolean array `result` of length `n`, where `result[i]` is `true` if, after giving the `i`th kid all the `extraCandies`, they will have the greatest number of candies among all the kids, or `false` otherwise.

Note that multiple kids can have the greatest number of candies.
"""


def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    """Time complexity: O(n), space complexity: O(1)."""
    candies__max = max(candies)
    required__min = candies__max - extraCandies
    return [c >= required__min for c in candies]
