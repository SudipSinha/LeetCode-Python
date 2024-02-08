import pytest
from leetcode import lc0392

examples = [
    ("abc", "ahbgdc", True),
    ("axc", "ahbgdc", False),
]


@pytest.mark.parametrize("s, t, output_true", examples)
def test_isSubsequence_simple(s: str, t: str, output_true: bool):
    output_calc = lc0392.Solution().isSubsequence_simple(s=s, t=t)
    assert output_calc == output_true

@pytest.mark.parametrize("s, t, output_true", examples)
def test_isSubsequence_dp(s: str, t: str, output_true: bool):
    output_calc = lc0392.Solution().isSubsequence_dp(s=s, t=t)
    assert output_calc == output_true
