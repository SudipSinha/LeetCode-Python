import pytest

from leetcode import lc2390

examples = [
    ("leet**cod*e", "lecoe"),
    ("erase*****", ""),
]


@pytest.mark.parametrize("s, output_true", examples)
def test_twoSum_naive(s: str, output_true: str):
    output_calc = lc2390.removeStars(s=s)
    assert output_calc == output_true
