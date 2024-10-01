import pytest

from meta import l0_AllWrong

examples = [
    (3, "ABA", "BAB"),
    (5, "BBBBB", "AAAAA"),
]


@pytest.mark.parametrize("N, C, output_true", examples)
def test_getSum(N: int, C: str, output_true: str):
    output_calc = l0_AllWrong.getWrongAnswers(N=N, C=C)
    assert output_calc == output_true
