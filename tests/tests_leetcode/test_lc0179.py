import pytest

from leetcode import lc0179

examples = [
    ([10, 2], "210"),
    ([3, 30, 34, 5, 9], "9534330"),
    ([111311, 1113], "1113111311"),
    ([3, 30, 34, 5, 9], "9534330"),
]


@pytest.mark.parametrize("nums, output_true", examples)
def test_largestNumber(nums: list[int], output_true: str):
    output_calc = lc0179.largestNumber(nums=nums)
    assert output_calc == output_true
