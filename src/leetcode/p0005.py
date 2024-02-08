"""Longest Palindromic Substring

Given a string `s`, return the longest palindromic substring in `s`.
"""


def _is_palindrome_substr(s: str, idx_start: int = 0, substr__len: int = -1) -> bool:
    """Theoretically this should be faster, but Python :("""
    substr__len = len(s) if substr__len == -1 else substr__len
    for i in range(substr__len // 2):
        if s[idx_start + i] != s[idx_start + substr__len - i - 1]:
            return False
    return True


def _is_palindrome(s: str) -> bool:
    return s[::-1] == s


class Solution:
    def longestPalindrome_naive(self, s: str) -> str:
        """Time complexity: O(n^2), Space complexity: O(n)."""
        for substr__len in range(len(s), 0, -1):
            for idx_start in range(0, len(s) - substr__len + 1):
                # if _is_palindrome_substr(s, idx_start, substr__len):
                if _is_palindrome(s[idx_start : idx_start + substr__len]):
                    return s[idx_start : idx_start + substr__len]
        return ""
