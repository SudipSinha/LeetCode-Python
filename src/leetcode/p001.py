class Solution:
    def twoSum_naive(self, nums: list[int], target: int) -> set[int]:
        """Time complexity: O(n^2), Space complexity: O(1)."""
        for i in range(len(nums) - 1):
            complement = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == complement:
                    return {i, j}
        return set()

    def twoSum_hashmap_2pass(self, nums: list[int], target: int) -> set[int]:
        """Time complexity: O(n), Space complexity: O(n)."""
        hashmap = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return {i, hashmap[complement]}
        return set()

    def twoSum_hashmap_1pass(self, nums: list[int], target: int) -> set[int]:
        """Time complexity: O(n), Space complexity: O(n)."""
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return {i, hashmap[complement]}
            hashmap[nums[i]] = i
        return set()
