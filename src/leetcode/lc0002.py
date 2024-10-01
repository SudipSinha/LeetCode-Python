"""Add Two Numbers

Link: https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in _reverse order_, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

from datastructures.linkedlist import ListNode


def addTwoNumbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    sum_dummyhead = ListNode(data=0)
    ptr_ll__sum = sum_dummyhead  # Moving pointer.
    carry = 0
    while l1 or l2 or carry != 0:
        if l1 is None and l2 is None and carry == 0:
            break
        elif l1 is not None and l2 is None and carry == 0:
            ptr_ll__sum.successor = l1
            break
        elif l1 is None and l2 is not None and carry == 0:
            ptr_ll__sum.successor = l2
            break
        else:
            digits__sum = carry + (l1.data if l1 else 0) + (l2.data if l2 else 0)
            ptr_ll__sum.successor = ListNode(data=0)
            ptr_ll__sum = ptr_ll__sum.successor
            ptr_ll__sum.data = digits__sum % 10
            carry = digits__sum // 10
        if l1:
            l1 = l1.successor
        if l2:
            l2 = l2.successor
    return sum_dummyhead.successor
