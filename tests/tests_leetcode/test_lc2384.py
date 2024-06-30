import pytest
from leetcode import lc2384

examples = [
    ("444947137", "7449447"),
    ("00009", "9"),
    ("000", "0"),
    ("", ""),
]


@pytest.mark.parametrize("num, output_true", examples)
def test_largestPalindromic(num: str, output_true: str):
    output_calc = lc2384.largestPalindromic(num=num)
    assert output_calc == output_true
