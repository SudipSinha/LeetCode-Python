import pytest
from leetcode import lc0072

examples = [
    ("horse", "ros", 3),
    ("intention", "execution", 5),
]


@pytest.mark.parametrize("word1, word2, output_true", examples)
def test_minDistance_recur(word1: str, word2: str, output_true: int):
    output_calc = lc0072.minDistance_recur(word1=word1, word2=word2)
    assert output_calc == output_true


@pytest.mark.parametrize("word1, word2, output_true", examples)
def test_minDistance_iter(word1: str, word2: str, output_true: int):
    output_calc = lc0072.minDistance_iter(word1=word1, word2=word2)
    assert output_calc == output_true
