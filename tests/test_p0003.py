import pytest
from leetcode import p0003


examples = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
]


@pytest.mark.parametrize("s, output_true", examples)
def test_lengthOfLongestSubstring_naive(s: str, output_true: int):
    output_calc = p0003.Solution().lengthOfLongestSubstring_naive(s)
    assert output_calc == output_true


@pytest.mark.parametrize("s, output_true", examples)
def test_lengthOfLongestSubstring_hashmap(s: str, output_true: int):
    output_calc = p0003.Solution().lengthOfLongestSubstring_hashmap(s)
    assert output_calc == output_true


@pytest.mark.parametrize("s, output_true", examples)
def test_lengthOfLongestSubstring_slidingwindow(s: str, output_true: int):
    output_calc = p0003.Solution().lengthOfLongestSubstring_slidingwindow(s)
    assert output_calc == output_true
