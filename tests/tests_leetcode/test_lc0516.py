import pytest
from leetcode import lc0516

examples = [
    ("bbbab", 4),
    ("cbbd", 2),
]


@pytest.mark.parametrize("s, output_true", examples)
def test_longestPalindromeSubseq_lcs(s: str, output_true: int):
    output_calc = lc0516.Solution().longestPalindromeSubseq_lcs(s=s)
    assert output_calc == output_true


@pytest.mark.parametrize("s, output_true", examples)
def test_longestPalindromeSubseq_dp(s: str, output_true: int):
    output_calc = lc0516.Solution().longestPalindromeSubseq_dp(s=s)
    assert output_calc == output_true
