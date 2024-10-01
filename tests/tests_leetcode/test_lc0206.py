import pytest

from datastructures.linkedlist import ListNode
from leetcode import lc0206

examples_list = [
    ([1, 2], [2, 1]),
    ([], []),
    ([1, 2, 3, 4], [4, 3, 2, 1]),
]

examples_linkedlist = [
    tuple(ListNode.from_iterable(iterable=digits) for digits in example)  # type: ignore
    for example in examples_list
]


@pytest.mark.parametrize("head, output_true", examples_linkedlist)
def test_reverseList(
    head: ListNode | None,
    output_true: ListNode | None,
):
    output_calc = lc0206.reverseList(head=head)
    assert output_calc == output_true
