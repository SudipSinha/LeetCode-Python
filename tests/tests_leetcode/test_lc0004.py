import pytest

from leetcode import lc0004

examples = [
    ([1, 3], [2], 2.0),
    ([1, 2], [3, 4], 2.5),
]


@pytest.mark.parametrize("nums1, nums2, output_true", examples)
def test_findMedianSortedArrays_naive(
    nums1: list[int], nums2: list[int], output_true: float
):
    output_calc = lc0004.findMedianSortedArrays_naive(nums1, nums2)
    assert output_calc == output_true
