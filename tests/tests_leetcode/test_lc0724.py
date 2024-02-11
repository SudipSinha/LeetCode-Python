import pytest
from leetcode import lc0724

examples = [
    ([1, 7, 3, 6, 5, 6], 3),
    ([1, 2, 3], -1),
    ([2, 1, -1], 0),
]


@pytest.mark.parametrize("nums, output_true", examples)
def test_maxArea_naive(nums: list[int], output_true: int):
    output_calc = lc0724.Solution().pivotIndex(nums=nums)
    assert output_calc == output_true
