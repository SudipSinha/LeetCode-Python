import pytest
from leetcode import lc0841

examples = [
    ([[1], [2], [3], []], True),
    ([[1, 3], [3, 0, 1], [2], [0]], False),
]


@pytest.mark.parametrize("rooms, output_true", examples)
def test_canVisitAllRooms(rooms: list[list[int]], output_true: bool):
    output_calc = lc0841.canVisitAllRooms(rooms=rooms)
    assert output_calc == output_true
