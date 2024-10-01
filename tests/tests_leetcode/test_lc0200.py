import pytest

from leetcode import lc0200

examples = [
    (
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ],
        1,
    ),
    (
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ],
        3,
    ),
]


@pytest.mark.parametrize("grid, output_true", examples)
def test_numIslands_dfs(grid: list[list[str]], output_true: int):
    output_calc = lc0200.numIslands(grid=grid, method="DFS")
    assert output_calc == output_true


@pytest.mark.parametrize("grid, output_true", examples)
def test_numIslands_bfs(grid: list[list[str]], output_true: int):
    output_calc = lc0200.numIslands(grid=grid, method="BFS")
    assert output_calc == output_true
