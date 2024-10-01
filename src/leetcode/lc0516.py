"""Longest Palindromic Subsequence

Link: https://leetcode.com/problems/longest-palindromic-subsequence/

Given a string `s`, find the longest palindromic subsequence's length in `s`.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
"""

from leetcode import lc1143


def longestPalindromeSubseq_lcs(s: str) -> int:
    """Relies on longest common subsequence."""
    lcs = lc1143.longestCommonSubsequence_first(text1=s, text2=s[::-1])
    return lcs["length"]


def longestPalindromeSubseq_dp(s: str) -> int:
    """Relies on idea from the longest palindromic substring."""
    if not s:
        return 0

    cache = [[0] * len(s) for _ in range(len(s))]
    for i in range(len(s)):
        cache[i][i] = 1

    def _lps_aux(left: int = 0, right: int = len(s) - 1) -> int:
        nonlocal cache

        if left < 0 or right == len(s) or left > right:
            return 0

        if s[left] == s[right]:
            length = 1 if left == right else 2
            cache[left][right] = length + _lps_aux(left - 1, right + 1)
        else:
            cache[left][right] = max(
                _lps_aux(left - 1, right), _lps_aux(left, right + 1)
            )
        return cache[left][right]

    for i in range(len(s)):
        _lps_aux(i, i)  # Base case: single character.
        _lps_aux(i, i + 1)  # Base case: two characters.

    return max(max(row) for row in cache)
