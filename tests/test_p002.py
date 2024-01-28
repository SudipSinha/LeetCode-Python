import pytest
from leetcode import p002


examples_list = [
    ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
    ([0], [0], [0]),
    ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ([], [], []),
]
examples_linkedlist = [
    tuple(p002._generate_linkedlist(digits) for digits in example)
    for example in examples_list
]


@pytest.mark.parametrize("l1, l2, output_true", examples_linkedlist)
def test_twoSum_naive(
    l1: p002.ListNode | None,
    l2: p002.ListNode | None,
    output_true: p002.ListNode | None,
):
    output_calc = p002.Solution().addTwoNumbers(l1, l2)
    assert output_calc == output_true


# @pytest.mark.parametrize("l1, l2, output_true", examples_linkedlist)
# def test_twoSum_hashmap_2pass(nums: list[int], target: int, output_true: set[int]):
#     output_calc = p001.Solution().twoSum_hashmap_2pass(nums, target)
#     assert output_calc == output_true


# @pytest.mark.parametrize("l1, l2, output_true", examples_linkedlist)
# def test_twoSum_hashmap_1pass(nums: list[int], target: int, output_true: set[int]):
#     output_calc = p001.Solution().twoSum_hashmap_1pass(nums, target)
#     assert output_calc == output_true
