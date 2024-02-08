"""Is Subsequence

Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """Time complexity: O(mn), Space complexity: O(1)."""
        idx = 0
        for char in s:
            while idx < len(t) and char != t[idx]:
                idx += 1
            idx += 1
            if idx > len(t):
                return False
        return True
