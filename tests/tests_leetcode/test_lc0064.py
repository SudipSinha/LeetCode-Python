import pytest
from leetcode import lc0064

examples = [
    ([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7),
    ([[1, 2, 3], [4, 5, 6]], 12),
]


@pytest.mark.parametrize("grid, output_true", examples)
def test_minPathSum(grid: list[list[int]], output_true: int):
    output_calc = lc0064.minPathSum(grid=grid)
    assert output_calc == output_true
