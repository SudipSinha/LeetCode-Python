"""Container With Most Water

Link: https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""


class Solution:
    def maxArea_naive(self, height: list[int]) -> int:
        """Time complexity: O(n^2), space complexity: O(1)."""
        area__max = 0
        for left in range(len(height)):
            for right in range(len(height) - 1, left, -1):
                area__cur = min([height[left], height[right]]) * (right - left)
                if area__cur > area__max:
                    area__max = area__cur
        return area__max

    def maxArea_2ptr(self, height: list[int]) -> int:
        """Two pointer approach. We always move the limiting side.
        Time complexity: O(n^2), space complexity: O(1).
        """
        left = 0
        right = len(height) - 1
        area__cur = min([height[left], height[right]]) * (right - left)
        area__max = area__cur

        while left < right:
            if height[left] < height[right]:  # Left is bottleneck.
                left += 1
            else:
                right -= 1
            area__cur = min([height[left], height[right]]) * (right - left)
            if area__cur > area__max:
                area__max = area__cur

        return area__max
