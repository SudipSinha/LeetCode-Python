import pytest

from leetcode import lc0216

examples = [
    (3, 7, [[1, 2, 4]]),
    (3, 9, [[1, 2, 6], [1, 3, 5], [2, 3, 4]]),
    (4, 1, []),
]


@pytest.mark.parametrize("k, n, output_true", examples)
def test_combinationSum3(k: int, n: int, output_true: str):
    output_calc = lc0216.combinationSum3(k=k, n=n)
    assert output_calc == output_true
