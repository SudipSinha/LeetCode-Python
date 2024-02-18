import pytest
from leetcode import lc0172

examples = [
    (0, 0),
    (3, 0),
    (5, 1),
]


@pytest.mark.parametrize("n, output_true", examples)
def test_trailingZeroes(n: int, output_true: int):
    output_calc = lc0172.Solution().trailingZeroes(n=n)
    assert output_calc == output_true
