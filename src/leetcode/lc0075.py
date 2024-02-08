class Solution:
    def moveZeroes_2ptr_replacement(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Two pointer technique with replacement with zeros.
        Time complexity: O(n), Space complexity: O(1).
        """

        pos_nonzero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos_nonzero] = nums[i]
                pos_nonzero += 1
            if i != pos_nonzero - 1:
                nums[i] = 0

    def moveZeroes_2ptr_swap(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Two pointer technique with swapping.
        Time complexity: O(n), Space complexity: O(1).
        """

        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # Wait to find a non-zero element to swap.
            if nums[slow] != 0:
                slow += 1
