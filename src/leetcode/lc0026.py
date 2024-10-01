"""Remove Duplicates from Sorted Array

Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates *in-place* such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

Consider the number of unique elements of `nums` to be `k`, to get accepted, you need to do the following things:
*   Change the array nums such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially. The remaining elements of `nums` are not important as well as the size of `nums`.
*   Return `k`.
"""


def removeDuplicates(nums: list[int]) -> int:
    """Time complexity: O(n), space complexity: O(1)."""
    if not nums:
        return 0
    left = 0
    n_unique = 1
    for right in range(1, len(nums)):
        if nums[right] != nums[left]:
            left += 1
            nums[left] = nums[right]
            n_unique += 1
    return n_unique
