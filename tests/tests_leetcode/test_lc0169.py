import pytest
from leetcode import lc0169

examples = [
    ([3, 2, 3], 3),
    ([2, 2, 1, 1, 1, 2, 2], 2),
]


@pytest.mark.parametrize("nums, output_true", examples)
def test_majorityElement(nums: list[int], output_true: int):
    output_calc = lc0169.Solution().majorityElement(nums=nums)
    assert output_calc == output_true
