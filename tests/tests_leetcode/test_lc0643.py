import pytest
from leetcode import lc0643

examples = [
    ([1, 12, -5, -6, 50, 3], 4, 12.75),
    ([5], 1, 5.0),
]


@pytest.mark.parametrize("nums, k, output_true", examples)
def test_findMaxAverage_naive(nums: list[int], k: int, output_true: int):
    output_calc = lc0643.Solution().findMaxAverage_naive(nums=nums, k=k)
    assert abs(output_calc - output_true) < 1e-5


@pytest.mark.parametrize("nums, k, output_true", examples)
def test_findMaxAverage_smart(nums: list[int], k: int, output_true: int):
    output_calc = lc0643.Solution().findMaxAverage_sw(nums=nums, k=k)
    assert abs(output_calc - output_true) < 1e-5
