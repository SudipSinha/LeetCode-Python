from __future__ import annotations

from collections.abc import Iterable
from copy import deepcopy
from dataclasses import dataclass
from typing import Any, Generic, Literal, TypeVar, get_args

T = TypeVar("T")


# Definition for singly-linked list.
@dataclass
class ListNode(Generic[T]):
    data: T | None = None
    successor: ListNode[T] | None = None

    def _get_type(self):
        """Determine the actual type parameter T at runtime.
        TODO: Does not work as of now.
        """
        if hasattr(
            self, "__orig_class__"
        ):  # Only available for instances of a generic class
            return get_args(self.__orig_class__)[0]
        return Any  # Default if not a generic instance

    def _default_value(self):
        """Determine the default value of the type parameter T at runtime.
        TODO: Does not work as of now.
        """
        type_ = self._get_type()
        return type_() if not isinstance(type_, TypeVar) else Any

    def __repr__(self) -> str:
        output = f"LinkedList[{self._get_type().__name__}]: "
        current: ListNode[T] | None = self
        while current is not None:
            output += (str(current.data) if current.data is not None else "∅") + " → "
            current = current.successor
        return output + "∅"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        while self or other:
            if (self and not other) or (not self and other):
                return False
            elif self.data != other.data:  # type: ignore
                return False
            self = self.successor  # type: ignore
            other = other.successor  # type: ignore
        return True

    def __len__(self) -> int:
        length = 0
        current = self
        while (
            current is not None
        ):  # Cannot use `current` as conditional as it depends on `__len__()`.
            length += 1
            current = current.successor  # type: ignore
        return length

    def from_iterable(self, iterable: Iterable[T]) -> ListNode[T] | None:
        if iterable is None or not iterable:
            return None
        type_ = self._get_type()
        dummy_head = ptr_ll = ListNode[type_]()  # type: ignore  # Dummy node.
        for element in iterable:
            if type_ != Any and not isinstance(element, type_):
                raise TypeError(f"Expected type {type_}, but got {type(element)}.")
            ptr_ll.successor = ListNode[type_](data=element)  # type: ignore
            ptr_ll = ptr_ll.successor
        return dummy_head.successor

    @classmethod
    def merge_alternate(
        cls, head1: ListNode[T] | None, head2: ListNode[T] | None
    ) -> ListNode[T] | None:
        """Merged linked list that alternates between the two arguments."""
        pointer1 = head1
        pointer2 = head2
        dummyhead = merged = ListNode[T](data=None)  # Dummy node.
        while pointer1 or pointer2:
            if pointer1:
                merged.successor = pointer1
                merged = merged.successor
                pointer1 = pointer1.successor
            if pointer2:
                merged.successor = pointer2
                merged = merged.successor
                pointer2 = pointer2.successor
        return dummyhead.successor

    def reverse(self) -> ListNode[T] | None:
        if not self:
            return None
        left = self
        right = self.successor
        left_of_left = None
        while right:
            right_of_right = right.successor
            right.successor = left
            left.successor = left_of_left
            left_of_left = left
            left = right
            right = right_of_right
        return left

    def middle(self, mode: Literal["left", "right"] = "left") -> ListNode[T] | None:
        if not self:
            return None
        slow = self
        fast = self
        while fast.successor and fast.successor.successor:
            slow = slow.successor  # type: ignore
            fast = fast.successor.successor
        if not fast.successor:  # Unique middle node.
            return slow
        elif mode == "left":
            return slow
        else:
            return slow.successor  # type: ignore

    def appendleft(self, element: T | None) -> None:
        """Append at the beginning in-place."""
        updated = ListNode[T](data=element)
        updated.successor = self
        self.__dict__ = deepcopy(
            updated.__dict__
        )  # https://stackoverflow.com/a/29591356/1369696

    def append(self, element: T | None) -> None:
        """Append at the end in-place."""
        current = self
        while current.successor is not None:
            current = current.successor
        current.successor = ListNode[T](data=element)

    def popleft(self) -> T | None:
        first = self.data
        self.__dict__ = deepcopy(
            self.successor.__dict__
        )  # https://stackoverflow.com/a/29591356/1369696
        return first

    def pop(self) -> T | None:
        prev = None
        curr = self
        while curr.successor is not None:
            prev = curr
            curr = curr.successor
        prev.successor = None  # type: ignore
        return curr.data


if __name__ == "__main__":
    #   Initialize and populate linked lists.
    ll_int = ListNode[int]().from_iterable(range(8))
    ll_float = ListNode[float]().from_iterable([4.0, 4.5, 5.0, 5.5, 6.0])
    ll_str = ListNode[str]().from_iterable(["a", "b", "c", "d", "e"])
    ll_any = ListNode().from_iterable(["a", 1, 2.0, [True, False], {"key": "value"}])  # type: ignore
    #   Print linked lists.
    print(ll_int)
    print(ll_float)
    print(ll_str)
    print(ll_any)
