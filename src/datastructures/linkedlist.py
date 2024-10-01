from __future__ import annotations

from collections.abc import Iterable
from copy import deepcopy
from dataclasses import dataclass
from typing import Literal


# Definition for singly-linked list.
@dataclass
class ListNode:
    data: int
    next: ListNode | None = None

    def __str__(self) -> str:
        output = ""
        current: ListNode | None = self
        while current is not None:
            output += f"{current.data} → "
            current = current.next
        return output + str(current)

    def __repr__(self) -> str:
        output = ""
        current: ListNode | None = self
        while current is not None:
            output += f"ListNode({current.data}) → "
            current = current.next
        return output + str(current)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ListNode):
            return False
        while self or other:
            if (self and not other) or (not self and other):
                return False
            elif self.data != other.data:  # type: ignore
                return False
            self = self.next  # type: ignore
            other = other.next  # type: ignore
        return True

    def __len__(self) -> int:
        length = 0
        current = self
        while (
            current is not None
        ):  # Cannot use `current` as conditional as it depends on `__len__()`.
            length += 1
            current = current.next  # type: ignore
        return length

    @classmethod
    def from_iterable(cls, iterable: Iterable) -> ListNode | None:
        if not iterable:
            return None
        dummy_head = ptr_ll = ListNode(data=0)  # Dummy node.
        for element in iterable:
            ptr_ll.next = ListNode(data=element)
            ptr_ll = ptr_ll.next
        return dummy_head.next

    @classmethod
    def merge_alternate(
        cls, head1: ListNode | None, head2: ListNode | None
    ) -> ListNode | None:
        """Merged linked list that alternates between the two arguments."""
        pointer1 = head1
        pointer2 = head2
        dummyhead = merged = ListNode(data=0)  # Dummy node.
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

    def reverse(self) -> ListNode | None:
        if not self:
            return None
        left = self
        right = self.next
        left_of_left = None
        while right:
            right_of_right = right.next
            right.next = left
            left.next = left_of_left
            left_of_left = left
            left = right
            right = right_of_right
        return left

    def middle(self, mode: Literal["left", "right"] = "left") -> ListNode | None:
        if not self:
            return None
        slow = self
        fast = self
        while fast.next and fast.next.next:
            slow = slow.next  # type: ignore
            fast = fast.next.next
        if not fast.next:  # Unique middle node.
            return slow
        elif mode == "left":
            return slow
        else:
            return slow.next  # type: ignore

    def appendleft(self, element: int) -> None:
        """Append at the beginning in-place."""
        updated = ListNode(data=element)
        updated.next = self
        self.__dict__ = deepcopy(
            updated.__dict__
        )  # https://stackoverflow.com/a/29591356/1369696

    def append(self, element: int) -> None:
        """Append at the end in-place."""
        current = self
        while current.next is not None:
            current = current.next
        current.next = ListNode(data=element)

    def popleft(self) -> int:
        first = self.data
        self.__dict__ = deepcopy(
            self.next.__dict__
        )  # https://stackoverflow.com/a/29591356/1369696
        return first

    def pop(self) -> int:
        prev = None
        curr = self
        while curr.next is not None:
            prev = curr
            curr = curr.next
        prev.next = None  # type: ignore
        return curr.data
