import pytest
from leetcode import lc0143

examples_list = [
    ([1, 2, 3, 4], [1, 4, 2, 3]),
    ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
    ([1, 2, 3, 4, 5, 6, 7], [1, 7, 2, 6, 3, 5, 4]),
]

examples_linkedlist = [
    tuple(lc0143.Solution.generate_linkedlist(digits=digits) for digits in example)  # type: ignore
    for example in examples_list
]


def test_ListNode_eq():
    assert lc0143.ListNode() == lc0143.ListNode()
    assert lc0143.ListNode() == lc0143.ListNode(0)
    assert lc0143.ListNode(0) == lc0143.ListNode(0)


@pytest.mark.parametrize("head, output_true", examples_linkedlist)
def test_reorderList(
    head: lc0143.ListNode | None,
    output_true: lc0143.ListNode | None,
):
    lc0143.Solution().reorderList(head=head)
    assert head == output_true
