import pytest
from leetcode import p0002


examples_list = [
    ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
    ([0], [0], [0]),
    ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ([], [], []),
]

examples_linkedlist = [
    tuple(p0002._generate_linkedlist(digits=digits) for digits in example)  # type: ignore
    for example in examples_list
]


@pytest.mark.parametrize("l1, l2, output_true", examples_linkedlist)
def test_twoSum(
    l1: p0002.ListNode | None,
    l2: p0002.ListNode | None,
    output_true: p0002.ListNode | None,
):
    output_calc = p0002.Solution().addTwoNumbers(l1, l2)
    assert output_calc == output_true
