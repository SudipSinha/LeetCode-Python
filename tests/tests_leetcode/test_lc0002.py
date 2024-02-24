import pytest
from leetcode import lc0002
from leetcode.lc0002 import ListNode

examples_list = [
    ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
    ([0], [0], [0]),
    ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ([], [], []),
]


def generate_linkedlist(digits: list[int]) -> ListNode | None:
    ll_dummyhead = ptr_ll = ListNode()  # Trash ListNode
    for d in digits:
        ptr_ll.next = ListNode(val=d)
        ptr_ll = ptr_ll.next
    return ll_dummyhead.next


examples_linkedlist = [
    tuple(generate_linkedlist(digits=digits) for digits in example)  # type: ignore
    for example in examples_list
]


def test_ListNode_eq():
    assert ListNode() == ListNode()
    assert ListNode() == ListNode(0)
    assert ListNode(0) == ListNode(0)


@pytest.mark.parametrize("l1, l2, output_true", examples_linkedlist)
def test_twoSum(
    l1: ListNode | None,
    l2: ListNode | None,
    output_true: ListNode | None,
):
    output_calc = lc0002.Solution().addTwoNumbers(l1, l2)
    assert output_calc == output_true
