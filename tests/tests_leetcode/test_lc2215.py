import pytest
from leetcode import lc2215

examples = [
    ([1, 2, 3], [2, 4, 6], [[1, 3], [4, 6]]),
    ([1, 2, 3, 3], [1, 1, 2, 2], [[3], []]),
]


@pytest.mark.parametrize("nums1, nums2, output_true", examples)
def test_findDifference(
    nums1: list[int], nums2: list[int], output_true: list[list[int]]
):
    output_calc = lc2215.findDifference(nums1=nums1, nums2=nums2)
    assert output_calc == output_true
