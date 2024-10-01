"""Largest Number

Link: https://leetcode.com/problems/largest-number/

Given a list of non-negative integers `nums`, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.
"""


class LargerNumKey(str):
    def __lt__(self, other):
        return self + other > other + self


def largestNumber(nums: list[int]):
    largest_num = "".join(sorted(map(str, nums), key=LargerNumKey))
    return "0" if largest_num[0] == "0" else largest_num
