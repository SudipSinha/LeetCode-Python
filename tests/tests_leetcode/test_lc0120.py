import pytest

from leetcode import lc0120

examples = [
    ([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], 11),
    ([[-10]], -10),
]


@pytest.mark.parametrize("triangle, output_true", examples)
def test_minimumTotal_recur_inner(triangle: list[list[int]], output_true: int):
    output_calc = lc0120.minimumTotal_recur_inner(triangle=triangle)
    assert output_calc == output_true


@pytest.mark.parametrize("triangle, output_true", examples)
def test_minimumTotal_recur_1fn(triangle: list[list[int]], output_true: int):
    triangle_tuple = tuple([tuple([item for item in row]) for row in triangle])
    output_calc = lc0120.minimumTotal_recur_1fn(triangle=triangle_tuple)
    assert output_calc == output_true


@pytest.mark.parametrize("triangle, output_true", examples)
def test_minimumTotal_iter(triangle: list[list[int]], output_true: int):
    output_calc = lc0120.minimumTotal_iter(triangle=triangle)
    assert output_calc == output_true
