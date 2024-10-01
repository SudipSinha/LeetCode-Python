"""Maximum Number of Vowels in a Substring of Given Length

Link: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

Given a string `s` and an integer `k`, return the maximum number of vowel letters in any substring of `s` with length `k`.

Vowel letters in English are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.
"""


def maxVowels_sw(s: str, k: int) -> int:
    """Sliding window approach.
    Time complexity: O(n), space complexity: O(n).
    """
    vowels = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}

    n_vowels__cur = sum(1 for char in s[0:k] if char in vowels)
    n_vowels__max = n_vowels__cur

    for i in range(1, len(s) - k + 1):
        if s[i - 1] in vowels:
            n_vowels__cur -= 1
        if s[i + k - 1] in vowels:
            n_vowels__cur += 1

        if n_vowels__cur > n_vowels__max:
            n_vowels__max = n_vowels__cur

    return n_vowels__max
