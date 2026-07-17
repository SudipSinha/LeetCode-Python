"""Longest Palindromic Subsequence

Link: https://leetcode.com/problems/longest-palindromic-subsequence/

Given a string `s`, find the longest palindromic subsequence's length in `s`.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
"""

from leetcode import lc1143


def longestPalindromeSubseq_lcs(s: str) -> int:
    """Relies on longest common subsequence.
    Time complexity: O(n^2), space complexity: O(n^2).
    """
    return lc1143.longestCommonSubsequence_length(text1=s, text2=s[::-1])


def longestPalindromeSubseq_dp(s: str) -> int:
    """Relies on idea from the longest palindromic substring.
    Time complexity: O(n^2), space complexity: O(n^2).
    """
    if not s:
        return 0

    cache = [[0] * len(s) for _ in range(len(s))]
    for i in range(len(s)):
        cache[i][i] = 1

    def _aux(left: int = 0, right: int = len(s) - 1) -> int:
        nonlocal cache

        if left < 0 or right == len(s) or left > right:
            return 0

        if s[left] == s[right]:
            length = 1 if left == right else 2
            cache[left][right] = length + _aux(left - 1, right + 1)
        else:
            cache[left][right] = max(_aux(left - 1, right), _aux(left, right + 1))
        return cache[left][right]

    for i in range(len(s)):
        _aux(i, i)  # Base case: single character.
        _aux(i, i + 1)  # Base case: two characters.

    return max(max(row) for row in cache)
