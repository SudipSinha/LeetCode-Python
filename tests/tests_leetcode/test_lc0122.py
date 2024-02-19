import pytest
from leetcode import lc0122

examples = [
    ([7, 1, 5, 3, 6, 4], 7),
    ([1, 2, 3, 4, 5], 4),
    ([7, 6, 4, 3, 1], 0),
]


@pytest.mark.parametrize("prices, output_true", examples)
def test_maxProfit(prices: list[int], output_true: int):
    output_calc = lc0122.Solution().maxProfit(prices=prices)
    assert output_calc == output_true
