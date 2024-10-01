"""Majority Element

Link: https://leetcode.com/problems/majority-element/

Given an array `nums` of size `n`, return the majority element.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.
"""

from collections import Counter, defaultdict


def majorityElement_hashmap(nums: list[int]) -> int | None:
    """Time complexity: O(len(nums)), space complexity: O(nunique(nums))."""
    if not nums:
        return None
    count: defaultdict[int, int] = defaultdict(int)
    for n in nums:
        count[n] += 1
    return max(count, key=count.get)  # type: ignore


def majorityElement_counter(nums: list[int]) -> int | None:
    """Time complexity: O(len(nums)), space complexity: O(nunique(nums))."""
    return Counter(nums).most_common(1)[0][0] if nums else None


def majorityElement_Boyer_Moore(nums: list[int]) -> int | None:
    """Boyer–Moore majority vote algorithm.
    Link: https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
    Time complexity: O(len(nums)), space complexity: O(1).
    """
    if not nums:
        return None
    count = 0
    candidate = None
    for n in nums:
        if count == 0:
            candidate = n
        if n == candidate:
            count += 1
        else:
            count -= 1
    return candidate
