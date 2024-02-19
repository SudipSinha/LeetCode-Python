import pytest
from leetcode import lc0322

examples = [
    ([1, 2, 5], 11, 3),
    ([2], 3, -1),
    ([1], 0, 0),
]


@pytest.mark.parametrize("coins, amount, output_true", examples)
def test_coinChange_dp(coins: list[int], amount: int, output_true: int):
    output_calc = lc0322.Solution().coinChange_dp(coins=coins, amount=amount)
    assert output_calc == output_true


@pytest.mark.parametrize("coins, amount, output_true", examples)
def test_coinChange_bfs(coins: list[int], amount: int, output_true: int):
    output_calc = lc0322.Solution().coinChange_bfs(coins=coins, amount=amount)
    assert output_calc == output_true
