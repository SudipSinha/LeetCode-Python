"""Unique Number of Occurrences

Link: https://leetcode.com/problems/unique-number-of-occurrences/

Given an array of integers `arr`, return `true` if the number of occurrences of each value in the array is unique or `false` otherwise.
"""

from collections import Counter


def uniqueOccurrences(arr: list[int]) -> bool:
    counts = Counter(arr).values()
    return len(set(counts)) == len(counts)
