"""Removing Stars From a String

Link: https://leetcode.com/problems/removing-stars-from-a-string/

You are given a string `s`, which contains stars `*`.

In one operation, you can:
*   Choose a star in `s`.
*   Remove the closest non-star character to its left, as well as remove the star itself.

Return the string after all stars have been removed.

Note:
*   The input will be generated such that the operation is always possible.
*   It can be shown that the resulting string will always be unique.
"""


def removeStars(s: str) -> str:
    """Time complexity: O(n), space complexity: O(n).
    The space complexity can be reduced to a constant by using a string.
    """
    stack: list[str] = []
    for c in s:
        if c == "*" and stack:
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)
