import pytest
from leetcode import lc0695

examples = [
    (
        [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ],
        6,
    ),
    ([[0, 0, 0, 0, 0, 0, 0, 0]], 0),
    ([[1, 0], [0, 0]], 1),
    ([[1, 1], [1, 0]], 3),
]


@pytest.mark.parametrize("grid, output_true", examples)
def test_numIslands_dfs(grid: list[list[int]], output_true: int):
    output_calc = lc0695.maxAreaOfIsland(grid=grid)
    assert output_calc == output_true
