"""Subsets

Link: https://leetcode.com/problems/subsets/

Given an integer array `nums` of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""


def subsets(nums: set[int]) -> set[frozenset[int]]:
    nums_list = list(nums)
    subsets: set[frozenset[int]] = set()
    subset__cur: list[int] = list()

    def _dfs(index: int):
        nonlocal subsets
        nonlocal subset__cur
        if index == len(nums_list):
            subsets.add(frozenset(subset__cur))
            return
        #   Branch for adding indexed element.
        subset__cur.append(nums_list[index])
        _dfs(index=index + 1)
        # Branch for ignoring indexed element.
        subset__cur.pop()
        _dfs(index=index + 1)

    _dfs(index=0)
    return subsets
