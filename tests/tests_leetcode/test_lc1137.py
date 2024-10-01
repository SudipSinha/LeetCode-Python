import pytest

from leetcode import lc1137

examples = [
    (4, 4),
    (25, 1389537),
]


@pytest.mark.parametrize("n, output_true", examples)
def test_tribonacci_hashmap(n: int, output_true: int):
    output_calc = lc1137.tribonacci_hashmap(n=n)
    assert output_calc == output_true


@pytest.mark.parametrize("n, output_true", examples)
def test_tribonacci_iter(n: int, output_true: int):
    output_calc = lc1137.tribonacci_iter(n=n)
    assert output_calc == output_true
