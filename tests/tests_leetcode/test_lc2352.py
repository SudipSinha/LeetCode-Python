import pytest

from leetcode import lc2352

examples = [
    ([[3, 2, 1], [1, 7, 6], [2, 7, 7]], 1),
    ([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]], 3),
]


@pytest.mark.parametrize("grid, output_true", examples)
def test_equalPairs_naive(grid: list[list[int]], output_true: int):
    output_calc = lc2352.equalPairs_naive(grid=grid)
    assert output_calc == output_true


@pytest.mark.parametrize("grid, output_true", examples)
def test_equalPairs_conjugate(grid: list[list[int]], output_true: int):
    output_calc = lc2352.equalPairs_conjugate(grid=grid)
    assert output_calc == output_true
