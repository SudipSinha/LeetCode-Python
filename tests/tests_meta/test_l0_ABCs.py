import pytest
from meta import l0_ABCs

examples = [
    (1, 2, 3, 6),
    (100, 100, 100, 300),
    (85, 16, 93, 194),
]


@pytest.mark.parametrize("A, B, C, output_true", examples)
def test_getSum(A: int, B: int, C: int, output_true: float):
    output_calc = l0_ABCs.getSum(A=A, B=B, C=C)
    assert output_calc == output_true
