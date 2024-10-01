"""Trapping Rain Water

Link: https://leetcode.com/problems/trapping-rain-water/

Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""


def trap_arrays(height: list[int]) -> int:
    """Time complexity: O(n), space complexity: O(n)."""
    max_left = [0] * len(height)
    max_right = [0] * len(height)
    for i in range(1, len(height)):
        max_left[i] = max(max_left[i - 1], height[i - 1])
    for i in range(len(height) - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], height[i + 1])
    capacity = [
        max(0, min(max_left[i], max_right[i]) - height[i]) for i in range(len(height))
    ]
    return sum(capacity)


def trap_2ptr(height: list[int]) -> int:
    """Hint: [NeetCode](https://www.youtube.com/watch?v=ZI2z5pq0TqA).
    Time complexity: O(n), space complexity: O(1).
    """
    if not height:
        return 0
    capacity = 0
    (left, right) = 0, len(height) - 1
    (max_left, max_right) = (height[left], height[right])
    while left < right:
        if max_left <= max_right:
            left += 1
            max_left = max(max_left, height[left])
            capacity += max_left - height[left]
        else:
            right -= 1
            max_right = max(max_right, height[right])
            capacity += max_right - height[right]
    return capacity
