"""Find the Difference of Two Arrays

Link: https://leetcode.com/problems/find-the-difference-of-two-arrays/

Given two `0`-indexed integer arrays `nums1` and `nums2`, return a list answer of size 2 where:

`answer[0]` is a list of all distinct integers in `nums1` which are not present in `nums2`.
`answer[1]` is a list of all distinct integers in `nums2` which are not present in `nums1`.
Note that the integers in the lists may be returned in any order.
"""


def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    (n1, n2) = (set(nums1), set(nums2))
    return [list(n1 - n2), list(n2 - n1)]
