"""Longest Subarray of 1's After Deleting One Element

Given a binary array `nums`, you should delete `k` elements from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
"""


class Solution:
    def longestSubarray_sw(self, nums: list[int], k: int = 1) -> int:
        """Sliding window approach.
        Time complexity: O(n), Space complexity: O(1).
        """

        if not nums:
            return 0
        if len(nums) < k:
            return sum(nums)

        left = 0
        right = 0
        zeros = 0
        ones_max = 0

        for right in range(len(nums)):
            zeros += 1 - nums[right]
            print(f"Update:({left}, {right}): zeros={zeros}")
            while zeros > k:
                zeros -= 1 - nums[left]
                left += 1
            ones_cur = right - left - zeros + 1
            if ones_cur > ones_max:
                ones_max = ones_cur

        return ones_max if ones_max != len(nums) else ones_max - 1

    def longestSubarray_alt(self, nums: list[int], k: int = 1) -> int:
        """Time complexity: O(n), Space complexity: O(n)."""

        if not nums:
            return 0
        if len(nums) < k:
            return sum(nums)

        ones_until_zero = []  # Ones between the last 0 and current 0.
        ones_cur = 0

        for num in nums:
            ones_cur += num
            if num == 0:
                ones_until_zero.append(ones_cur)
                ones_cur = 0
        if nums[-1] == 1:  # Add the last index no matter what.
            ones_until_zero.append(ones_cur)

        if len(ones_until_zero) == 1:
            # Length can be 1 if there are no zeros or if the last element is zero.
            if nums[-1] == 0:
                return sum(ones_until_zero) - k + 1
            else:
                return sum(ones_until_zero) - k

        sum__cur = sum(ones_until_zero[0 : k + 1])
        sum__max = sum__cur
        for i in range(1, len(ones_until_zero) - k):
            sum__cur = sum__cur - ones_until_zero[i - 1] + ones_until_zero[i + 1]
            if sum__cur > sum__max:
                sum__max = sum__cur
        return sum__max


print(Solution().longestSubarray_sw([1, 1, 0, 0, 1, 1, 1, 0, 1]))
# print(Solution().longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))
# print(Solution().longestSubarray([1, 0, 1, 0]))
