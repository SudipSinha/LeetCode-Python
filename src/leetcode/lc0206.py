"""Reverse Linked List

Link: https://leetcode.com/problems/reverse-linked-list/

Given the `head` of a singly linked list, reverse the list, and return the reversed list.
"""

from leetcode.lc0002 import ListNode


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None
        left = head
        right = head.next
        left_of_left = None
        while right:
            right_of_right = right.next
            right.next = left
            left.next = left_of_left
            left_of_left = left
            left = right
            right = right_of_right
        return left
