"""Middle of the Linked List

Link: https://leetcode.com/problems/middle-of-the-linked-list/

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""

from leetcode.lc0002 import ListNode


class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None
        slow = head
        fast = head
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        if not fast.next:
            return slow
        else:
            return slow.next
