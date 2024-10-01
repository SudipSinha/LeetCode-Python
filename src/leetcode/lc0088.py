"""Merge Sorted Array

Link: https://leetcode.com/problems/merge-sorted-array/

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first m elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.
"""


def merge_copy(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """Time complexity: O(m + n), space complexity: O(m + n)."""
    if not nums1 or not nums2:
        return
    merged = [0] * len(nums1)
    ptr1 = 0
    ptr2 = 0
    while ptr1 + ptr2 < m + n:
        if ptr2 == n or ptr1 < m and nums1[ptr1] <= nums2[ptr2]:
            merged[ptr1 + ptr2] = nums1[ptr1]
            ptr1 += 1
        else:
            merged[ptr1 + ptr2] = nums2[ptr2]
            ptr2 += 1
    for i in range(len(nums1)):
        nums1[i] = merged[i]


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """Time complexity: O(m + n), space complexity: O(1)."""
    while n > 0:
        if nums2[n - 1] >= nums1[m - 1]:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
        else:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
