"""Longest Increasing Subsequence

Link: https://leetcode.com/problems/longest-increasing-subsequence/

Given an integer array `nums`, return the length of the longest strictly increasing subsequence.
"""

from typing import TypedDict


class LIS(TypedDict):
    length: int
    subseq: list[int]


def argmax(nums: list[int], candidates: list[int] | None = None) -> int:
    """Returns the index with maximum value within the index subset `candidates`."""
    if not candidates:
        candidates = list(range(len(nums)))
    return max(
        range(len(nums)), key=lambda index: nums[index] if index in candidates else -1
    )


#   TODO: O(n⋅log(n)) solution.
def lengthOfLIS_dp(nums: list[int]) -> LIS:
    """Dynamic programming solution.
    Idea: https://cp-algorithms.com/sequences/longest_increasing_subsequence.html
    Recurrence relation: LIS(k) = max{1, 1 + max_{j < k, v_j < v_k} {LIS(j)}}.
    Time complexity: O(n^2), space complexity: O(n^2).
    The space complexity can be reduced to O(n) if the LIS is not required.
    It can also be reduced by using backtracking to get the LIS.
    """
    lengths = [1] * len(nums)
    subseqs: list[list[int]] = [[] for _ in range(len(nums))]
    subseqs[0] = [nums[0]]
    for i in range(1, len(nums)):
        #   If the subseq is not required, just use the following line.
        # len_lis[i] = max((len_lis[j] + 1 for j in range(i) if nums[j] < nums[i]), default=1)
        candidates = []
        for j in range(i):
            if nums[j] < nums[i]:
                candidates.append(j)
        if candidates:
            index_max = argmax(lengths, candidates)
            lengths[i] = lengths[index_max] + 1
            subseqs[i] = subseqs[index_max] + [nums[i]]
        else:
            lengths[i] = 1
            subseqs[i] = [nums[i]]
    index__max = argmax(lengths)
    return {
        "length": lengths[index__max],
        "subseq": subseqs[index__max],
    }
