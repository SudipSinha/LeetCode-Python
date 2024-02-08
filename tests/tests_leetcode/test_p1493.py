import pytest
from leetcode import p1493


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
    output_calc = p1493.Solution().longestSubarray(nums=nums)
    assert output_calc == output_true
