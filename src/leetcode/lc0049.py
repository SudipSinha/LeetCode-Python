"""Group Anagrams

Link: https://leetcode.com/problems/group-anagrams/

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> frozenset[frozenset[str]]:
        """Time complexity: O(len(strs) ⋅ maxlen(strs)), space complexity: O(n)."""
        anagrams = defaultdict(list)
        for word in strs:
            anagrams["".join(sorted(word))].append(word)

        return frozenset(frozenset(words) for words in anagrams.values())


print(Solution().groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
