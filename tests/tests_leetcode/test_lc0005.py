import pytest

from leetcode import lc0005

examples = [
    ("babad", {"length": 3, "substrs": {"bab", "aba"}}),
    ("cbbd", {"length": 2, "substrs": {"bb"}}),
    ("ccc", {"length": 3, "substrs": {"ccc"}}),
    ("bb", {"length": 2, "substrs": {"bb"}}),
    ("a", {"length": 1, "substrs": {"a"}}),
]


@pytest.mark.parametrize("s, output_true", examples)
def test_longestPalindrome_naive(s: str, output_true: lc0005.LP):
    output_calc = lc0005.longestPalindrome_naive(s=s)
    assert output_calc == output_true


@pytest.mark.parametrize("s, output_true", examples)
def test_longestPalindrome_centerout(s: str, output_true: lc0005.LP):
    output_calc = lc0005.longestPalindrome_centerout(s=s)
    assert output_calc == output_true


@pytest.mark.parametrize("s, output_true", examples)
def test_longestPalindrome_dp(s: str, output_true: lc0005.LP):
    output_calc = lc0005.longestPalindrome_dp(s=s)
    assert output_calc == output_true
