import pytest

from leetcode import lc1004

examples = [
    ([], 0, 0),
    ([], 1, 0),
    ([0], 1, 1),
    ([1], 1, 1),
    ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6),
    ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3, 10),
]


@pytest.mark.parametrize("nums, k, output_true", examples)
def test_longestOnes_sw(nums: list[int], k: int, output_true: int):
    output_calc = lc1004.longestOnes_sw(nums=nums, k=k)
    assert output_calc == output_true
