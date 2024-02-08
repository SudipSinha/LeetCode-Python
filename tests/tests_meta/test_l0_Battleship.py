import pytest
from meta import l0_Battleship

examples = [
    (2, 3, [[0, 0, 1], [1, 0, 1]], 0.5),
    (2, 2, [[1, 1], [1, 1]], 1.0),
]


@pytest.mark.parametrize("R, C, G, output_true", examples)
def test_getHitProbability(R: int, C: int, G: list[list[int]], output_true: float):
    output_calc = l0_Battleship.getHitProbability(R=R, C=C, G=G)
    assert abs(output_calc - output_true) < 1e-6
