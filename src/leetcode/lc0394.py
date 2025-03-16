"""Decode String

Link: https://leetcode.com/problems/decode-string/

Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the encoded_string inside the square brackets is being repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, `k`. For example, there will not be input like `3a` or `2[4]`.
"""


def decodeString_recursive(s: str, idx: int = 0) -> str:
    """Time complexity: O(|s|), space complexity: O(|decoded|).
    Stolen from: https://walkccc.me/LeetCode/problems/0394/
    """

    decoded = ""
    while idx < len(s) and s[idx] != "]":
        if s[idx].isdigit():
            #   Multiplier
            multiplier = 0
            while idx < len(s) and s[idx].isdigit():
                multiplier = multiplier * 10 + int(s[idx])
                idx += 1
            idx += 1  # Skip "["
            decoded_sub = decodeString_recursive(s, idx)
            decoded += multiplier * decoded_sub
            idx += 1  # Skip "]"
        else:
            decoded += s[idx]
            idx += 1
    return decoded


def decodeString_1pass(s: str) -> str:
    """Time complexity: O(|s|), space complexity: O(|decoded|)."""
    stack: list[tuple[str, int]] = []  # (prevStr, repeatCount)

    substr__cur = ""
    multiplier__cur = 0
    for c in s:
        if c.isdigit():
            multiplier__cur = multiplier__cur * 10 + int(c)
        else:
            if c == "[":
                stack.append((substr__cur, multiplier__cur))
                substr__cur = ""
                multiplier__cur = 0
            elif c == "]":
                (substr__prev, multiplier__prev) = stack.pop()
                substr__cur = substr__prev + multiplier__prev * substr__cur
            else:
                substr__cur += c

    return substr__cur


def decodeString_backandforth(s: str) -> str:
    """Time complexity: O(|s|), space complexity: O(|decoded|)."""
    stack: list[str] = []

    for _, c in enumerate(s):
        if c == "]":
            #   Get the substring.
            substr = "".join(stack.pop())
            while stack[-1] != "[":
                substr = stack.pop() + substr

            stack.pop()  # Remove `[`.

            #   Get the multiplier.
            multiplier = ""
            while len(stack) != 0 and str.isdigit(stack[-1]):
                multiplier = stack.pop() + multiplier

            stack.append(substr * int(multiplier))
        else:
            stack.append(c)

    return "".join(stack)
