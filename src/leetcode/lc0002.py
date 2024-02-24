"""Add Two Numbers

Link: https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in _reverse order_, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
# mypy: ignore-errors


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode | None = next

    def __str__(self) -> str:
        """String representation."""
        return str(self.val)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ListNode):
            return False

        while self or other:
            if (self and not other) or (not self and other):
                return False
            if self.val != other.val:
                return False
            self = self.next
            other = other.next

        return True


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        sum_dummyhead = ListNode()
        ptr_ll__sum = sum_dummyhead  # Moving pointer.
        carry = 0
        while l1 or l2 or carry != 0:
            if l1 is None and l2 is None and carry == 0:
                break
            elif l1 is not None and l2 is None and carry == 0:
                ptr_ll__sum.next = l1
                break
            elif l1 is None and l2 is not None and carry == 0:
                ptr_ll__sum.next = l2
                break
            else:
                digits__sum = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
                ptr_ll__sum.next = ListNode()
                ptr_ll__sum = ptr_ll__sum.next
                ptr_ll__sum.val = digits__sum % 10
                carry = digits__sum // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return sum_dummyhead.next
