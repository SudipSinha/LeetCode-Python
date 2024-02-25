import pytest
from leetcode import lc0300

examples = [
    ([10, 9, 2, 5, 3, 7, 101, 18], {"length": 4, "subseq": [2, 5, 7, 101]}),
    ([0, 1, 0, 3, 2, 3], {"length": 4, "subseq": [0, 1, 2, 3]}),
    ([7, 7, 7, 7, 7, 7, 7], {"length": 1, "subseq": [7]}),
]


@pytest.mark.parametrize("nums, output_true", examples)
def test_lengthOfLIS_dp(nums: list[int], output_true: lc0300.LIS):
    output_calc = lc0300.Solution().lengthOfLIS_dp(nums=nums)
    assert output_calc == output_true
