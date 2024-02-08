"""Longest Palindromic Substring

Given a string `s`, return the longest palindromic substring in `s`.
"""


def _is_palindrome(s: str) -> bool:
    return s[::-1] == s


class Solution:
    def longestPalindrome_naive(self, s: str) -> str:
        """Time complexity: O(n^2), Space complexity: O(n)."""
        for substr__len in range(len(s), 0, -1):
            for idx_start in range(0, len(s) - substr__len + 1):
                if _is_palindrome(s[idx_start : idx_start + substr__len]):
                    return s[idx_start : idx_start + substr__len]
        return ""
