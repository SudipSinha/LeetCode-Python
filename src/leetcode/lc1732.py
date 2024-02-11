"""Find the Highest Altitude

Link: https://leetcode.com/problems/find-the-highest-altitude/description/

There is a biker going on a road trip. The road trip consists of `n + 1` points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i and `i + 1` for all (`0 <= i < n`). Return the highest altitude of a point.
"""


class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        """Time complexity: O(n), Space complexity: O(1)."""
        cumsum__cur = 0
        cumsum__max = cumsum__cur
        for delta in gain:
            cumsum__cur += delta
            if cumsum__cur > cumsum__max:
                cumsum__max = cumsum__cur
        return cumsum__max
