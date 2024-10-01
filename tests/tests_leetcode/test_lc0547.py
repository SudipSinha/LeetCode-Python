import pytest

from leetcode import lc0547

examples = [
    ([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2),
    ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),
]


@pytest.mark.parametrize("isConnected, output_true", examples)
def test_findCircleNum(isConnected: list[list[int]], output_true: int):
    output_calc = lc0547.findCircleNum(isConnected=isConnected)
    assert output_calc == output_true
