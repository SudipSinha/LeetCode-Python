"""Max Consecutive Ones III

Link: https://leetcode.com/problems/max-consecutive-ones-iii/

Given a binary array `nums` and an integer `k`, return the maximum number of consecutive `1`'s in the array if you can flip at most `k` `0`'s.
"""


class Solution:
    def longestOnes_sw(self, nums: list[int], k: int) -> int:
        """Sliding window approach.
        Time complexity: O(n), space complexity: O(1).
        """

        left = 0
        right = 0
        zeros = 0
        subarray_len__max = 0

        for right in range(len(nums)):
            zeros += 1 - nums[right]
            while zeros > k:
                zeros -= 1 - nums[left]
                left += 1
            subarray_len = right - left + 1
            if subarray_len > subarray_len__max:
                subarray_len__max = subarray_len

        return subarray_len__max
