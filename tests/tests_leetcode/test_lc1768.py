import pytest

from leetcode import lc1768

examples = [
    ("abc", "pqr", "apbqcr"),
    ("ab", "pqrs", "apbqrs"),
    ("abcd", "pq", "apbqcd"),
]


@pytest.mark.parametrize("word1, word2, output_true", examples)
def test_mergeAlternately(word1: str, word2: str, output_true: str):
    output_calc = lc1768.mergeAlternately(word1=word1, word2=word2)
    assert output_calc == output_true
