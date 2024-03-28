"""Merge Intervals

Link: https://leetcode.com/problems/merge-intervals/

Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""


def merge(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    merged = []
    intervals.sort(key=lambda x: x[0])
    (start__cur, end__cur) = intervals[0]
    for interval in intervals:
        if interval[0] <= end__cur:
            end__cur = max(end__cur, interval[1])
        else:
            merged.append((start__cur, end__cur))
            (start__cur, end__cur) = interval
    merged.append((start__cur, end__cur))
    return merged
