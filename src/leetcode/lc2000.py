"""Reverse Prefix of Word

Link: https://leetcode.com/problems/reverse-prefix-of-word/

Given a 0-indexed string `word` and a character `ch`, reverse the segment of `word` that starts at index `0` and ends at the index of the first occurrence of `ch` (inclusive). If the character `ch` does not exist in `word`, do nothing.

For example, if `word = "abcdefd"` and `ch = "d"`, then you should reverse the segment that starts at `0` and ends at `3` (inclusive). The resulting string will be `"dcbaefd"`.
Return the resulting string.
"""

from collections import deque


def reversePrefix_naive(word: str, ch: str) -> str:
    """Time complexity: O(n), space complexity: O(n)."""
    reversed_prefix = word
    reverse_index = None
    for i, c in enumerate(word):
        if c == ch:
            reverse_index = i
            break
    if reverse_index:
        reversed_prefix_list = list(word)
        for i in range(0, reverse_index + 1):
            reversed_prefix_list[i] = word[reverse_index - i]
        reversed_prefix = "".join(reversed_prefix_list)
    return reversed_prefix


def reversePrefix_deque(word: str, ch: str) -> str:
    """Time complexity: O(n), space complexity: O(n).
    Beats 100% for runtime: https://leetcode.com/problems/reverse-prefix-of-word/submissions/1603193462.
    """
    queue: deque[str] = deque()
    reverse = False
    for c in word:
        if not reverse:
            queue.appendleft(c)
        else:
            queue.append(c)
        if not reverse and c == ch:
            reverse = True
    if not reverse:
        return word
    return "".join(queue)
