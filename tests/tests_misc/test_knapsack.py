import pytest

from misc import knapsack

examples = [
    ([7, 9, 5, 12, 14, 6, 12], [3, 4, 2, 6, 7, 3, 5], 15, {1, 2, 6, 7}),
]


@pytest.mark.parametrize("values, weights, weight__max, output_true", examples)
def test_findMedianSortedArrays_naive(
    values: list[float], weights: list[float], weight__max: float, output_true: set[int]
):
    output_calc = knapsack.zero_one_knapsack(values, weights, weight__max)
    assert output_calc == output_true
