"""Longest Common Subsequence
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
"""

import numpy
from typing import TypedDict


class LCS(TypedDict):
    length: int
    subseq: str


class Solution:
    def longestCommonSubsequence_first(self, text1: str, text2: str) -> LCS:
        """Dynamic programming solution.
        Time complexity: O(mn), Space complexity: O(mn).
        """
        lengths = numpy.full(shape=(len(text1) + 1, len(text2) + 1), fill_value=-1)
        lengths[0, :].fill(0)
        lengths[:, 0].fill(0)
        subseqs = numpy.full(
            shape=(len(text1) + 1, len(text2) + 1),
            fill_value="",
            dtype=f"U{min(len(text1), len(text2))}",
        )  # It dtype is not specified, it takes '<U1' and only one character is stored.

        # Define the recurrence relation
        def longestCommonSubsequence_aux(idx1: int, idx2: int) -> LCS:
            nonlocal lengths
            nonlocal subseqs
            
            if lengths[idx1, idx2] >= 0:
                return {
                    "length": lengths[idx1, idx2],
                    "subseq": subseqs[idx1, idx2],
                }

            if text1[idx1 - 1] == text2[idx2 - 1]:
                upleft = longestCommonSubsequence_aux(idx1 - 1, idx2 - 1)
                lengths[idx1, idx2] = upleft["length"] + 1
                subseqs[idx1, idx2] = upleft["subseq"] + text1[idx1 - 1]
                return {
                    "length": lengths[idx1, idx2],
                    "subseq": subseqs[idx1, idx2],
                }
            else:
                up = longestCommonSubsequence_aux(idx1 - 1, idx2)
                left = longestCommonSubsequence_aux(idx1, idx2 - 1)
                if up["length"] > left["length"]:
                    lengths[idx1, idx2] = up["length"]
                    subseqs[idx1, idx2] = up["subseq"]
                else:
                    lengths[idx1, idx2] = left["length"]
                    subseqs[idx1, idx2] = left["subseq"]
                return {
                    "length": lengths[idx1, idx2],
                    "subseq": subseqs[idx1, idx2],
                }

        result = longestCommonSubsequence_aux(idx1=len(text1), idx2=len(text2))

        return {
            "length": result["length"],
            "subseq": result["subseq"],
        }

    # def longestCommonSubsequence_all(self, text1: str, text2: str) -> LCS:
    #     """Dynamic programming solution.
    #     Time complexity: O(mn), Space complexity: O(mn).
    #     """
    #     lengths = numpy.full(shape=(len(text1) + 1, len(text2) + 1), fill_value=-1)
    #     lengths[0, :].fill(0)
    #     lengths[:, 0].fill(0)

    #     # Define the recurrence relation
    #     def lcs_length(idx1: int, idx2: int) -> int:

    #         if lengths[idx1, idx2] >= 0:
    #             return lengths[idx1, idx2]

    #         if text1[idx1 - 1] == text2[idx2 - 1]:
    #             return lcs_length(idx1 - 1, idx2 - 1) + 1
    #         else:
    #             return max(
    #                 lcs_length(idx1 - 1, idx2),
    #                 lcs_length(idx1, idx2 - 1),
    #             )

    #     def lcs_subseqs(idx1: int, idx2: int) -> set[str]:
    #         if idx1 == 0 or idx2 == 0:
    #             return ""
    #         if text1[idx1 - 1] == text2[idx2 - 1]:
    #             return lcs_subseqs(idx1 - 1, idx2 - 1) + text1[idx1 - 1]

    #         subseqs = [""]
    #         up = lengths[idx1 - 1, idx2]
    #         left = lengths[idx1, idx2 - 1]
    #         if up > left:
    #             subseqs[-1] = lcs_subseqs(idx1 - 1, idx2)
    #         elif left > up:
    #             subseqs[-1] = lcs_subseqs(idx1, idx2 - 1)
    #         else:
    #             subseqs[-1] = lcs_subseqs(idx1 - 1, idx2)
    #             subseqs.append(lcs_subseqs(idx1, idx2 - 1))
    #         return subseqs

    #     length = lcs_length(idx1=len(text1), idx2=len(text2))
    #     subseqs = lcs_subseqs(idx1=len(text1), idx2=len(text2))

    #     return {
    #         "length": length,
    #         "subseq": subseqs,
    #     }
