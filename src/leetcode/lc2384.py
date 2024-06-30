"""Largest Palindromic Number

Link: https://leetcode.com/problems/largest-palindromic-number/

You are given a string `num` consisting of digits only.

Return the largest palindromic integer (in the form of a string) that can be formed using digits taken from `num`. It should not contain leading zeroes.

Notes:
*   You do not need to use all the digits of `num`, but you must use at least one digit.
*   The digits can be reordered.
"""

from collections import Counter


def largestPalindromic(num: str) -> str:
    """Time complexity: O(n), space complexity: O(n)."""
    start: list[str] = []
    reserve: str = ""
    digits: list[str] = list(num)
    digits_counter: Counter[str] = Counter(digits)
    for d in sorted(digits_counter, reverse=True):
        if len(start) > 0 or (d != "0" and digits_counter[d] >= 2):
            start.append(d * (digits_counter[d] // 2))
        if digits_counter[d] % 2 == 1 and not reserve:
            reserve = d  # Save for the middle element
    merged = "".join(start + [reserve if reserve else ""] + start[::-1])
    if not merged and num:
        merged = "0"
    return merged
