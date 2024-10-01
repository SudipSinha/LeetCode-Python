"""Middle of the Linked List

Link: https://leetcode.com/problems/middle-of-the-linked-list/

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""

from leetcode.lc0002 import ListNode


def middleNode(head: ListNode | None) -> ListNode | None:
    if not head:
        return None
    return head.middle(mode="right")
