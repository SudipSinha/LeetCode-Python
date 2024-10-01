import pytest

from leetcode import lc1071

examples = [
    ("ABCABC", "ABC", "ABC"),
    ("ABABAB", "ABAB", "AB"),
    ("LEET", "CODE", ""),
]


@pytest.mark.parametrize("str1, str2, output_true", examples)
def test_gcdOfStrings(str1: str, str2: str, output_true: str):
    output_calc = lc1071.gcdOfStrings(str1=str1, str2=str2)
    assert output_calc == output_true
