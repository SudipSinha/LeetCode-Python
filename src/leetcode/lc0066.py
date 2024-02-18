"""Plus One

Link: https://leetcode.com/problems/plus-one/

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

RADIX = 10


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        """Time complexity: O(n), space complexity: O(n).
        The space complexity can be brought down to O(1) by modifying `digits` in place.
        """
        n_digits = len(digits)
        successor = digits.copy()

        position = 0  # Units.
        carry = 0
        value_position = digits[n_digits - position - 1] + 1
        if value_position > RADIX - 1:
            value_position = value_position % RADIX
            carry = 1
        successor[n_digits - position - 1] = value_position

        while carry > 0 and n_digits - position > 0:
            position += 1
            value_position = digits[n_digits - position - 1] + carry
            carry = 0
            if value_position > RADIX - 1:
                value_position = value_position % RADIX
                carry = 1
            successor[n_digits - position - 1] = value_position

        if carry > 0:  # Add a new digit to the left.
            successor = [carry] + successor

        return successor
