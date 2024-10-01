"""Reverse Linked List

Link: https://leetcode.com/problems/reverse-linked-list/

Given the `head` of a singly linked list, reverse the list, and return the reversed list.
"""

from datastructures.linkedlist import ListNode


def reverseList(head: ListNode | None) -> ListNode | None:
    if not head:
        return None
    return head.reverse()
