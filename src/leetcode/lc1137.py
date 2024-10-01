"""N-th Tribonacci Number

Link: https://leetcode.com/problems/n-th-tribonacci-number/

The Tribonacci sequence `T_n` is defined as follows:

`T_0 = 0`, `T_1 = 1`, `T_2 = 1`, and `T_{n+3} = T_n + T_{n+1} + T_{n+2}` for `n >= 0`.

Given `n`, return the value of `T_n`.
"""


def tribonacci_hashmap(n: int) -> int:
    """Time complexity: O(n), space complexity: O(n)."""

    cache = {0: 0, 1: 1, 2: 1}

    def _inner(n: int = n) -> int:
        if n in cache:
            return cache[n]
        cache[n] = _inner(n - 3) + _inner(n - 2) + _inner(n - 1)
        return cache[n]

    return _inner()


def tribonacci_iter(n: int) -> int:
    """Time complexity: O(n), space complexity: O(1)."""

    if n == 0:
        return 0
    elif n in {1, 2}:
        return 1

    minus1 = 0
    minus2 = 1
    minus3 = 1
    curr = 0

    for _ in range(3, n + 1):
        curr = minus1 + minus2 + minus3
        (minus1, minus2, minus3) = (minus2, minus3, curr)

    return curr
