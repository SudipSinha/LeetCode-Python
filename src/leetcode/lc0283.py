"""Move Zeroes

Link: https://leetcode.com/problems/move-zeroes/

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""


def moveZeroes_2ptr_replacement(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    Two pointer technique with replacement with zeros.
    Time complexity: O(n), space complexity: O(1).
    """

    pos_nonzero = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos_nonzero] = nums[i]
            pos_nonzero += 1
        if i != pos_nonzero - 1:
            nums[i] = 0


def moveZeroes_2ptr_swap(nums: list) -> None:
    """
    Do not return anything, modify nums in-place instead.
    Two pointer technique with swapping.
    Time complexity: O(n), space complexity: O(1).
    """

    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0 and nums[slow] == 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]

        # Wait to find a non-zero element to swap.
        if nums[slow] != 0:
            slow += 1
