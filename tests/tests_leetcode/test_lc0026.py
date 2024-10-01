import pytest

from leetcode import lc0026

examples = [
    ([1, 1, 2], 2, [1, 2]),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
]


@pytest.mark.parametrize("nums, output_true, nums_modified", examples)
def test_removeDuplicates(nums: list[int], output_true: int, nums_modified: list[int]):
    output_calc = lc0026.removeDuplicates(nums=nums)
    assert output_calc == output_true
    assert nums[0:output_calc] == nums_modified
