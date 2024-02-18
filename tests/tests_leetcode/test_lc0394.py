import pytest
from leetcode import lc0394

examples = [
    ("3[a]2[bc]", "aaabcbc"),
    ("3[a2[c]]", "accaccacc"),
    ("2[abc]3[cd]ef", "abcabccdcdcdef"),
]


@pytest.mark.parametrize("s, output_true", examples)
def test_decodeString_1pass(s: str, output_true: str):
    output_calc = lc0394.Solution().decodeString_1pass(s=s)
    assert output_calc == output_true


@pytest.mark.parametrize("s, output_true", examples)
def test_decodeString_backandforth(s: str, output_true: str):
    output_calc = lc0394.Solution().decodeString_backandforth(s=s)
    assert output_calc == output_true


@pytest.mark.parametrize("s, output_true", examples)
def test_decodeString_recursive(s: str, output_true: str):
    output_calc = lc0394.Solution().decodeString_recursive(s=s)
    assert output_calc == output_true
