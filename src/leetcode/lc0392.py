"""Is Subsequence

Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).
"""


class Solution:
    def isSubsequence_simple(self, s: str, t: str) -> bool:
        """Time complexity: O(mn), Space complexity: O(1)."""
        idx_t = 0
        for char in s:
            while idx_t < len(t) and char != t[idx_t]:
                idx_t += 1
            idx_t += 1
            if idx_t > len(t):
                return False
        return True

    def isSubsequence_dp(self, s: str, t: str) -> bool:
        """Dynamic programming solution. Copied from:
        https://leetcode.com/problems/is-subsequence/solutions/4074367/93-76-two-pointers-dp/
        Time complexity: O(mn), Space complexity: O(1).
        """
        nxt = [{} for _ in range(len(t) + 1)]
        for i in range(len(t) - 1, -1, -1):
            nxt[i] = nxt[i + 1].copy()
            nxt[i][t[i]] = i + 1
        
        i = 0
        for c in s:
            if c in nxt[i]:
                i = nxt[i][c]
            else:
                return False
        return True
