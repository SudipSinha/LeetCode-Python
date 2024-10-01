"""Merge Strings Alternately

Link: https://leetcode.com/problems/merge-strings-alternately/

You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""


def mergeAlternately(word1: str, word2: str) -> str:
    """Time complexity: O(m + n), space complexity: O(m + n)."""
    merged = [""] * (len(word1) + len(word2))
    i = j = 0
    for k, _ in enumerate(merged):
        if i < len(word1) and j < len(word2):
            if k % 2 == 0:
                merged[k] = word1[i]
                i += 1
            else:
                merged[k] = word2[j]
                j += 1
        elif i < len(word1):
            merged[k:] = word1[i:]
            break
        else:
            merged[k:] = word2[j:]
            break
    return "".join(merged)
