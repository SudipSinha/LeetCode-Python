import pytest

from leetcode import lc0151

examples = [
    ("the sky is blue", "blue is sky the"),
    ("  hello world  ", "world hello"),
    ("a good   example", "example good a"),
]


@pytest.mark.parametrize("s, output_true", examples)
def test_reverseWords(s: str, output_true: str):
    output_calc = lc0151.reverseWords(s=s)
    assert output_calc == output_true
