import pytest
from leetcode import lc0121

examples = [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
]


@pytest.mark.parametrize("prices, output_true", examples)
def test_maxProfit_naive(prices: list[int], output_true: int):
    output_calc = lc0121.Solution().maxProfit_naive(prices=prices)
    assert output_calc == output_true


@pytest.mark.parametrize("prices, output_true", examples)
def test_maxProfit_2ptr(prices: list[int], output_true: int):
    output_calc = lc0121.Solution().maxProfit_2ptr(prices=prices)
    assert output_calc == output_true
