import pytest

from leetcode import lc0056

examples = [
    ([(1, 3), (2, 6), (8, 10), (15, 18)], [(1, 6), (8, 10), (15, 18)]),
    ([(1, 4), (4, 5)], [(1, 5)]),
]


@pytest.mark.parametrize("intervals, output_true", examples)
def test_merge(intervals: list[tuple[int, int]], output_true: list[tuple[int, int]]):
    output_calc = lc0056.merge(intervals=intervals)
    assert output_calc == output_true
