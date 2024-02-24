import pytest
from leetcode import lc0002

examples_list = [
    ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
    ([0], [0], [0]),
    ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ([], [], []),
]

examples_linkedlist = [
    tuple(lc0002.generate_linkedlist(digits=digits) for digits in example)  # type: ignore
    for example in examples_list
]


def test_ListNode_eq():
    assert lc0002.ListNode() == lc0002.ListNode()
    assert lc0002.ListNode() == lc0002.ListNode(0)
    assert lc0002.ListNode(0) == lc0002.ListNode(0)


@pytest.mark.parametrize("l1, l2, output_true", examples_linkedlist)
def test_twoSum(
    l1: lc0002.ListNode | None,
    l2: lc0002.ListNode | None,
    output_true: lc0002.ListNode | None,
):
    output_calc = lc0002.Solution().addTwoNumbers(l1, l2)
    assert output_calc == output_true
