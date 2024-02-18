"""Longest Substring Without Repeating Characters

Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string `s`, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring_naive(self, s: str) -> int:
        """Time complexity: O(n^2), space complexity: O(1)."""
        length__max = 0
        for i in range(len(s)):
            current = 1
            for j in range(i + 1, len(s)):
                if s[j] in s[i:j]:
                    break
                current += 1
            length__max = max(current, length__max)
        return length__max

    def lengthOfLongestSubstring_hashmap(self, s: str) -> int:
        """Time complexity: O(n^2), space complexity: O(1)."""
        length__max = 0
        for idx_start, letter_start in enumerate(s):
            visited = {letter_start}
            current = 1
            for letter_new in s[idx_start + 1 :]:
                if letter_new in visited:
                    break
                current += 1
                visited.add(letter_new)
            length__max = max(current, length__max)
        return length__max

    def lengthOfLongestSubstring_slidingwindow(self, s: str) -> int:
        """Time complexity: O(n), space complexity: O(1)."""
        head = 0
        length__max = 0
        seen: dict[str, int] = {}
        for tail, letter in enumerate(s):
            if letter in seen and head <= seen[letter]:
                head = seen[letter] + 1
            seen[letter] = tail
            length__max = max(length__max, tail - head + 1)
        return length__max
