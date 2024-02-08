import pytest
from leetcode import p0392

examples = [
    ("abc", "ahbgdc", True),
    ("axc", "ahbgdc", False),
]

@pytest.mark.parametrize("s, t, output_true", examples)
def test_isSubsequence(s: str, t: str, output_true: bool):
    output_calc = p0392.Solution().isSubsequence(s=s, t=t)
    assert output_calc == output_true
