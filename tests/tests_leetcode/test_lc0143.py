import pytest
from leetcode import lc0143
from leetcode.lc0002 import ListNode

from tests.tests_leetcode.test_lc0002 import generate_linkedlist

examples_list = [
    ([1, 2, 3, 4], [1, 4, 2, 3]),
    ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
    ([1, 2, 3, 4, 5, 6, 7], [1, 7, 2, 6, 3, 5, 4]),
]

examples_linkedlist = [
    tuple(generate_linkedlist(digits=digits) for digits in example)  # type: ignore
    for example in examples_list
]


@pytest.mark.parametrize("head, output_true", examples_linkedlist)
def test_reorderList(
    head: ListNode | None,
    output_true: ListNode | None,
):
    lc0143.Solution().reorderList(head=head)
    assert head == output_true
