import pytest

from leetcode import lc0876
from leetcode.lc0002 import ListNode

examples_list = [
    ([1, 2, 3, 4, 5], [3, 4, 5]),
    ([1, 2, 3, 4, 5, 6], [4, 5, 6]),
]

examples_linkedlist = [
    tuple(ListNode().from_iterable(iterable=digits) for digits in example)  # type: ignore
    for example in examples_list
]


@pytest.mark.parametrize("head, output_true", examples_linkedlist)
def test_middleNode(
    head: ListNode | None,
    output_true: ListNode | None,
):
    output_calc = lc0876.middleNode(head=head)
    assert output_calc == output_true
