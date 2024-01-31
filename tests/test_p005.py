import pytest
from leetcode import p005


examples = [
    ("babad", "bab"),
    ("cbbd", "bb"),
    ("bb", "bb"),
    ("a", "a"),
]


@pytest.mark.parametrize("input, output_true", examples)
def test_longestPalindrome_naive(input: str, output_true: str):
    output_calc = p005.Solution().longestPalindrome_naive(input)
    assert output_calc == output_true
