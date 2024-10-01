import pytest

from leetcode import lc0062

examples = [
    (3, 7, 28),
    (3, 2, 3),
]


@pytest.mark.parametrize("m, n, output_true", examples)
def test_uniquePaths_math(m: int, n: int, output_true: int):
    output_calc = lc0062.uniquePaths_math(m=m, n=n)
    assert output_calc == output_true


@pytest.mark.parametrize("m, n, output_true", examples)
def test_uniquePaths_dp(m: int, n: int, output_true: int):
    output_calc = lc0062.uniquePaths_dp(m=m, n=n)
    assert output_calc == output_true
