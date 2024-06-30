import pytest
from leetcode import lc1363

examples = [
    ([8, 1, 9], "981"),
    ([8, 6, 7, 1, 0], "8760"),
    ([1], ""),
    ([0, 0, 0, 0, 0, 0], "0"),
    ([9, 8, 6, 8, 6], "966"),
]


@pytest.mark.parametrize("digits, output_true", examples)
def test_maxProfit_naive(digits: list[int], output_true: str):
    output_calc = lc1363.largestMultipleOfThree(digits=digits)
    assert output_calc == output_true
