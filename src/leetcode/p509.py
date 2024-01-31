"""Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
    F(0) = 0, F(1) = 1
    F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
"""

from math import sqrt


class Solution:
    def fib_iter(self, n: int) -> int:
        """Iterative solution.
        Time complexity: O(n), Space complexity: O(1).
        """
        minus2 = 0
        minus1 = 1
        curr = 0
        for _ in range(n):
            minus2 = minus1
            minus1 = curr
            curr = minus2 + minus1
        return curr

    def fib_goldenratio(self, n: int) -> int:
        """Using the golden ratio.
        https://en.wikipedia.org/wiki/Fibonacci_sequence#Relation_to_the_golden_ratio
        The computational complexity depends on that of computing the powers.
        The space complexity is O(1).
        """
        sqrt5 = sqrt(5)
        ratio_golden = (1 + sqrt5) / 2
        conjugate = (1 - sqrt5) / 2
        return round((ratio_golden**n - conjugate**n) / sqrt5)

    def fib_dp_list(self, n: int) -> int:
        """Dynamic programming solution.
        Time complexity: O(n), Space complexity: O(1).
        """
        if n in {0, 1}:
            return n

        memo = [0 for _ in range(n + 1)]  # n -> Fib(n)
        memo[1] = 1

        def fib_dp_aux(m: int, memo: list[int]):
            if m in {0, 1}:
                return m
            memo[m] = fib_dp_aux(m - 1, memo) + fib_dp_aux(m - 2, memo)
            return memo[m]

        return fib_dp_aux(n, memo)

    def fib_dp_dict(self, n: int) -> int:
        """Dynamic programming solution.
        Time complexity: O(n), Space complexity: O(1).
        """
        memo = {0: 0, 1: 1}  # n -> Fib(n)

        def fib_dp_aux(m: int, memo: dict[int, int]):
            if m in memo:
                return memo[m]
            return fib_dp_aux(m - 1, memo) + fib_dp_aux(m - 2, memo)

        return fib_dp_aux(n, memo)
