"""Reverse Words in a String III

Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/

Given a string `s`, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
"""


def reverseWords(s: str) -> str:
    words = s.split(" ")
    return " ".join(word[::-1] for word in words)
