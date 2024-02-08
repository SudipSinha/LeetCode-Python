"""Longest Subarray of 1's After Deleting One Element

Given a binary array `nums`, you should delete `k` elements from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
"""



class Solution:
    def longestSubarray(self, nums: list[int], k: int = 1) -> int:
        if not nums:
            return 0
        if len(nums) < k:
            return sum(nums)

        idxs_zero = []  # Indexes of 0s.
        ones_loc = []  # Ones from last 0 to this 0.
        ones_cur = 0

        for i in range(len(nums) - 1):
            ones_cur += nums[i]

            if nums[i] == 0:
                idxs_zero.append(i)
                ones_loc.append(ones_cur)
                ones_cur = 0

        # Add the last index no matter what.
        idxs_zero.append(len(nums) - 1)
        ones_loc.append(ones_cur + nums[-1])

        if len(idxs_zero) == 1:
            # Length can be 1 if there are no zeros or if the last element is zero.
            if nums[-1] == 0:
                return sum(ones_loc) - k + 1
            else:
                return sum(ones_loc) - k
        
        sum__cur = sum(ones_loc[0:k + 1])
        sum__max = sum__cur
        for i in range(1, len(ones_loc) - k):
            sum__cur = sum__cur - ones_loc[i - 1] + ones_loc[i + 1]
            if sum__cur > sum__max:
                sum__max = sum__cur
        return sum__max



print(Solution().longestSubarray([1, 0]))
# print(Solution().longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))
# print(Solution().longestSubarray([1, 0, 1, 0]))
