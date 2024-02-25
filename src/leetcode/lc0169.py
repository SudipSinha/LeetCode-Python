"""Majority Element

Link: https://leetcode.com/problems/majority-element/

Given an array `nums` of size `n`, return the majority element.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.
"""

from collections import defaultdict


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count: defaultdict[int, int] = defaultdict(int)
        for n in nums:
            count[n] += 1
        return max(count, key=count.get)  # type: ignore
