import pytest

from leetcode import lc0017

examples = [
    ("23", {"ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"}),
    ("", set()),
    ("2", {"a", "b", "c"}),
]


@pytest.mark.parametrize("digits, output_true", examples)
def test_letterCombinations(digits: str, output_true: set[str]):
    output_calc = lc0017.letterCombinations(digits=digits)
    assert output_calc == output_true
