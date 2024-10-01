import pytest

from leetcode import lc1207

examples = [
    ([1, 2, 2, 1, 1, 3], True),
    ([1, 2], False),
    ([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], True),
]


@pytest.mark.parametrize("arr, output_true", examples)
def test_uniqueOccurrences(arr: list[int], output_true: int):
    output_calc = lc1207.uniqueOccurrences(arr=arr)
    assert output_calc == output_true
