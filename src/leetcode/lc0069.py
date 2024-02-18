"""Sqrt(x)

Link: https://leetcode.com/problems/sqrtx/

Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use `pow(x, 0.5)` in C++ or `x ** 0.5` in python.
"""


class Solution:
    def mySqrt_naive(self, x: int) -> int:
        sqrt = 0
        while sqrt * sqrt <= x:
            sqrt += 1
        return sqrt - 1

    def mySqrt_binarysearch(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        left = 0
        right = x // 2
        while left <= right:
            mid = left + (right - left) // 2
            sq = mid * mid
            if sq == x:
                return mid
            elif sq < x:
                left = mid + 1
            else:
                right = mid - 1
        return right
