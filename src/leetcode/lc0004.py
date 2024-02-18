"""Median of Two Sorted Arrays

Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.
"""


class Solution:
    def findMedianSortedArrays_naive(self, nums1: list[int], nums2: list[int]) -> float:
        """Time complexity: O((m + n) log(m + n)), space complexity: O(m + n)."""
        merged = sorted(nums1 + nums2)
        n = len(merged)
        if n % 2 == 1:
            return merged[(n - 1) // 2]
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2
