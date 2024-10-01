"""Combination Sum III

Link: https://leetcode.com/problems/combination-sum-iii/

Find all valid combinations of `k` numbers that sum up to n such that the following conditions are true:
*   Only numbers 1 through 9 are used.
*   Each number is used at most once.

Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
"""


def combinationSum3(k: int, n: int, m: int = 1) -> list[list[int]]:
    """Idea copied from https://leetcode.com/problems/combination-sum-iii/solutions/3924627/python3-recursive-beats-98-16/"""

    if m + k <= 10 and 10 - k >= m:
        minimum = sum(range(m, m + k))
        maximum = sum(range(10 - k, 10))
    else:
        return []

    #   Base cases.
    if k == 1 and n > m and n < 10:
        return [[n]]
    if n < minimum or n > maximum:
        return []
    elif n == minimum and m + k <= 10:  # Speed up
        return [list(range(m, m + k))]
    elif n == maximum and 10 - k > m:  # Speed up
        return [list(range(10 - k, 10))]

    output = []
    for i in range(m, 10):
        for ans in combinationSum3(k=k - 1, n=n - i, m=i + 1):
            output.append([i] + ans)
    return output
