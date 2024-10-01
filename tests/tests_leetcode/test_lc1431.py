import pytest

from leetcode import lc1431

examples = [
    ([2, 3, 5, 1, 3], 3, [True, True, True, False, True]),
    ([4, 2, 1, 1, 2], 1, [True, False, False, False, False]),
    ([12, 1, 12], 10, [True, False, True]),
]


@pytest.mark.parametrize("candies, extraCandies, output_True", examples)
def test_kidsWithCandies(
    candies: list[int], extraCandies: int, output_True: list[bool]
):
    output_calc = lc1431.kidsWithCandies(candies, extraCandies)
    assert output_calc == output_True
