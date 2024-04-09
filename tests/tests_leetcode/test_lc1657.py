import pytest
from leetcode import lc1657

examples = [
    ("abc", "bca", True),
    ("a", "aa", False),
    ("cabbba", "abbccc", True),
]


@pytest.mark.parametrize("word1, word2, output_true", examples)
def test_closeStrings(word1: str, word2: str, output_true: int):
    output_calc = lc1657.closeStrings(word1=word1, word2=word2)
    assert output_calc == output_true
