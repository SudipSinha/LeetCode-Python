import pytest
from leetcode import lc0221

examples = [
    (
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ],
        4,
    ),
    ([["0"]], 0),
]


@pytest.mark.parametrize("matrix, output_true", examples)
def test_maximalSquare_naive(matrix: list[list[str]], output_true: int):
    output_calc = lc0221.maximalSquare_naive(matrix=matrix)
    assert output_calc == output_true


@pytest.mark.parametrize("matrix, output_true", examples)
def test_maximalSquare_dp(matrix: list[list[str]], output_true: int):
    output_calc = lc0221.maximalSquare_dp(matrix=matrix)
    assert output_calc == output_true
