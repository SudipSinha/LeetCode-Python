import pytest

from leetcode import lc2000

examples = [
    ("abcdefd", "d", "dcbaefd"),
    ("xyxzxe", "z", "zxyxxe"),
    ("abcd", "z", "abcd"),
]


@pytest.mark.parametrize("word, ch, output_true", examples)
def test_removeDuplicates_naive(word: str, ch: str, output_true: str):
    output_calc = lc2000.reversePrefix_naive(word=word, ch=ch)
    assert output_calc == output_true


@pytest.mark.parametrize("word, ch, output_true", examples)
def test_removeDuplicates_deque(word: str, ch: str, output_true: str):
    output_calc = lc2000.reversePrefix_deque(word=word, ch=ch)
    assert output_calc == output_true
