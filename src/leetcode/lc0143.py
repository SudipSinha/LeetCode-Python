"""Reorder List

Link: https://leetcode.com/problems/reorder-list/

You are given the head of a singly linked-list. The list can be represented as:
`L0 → L1 → … → Ln - 1 → Ln`

Reorder the list to be on the following form:
`L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …`

You may not modify the values in the list's nodes. Only nodes themselves may be changed."""
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
    @classmethod
    def generate_linkedlist(cls, digits: list[int]) -> ListNode:
        ll_dummyhead = ptr_ll = ListNode()  # Trash ListNode
        for d in digits:
            ptr_ll.next = ListNode(val=d)
            ptr_ll = ptr_ll.next
        return ll_dummyhead.next

    @classmethod
    def print_linkedlist(cls, head: ListNode | None) -> str:
        nodes_value = []
        while head:
            nodes_value.append(str(head))
            head = head.next
        return " → ".join(nodes_value)

    @classmethod
    def middle(cls, head: ListNode | None) -> ListNode | None:
        if not head:
            return None
        slow = fast = head
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    @classmethod
    def reverse(cls, head: ListNode | None) -> ListNode | None:
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

    @classmethod
    def alternate(
        cls, head1: ListNode | None, head2: ListNode | None
    ) -> ListNode | None:
        pointer1 = head1
        pointer2 = head2
        dummyhead = merged = ListNode()  # Dummy node.
        while pointer1 or pointer2:
            if pointer1:
                merged.next = pointer1
                merged = merged.next
                pointer1 = pointer1.next
            if pointer2:
                merged.next = pointer2
                merged = merged.next
                pointer2 = pointer2.next
        return dummyhead.next

    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Split the linked list from the midpoint.
        mid = Solution.middle(head=head)
        if mid.next:  # Fails for a single node linked list.
            part2 = mid.next
        mid.next = None
        part1 = head

        part2_reversed = Solution.reverse(head=part2)

        return Solution.alternate(head1=part1, head2=part2_reversed)
