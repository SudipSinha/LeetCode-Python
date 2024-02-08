"""Reverse Words in a String III

Given a string `s`, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        return " ".join(word[::-1] for word in words)
