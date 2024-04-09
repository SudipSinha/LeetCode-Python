import pytest
from leetcode import lc0876
from leetcode.lc0002 import ListNode

from tests.tests_leetcode.test_lc0002 import generate_linkedlist

examples_list = [
    ([1, 2, 3, 4, 5], [3, 4, 5]),
    ([1, 2, 3, 4, 5, 6], [4, 5, 6]),
]


examples_linkedlist = [
    tuple(generate_linkedlist(digits=digits) for digits in example)  # type: ignore
    for example in examples_list
]


@pytest.mark.parametrize("head, output_true", examples_linkedlist)
def test_middleNode(
    head: ListNode | None,
    output_true: ListNode | None,
):
    output_calc = lc0876.Solution().middleNode(head=head)
    assert output_calc == output_true
