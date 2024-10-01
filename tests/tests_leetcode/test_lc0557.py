import pytest

from leetcode import lc0557

examples = [
    ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
    ("Mr Ding", "rM gniD"),
]


@pytest.mark.parametrize("s, output_true", examples)
def test_reverseWords(s: str, output_true: str):
    output_calc = lc0557.reverseWords(s)
    assert output_calc == output_true
