import pytest
from leetcode import lc0011

examples = [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1),
]


@pytest.mark.parametrize("height, output_true", examples)
def test_maxArea_naive(height: list[int], output_true: int):
    output_calc = lc0011.Solution().maxArea_naive(height=height)
    assert output_calc == output_true


@pytest.mark.parametrize("height, output_true", examples)
def test_maxArea_2ptr(height: list[int], output_true: int):
    output_calc = lc0011.Solution().maxArea_2ptr(height=height)
    assert output_calc == output_true
