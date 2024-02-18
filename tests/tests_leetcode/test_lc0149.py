import pytest
from leetcode import lc0149

examples = [
    ([[1, 1], [2, 2], [3, 3]], 3),
    ([(1, 1), (3, 2), (5, 3), (4, 1), (2, 3), (1, 4)], 4),
    ([[4, 5], [4, -1], [4, 0]], 3),
]


@pytest.mark.parametrize("points, output_true", examples)
def test_maxPoints_line_2d(points: list[tuple[int, int]], output_true: int):
    output_calc = lc0149.Solution().maxPoints_line_2d(points=points)
    assert output_calc == output_true
