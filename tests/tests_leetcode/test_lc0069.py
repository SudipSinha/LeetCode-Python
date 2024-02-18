import pytest
from leetcode import lc0069

examples = [
    (0, 0),
    (1, 1),
    (4, 2),
    (8, 2),
]


@pytest.mark.parametrize("x, output_true", examples)
def test_mySqrt_naive(x: int, output_true: int):
    output_calc = lc0069.Solution().mySqrt_naive(x=x)
    assert output_calc == output_true


@pytest.mark.parametrize("x, output_true", examples)
def test_mySqrt_binarysearch(x: int, output_true: int):
    output_calc = lc0069.Solution().mySqrt_binarysearch(x=x)
    assert output_calc == output_true
