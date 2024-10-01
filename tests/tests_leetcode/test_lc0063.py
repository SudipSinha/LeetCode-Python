import pytest

from leetcode import lc0063

examples = [
    ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2),
    ([[0, 1], [0, 0]], 1),
]


@pytest.mark.parametrize("obstacleGrid, output_true", examples)
def test_uniquePathsWithObstacles(obstacleGrid: list[list[int]], output_true: int):
    output_calc = lc0063.uniquePathsWithObstacles(obstacleGrid=obstacleGrid)
    assert output_calc == output_true
