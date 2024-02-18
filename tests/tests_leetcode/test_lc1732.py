import pytest
from leetcode import lc1732

examples = [
    ([-5, 1, 5, 0, -7], 1),
    ([-4, -3, -2, -1, 4, 3, 2], 0),
]


@pytest.mark.parametrize("gain, output_true", examples)
def test_largestAltitude(gain: list[int], output_true: int):
    output_calc = lc1732.Solution().largestAltitude(gain=gain)
    assert output_calc == output_true
