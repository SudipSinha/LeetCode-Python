import pytest
from leetcode import lc1493

examples = [
    ([], 0),
    ([0], 0),
    ([1], 0),
    ([0, 0], 0),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1, 0, 1], 3),
    ([0, 1, 1, 1, 0, 1, 1, 0, 1], 5),
    ([1, 1, 1], 2),
    ([1, 1, 0, 0, 1, 1, 1, 0, 1], 4),
]


@pytest.mark.parametrize("nums, output_true", examples)
def test_longestSubarray_sw(nums: list[int], output_true: int):
    output_calc = lc1493.Solution().longestSubarray_sw(nums=nums)
    assert output_calc == output_true


@pytest.mark.parametrize("nums, output_true", examples)
def test_longestSubarray_alt(nums: list[int], output_true: int):
    output_calc = lc1493.Solution().longestSubarray_alt(nums=nums)
    assert output_calc == output_true
