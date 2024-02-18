"""Factorial Trailing Zeroes

Link: https://leetcode.com/problems/factorial-trailing-zeroes/

Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        """Time complexity: O(log5(n)), space complexity: O(1).
        Idea: https://brilliant.org/wiki/trailing-number-of-zeros/
        """
        zeros = 0
        div = 5
        while n > 0 and n // div > 0:
            zeros += n // div
            div *= 5
        return zeros
