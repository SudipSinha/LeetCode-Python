"""Determine if Two Strings Are Close

Link: https://leetcode.com/problems/determine-if-two-strings-are-close/

Two strings are considered close if you can attain one from the other using the following operations:

*   Operation 1: Swap any two existing characters.
    For example, `abcde` -> `aecdb`
*   Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
    For example, `aacabb` -> `bbcbaa` (all `a`'s turn into `b`'s, and all `b`'s turn into `a`'s)

You can use the operations on either string as many times as necessary.

Given two strings, `word1` and `word2`, return `true` if `word1` and `word2` are close, and `false` otherwise.
"""

from collections import Counter


def closeStrings(word1: str, word2: str) -> bool:
    (c1, c2) = (Counter(word1), Counter(word2))
    same_letters = sorted(c1.keys()) == sorted(c2.keys())
    same_counts = sorted(c1.values()) == sorted(c2.values())
    return same_letters and same_counts
