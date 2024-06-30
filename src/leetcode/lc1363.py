"""Largest Multiple of Three

Link: https://leetcode.com/problems/largest-multiple-of-three/

Given an array of digits `digits`, return the largest multiple of three that can be formed by concatenating some of the given digits in any order. If there is no answer return an empty string.

Since the answer may not fit in an integer data type, return the answer as a string. Note that the returning answer must not contain unnecessary leading zeros.
"""

from functools import cache


def digits_to_largest_num(digits: list[int]) -> str:
    """Time complexity: O(n) (use counting sort), space complexity: O(1)."""
    digits.sort(reverse=True)
    if digits and all(d == 0 for d in digits):
        return "0"
    return "".join(str(d) for d in digits)


def largestMultipleOfThree_math(digits: list[int]) -> str:
    """Time complexity: O(n), space complexity: O(1).
    Logic:
    *   To get the largest number:
        1.  The first priority is to remove minimum number of digits
        2.  The second priority is to remove smaller digits.
        3.  The largest number is one with the digits in descending order.
    *   Get the sum. If sum % 3 =
        *   0: We are done.
        *   1: We try to remove
            1.  (better) One digit d with d % 3 = 1
            2.  (worse) Two digits d with d % 3 = 2
        *   2: We try to remove
            1.  (better) One digit d with d % 3 = 2
            2.  (worse) Two digits d with d % 3 = 1
    """

    mod1_1x = [3 * i + 1 for i in range(3)]
    mod2_1x = [3 * i + 2 for i in range(3)]
    mod1_2x = []
    mod2_2x = []
    for i in range(3):
        for j in range(i, 3):
            mod1_2x.append((mod1_1x[i], mod1_1x[j]))
            mod2_2x.append((mod2_1x[i], mod2_1x[j]))
    match sum(digits) % 3:
        case 0:
            return digits_to_largest_num(digits)
        case 1:
            for k in mod1_1x:
                if k in digits:
                    digits.remove(k)
                    return digits_to_largest_num(digits)
            for i, j in mod2_2x:
                if i in digits and j in digits and (i != j or digits.count(i) >= 2):
                    digits.remove(i)
                    digits.remove(j)
                    return digits_to_largest_num(digits)
        case 2:
            for k in mod2_1x:
                if k in digits:
                    digits.remove(k)
                    return digits_to_largest_num(digits)
            for i, j in mod1_2x:
                if i in digits and j in digits and (i != j or digits.count(i) >= 2):
                    digits.remove(i)
                    digits.remove(j)
                    return digits_to_largest_num(digits)
    return ""


def largestMultipleOfThree_dp(digits: list[int]) -> str:
    """Time complexity: O(2^n), space complexity: O(n)."""
    digits.sort()

    @cache
    def _dp(digits_int=digits):
        if not digits_int:
            return ""
        if sum(digits_int) % 3 == 0:
            return digits_to_largest_num(digits_int)
        results = []
        for d in digits_int:
            digits_int.remove(d)
            if result_d := _dp(digits_int):
                results.append(result_d)
            digits_int.append(d)
        return str(max(int(n) for n in results)) if results else ""

    return _dp()
