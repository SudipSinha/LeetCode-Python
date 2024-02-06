"""Maximum Average Subarray I
You are given an integer array nums consisting of `n` elements, and an integer `k`.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 1e-5 will be accepted.
"""

from math import inf


class Solution:
    def findMaxAverage_naive(self, nums: list[int], k: int) -> float:
        """Time complexity: O(nk), Space complexity: O(n)"""
        sum__max = -inf
        for i in range(len(nums) - k + 1):
            sum__cur = sum(nums[i : i + k])
            if sum__cur > sum__max:
                sum__max = sum__cur
        return sum__max / k


    def findMaxAverage_smart(self, nums: list[int], k: int) -> float:
        """Update the sum intelligently.
        Time complexity: O(n), Space complexity: O(n).
        """
        sum__cur = sum(nums[0 : k])
        sum__max = sum__cur
        for i in range(1, len(nums) - k + 1):
            sum__cur = sum__cur - nums[i - 1] + nums[i + k - 1]
            if sum__cur > sum__max:
                sum__max = sum__cur
        return sum__max / k
