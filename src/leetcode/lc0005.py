"""Longest Palindromic Substring

Link: https://leetcode.com/problems/longest-palindromic-substring/

Given a string `s`, return the longest palindromic substring in `s`.
"""

from math import ceil, floor
from typing import TypedDict


class LP(TypedDict):
    length: int
    substrs: set[str]


def _is_palindrome(s: str) -> bool:
    mid = len(s) / 2
    mid_left = floor(mid)
    mid_right = ceil(mid)
    return s[0:mid_left] == s[: mid_right - 1 : -1]


def longestPalindrome_naive(s: str) -> LP:
    """Time complexity: O(n^3), space complexity: O(n)."""
    output: LP = {"length": 0, "substrs": set()}
    if not s:
        return output
    for substr__len in range(len(s), 0, -1):
        for idx_start in range(0, len(s) - substr__len + 1):
            if _is_palindrome(s[idx_start : idx_start + substr__len]):
                if substr__len > output["length"]:
                    output["length"] = substr__len
                    output["substrs"].clear()
                    output["substrs"].add(s[idx_start : idx_start + substr__len])
                if substr__len == output["length"]:
                    output["substrs"].add(s[idx_start : idx_start + substr__len])
                else:
                    break
    return output


def longestPalindrome_centerout(s: str) -> LP:
    """Time complexity: O(n^2), space complexity: O(n)."""
    if not s:
        return {"length": 0, "substrs": {""}}
    length__max = 0
    substr__max: set[str] = set()
    for center in range(0, len(s)):
        #   Base case: single character.
        radius = 1
        while (
            0 <= center - radius < len(s)
            and 0 <= center + radius < len(s)
            and s[center - radius] == s[center + radius]
        ):
            radius += 1
        length = 2 * radius - 1
        if length > length__max:
            length__max = length
            substr__max.clear()
            substr__max.add(s[center - (radius - 1) : center + (radius - 1) + 1])
        elif length == length__max:
            substr__max.add(s[center - (radius - 1) : center + (radius - 1) + 1])

        #   Base case: two characters.
        radius = 0
        while (
            0 <= center - radius < len(s)
            and 0 <= center + radius + 1 < len(s)
            and s[center - radius] == s[center + radius + 1]
        ):
            radius += 1
        length = 2 * radius
        if length > length__max:
            length__max = length
            substr__max.clear()
            substr__max.add(s[center - (radius - 1) : center + radius + 1])
        elif length == length__max:
            substr__max.add(s[center - (radius - 1) : center + radius + 1])

    return {"length": length__max, "substrs": substr__max}


def longestPalindrome_dp(s: str) -> LP:
    """Time complexity: O(n^2), space complexity: O(n^2)."""
    if not s:
        return {"length": 0, "substrs": set()}
    palindrome = [[False] * len(s) for _ in range(len(s))]
    length__max = 1
    substr__max: set[str] = set()

    for i in range(len(s)):
        #   Base case: single character.
        palindrome[i][i] = True
        if length__max == 1:
            substr__max.add(s[i])
        #   Base case: two characters.
        if i + 1 < len(s) and s[i] == s[i + 1]:
            palindrome[i][i + 1] = True
            if length__max == 1:
                length__max = 2
                substr__max.clear()
                substr__max.add(s[i : i + 2])
            elif length__max == 2:
                substr__max.add(s[i : i + 2])

    for length in range(3, len(s) + 1):
        for left in range(0, len(s) - length + 1):
            right = left + length - 1
            if palindrome[left + 1][right - 1] and s[left] == s[right]:
                palindrome[left][right] = True
                if length > length__max:
                    length__max = length
                    substr__max.clear()
                    substr__max.add(s[left : right + 1])
                elif length == length__max:
                    substr__max.add(s[left : right + 1])

    return {"length": length__max, "substrs": substr__max}
