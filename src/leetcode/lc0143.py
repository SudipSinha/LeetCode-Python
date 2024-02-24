"""Reorder List

Link: https://leetcode.com/problems/reorder-list/

You are given the head of a singly linked-list. The list can be represented as:
`L0 → L1 → … → Ln - 1 → Ln`

Reorder the list to be on the following form:
`L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …`

You may not modify the values in the list's nodes. Only nodes themselves may be changed."""
# mypy: ignore-errors

from leetcode import lc0206
from leetcode.lc0002 import ListNode


class Solution:
    @classmethod
    def middle_first(cls, head: ListNode | None) -> ListNode | None:
        """Middle of the linked list. Returns the first one if there is a tie."""
        if not head:
            return None
        slow = fast = head
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    @classmethod
    def merge_alternate(
        cls, head1: ListNode | None, head2: ListNode | None
    ) -> ListNode | None:
        """Merged linked list that alternates between the two arguments."""
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
        mid = Solution.middle_first(head=head)
        if mid.next:  # Fails for a single node linked list.
            part2 = mid.next
        mid.next = None
        part1 = head

        part2_reversed = lc0206.Solution().reverseList(head=part2)

        return Solution.merge_alternate(head1=part1, head2=part2_reversed)
