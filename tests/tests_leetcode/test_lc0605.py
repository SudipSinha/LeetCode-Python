import pytest

from leetcode import lc0605

examples = [
    ([1, 0, 0, 0, 1], 1, True),
    ([1, 0, 0, 0, 1], 2, False),
]


@pytest.mark.parametrize("flowerbed, n, output_true", examples)
def test_canPlaceFlowers_naive(flowerbed: list[int], n: int, output_true: bool):
    output_calc = lc0605.canPlaceFlowers_naive(flowerbed=flowerbed, n=n)
    assert output_calc == output_true


@pytest.mark.parametrize("flowerbed, n, output_true", examples)
def test_canPlaceFlowers_string(flowerbed: list[int], n: int, output_true: bool):
    output_calc = lc0605.canPlaceFlowers_string(flowerbed=flowerbed, n=n)
    assert output_calc == output_true
