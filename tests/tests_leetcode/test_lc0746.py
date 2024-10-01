import pytest

from leetcode import lc0746

examples = [
    ([10, 15, 20], 15),
    ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
]


@pytest.mark.parametrize("cost, output_true", examples)
def test_minCostClimbingStairs_cache(cost: list[int], output_true: int):
    output_calc = lc0746.minCostClimbingStairs_cache(cost=cost)
    assert output_calc == output_true


@pytest.mark.parametrize("cost, output_true", examples)
def test_minCostClimbingStairs_array(cost: list[int], output_true: int):
    output_calc = lc0746.minCostClimbingStairs_array(cost=cost)
    assert output_calc == output_true
