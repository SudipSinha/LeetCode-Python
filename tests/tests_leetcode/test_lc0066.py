import pytest

from leetcode import lc0066

examples = [
    ([1, 2, 3], [1, 2, 4]),
    ([4, 3, 2, 1], [4, 3, 2, 2]),
    ([9], [1, 0]),
]


@pytest.mark.parametrize("digits, output_true", examples)
def test_plusOne(digits: list[int], output_true: list[int]):
    output_calc = lc0066.plusOne(digits=digits)
    assert output_calc == output_true
