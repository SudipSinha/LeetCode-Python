import pytest

from leetcode import lc1143

examples = [
    ("abcde", "ace", {"length": 3, "subseq": "ace"}),
    ("abc", "abc", {"length": 3, "subseq": "abc"}),
    ("abc", "def", {"length": 0, "subseq": ""}),
    ("", "", {"length": 0, "subseq": ""}),
]


@pytest.mark.parametrize("text1, text2, output_true", examples)
def test_longestCommonSubsequence_first(
    text1: str, text2: str, output_true: lc1143.LCS
):
    output_calc = lc1143.longestCommonSubsequence_first(text1=text1, text2=text2)
    assert output_calc == output_true
