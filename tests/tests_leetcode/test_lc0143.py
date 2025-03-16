import pytest

from datastructures.linkedlist import ListNode
from leetcode import lc0143

examples_list = [
    ([1, 2, 3, 4], [1, 4, 2, 3]),
    ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
    ([1, 2, 3, 4, 5, 6, 7], [1, 7, 2, 6, 3, 5, 4]),
]

examples_linkedlist = [
    tuple(ListNode().from_iterable(iterable=digits) for digits in example)  # type: ignore
    for example in examples_list
]


@pytest.mark.parametrize("head, output_true", examples_linkedlist)
def test_reorderList(
    head: ListNode | None,
    output_true: ListNode | None,
):
    lc0143.reorderList(head=head)
    assert head == output_true
