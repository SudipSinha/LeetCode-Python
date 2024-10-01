"""Reorder List

Link: https://leetcode.com/problems/reorder-list/

You are given the head of a singly linked-list. The list can be represented as:
`L_0 → L_1 → … → L_{n - 1} → L_n`

Reorder the list to be on the following form:
`L_0 → L_n → L_1 → L_{n - 1} → L_2 → L_{n - 2} → …`

You may not modify the values in the list's nodes. Only nodes themselves may be changed."""

from datastructures.linkedlist import ListNode


def reorderList(head: ListNode | None) -> None:
    """Do not return anything, modify head in-place instead."""
    # Split the linked list from the midpoint.
    if not head:
        return None
    mid = head.middle(mode="left")
    #   Special check for a single node linked list.
    if mid.successor:  # type: ignore
        part2 = mid.successor  # type: ignore
    mid.successor = None  # type: ignore
    part1 = head

    part2_reversed = part2.reverse()

    head = ListNode.merge_alternate(head1=part1, head2=part2_reversed)
