import pytest

from leetcode import lc0078

examples_list = [
    ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
    ([0], [[], [0]]),
]
examples_set = [
    (set(nums), set(frozenset(subset) for subset in subsets))  # type: ignore
    for (nums, subsets) in examples_list
]


@pytest.mark.parametrize("nums, output_true", examples_set)
def test_subsets(nums: set[int], output_true: set[frozenset[int]]):
    output_calc = lc0078.subsets(nums=nums)
    assert output_calc == output_true
