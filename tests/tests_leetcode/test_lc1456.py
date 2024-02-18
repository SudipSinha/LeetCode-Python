import pytest
from leetcode import lc1456

examples = [
    ("abciiidef", 3, 3),
    ("aeiou", 2, 2),
    ("leetcode", 3, 2),
]


@pytest.mark.parametrize("s, k, output_true", examples)
def test_maxVowels_sw(s: str, k: int, output_true: int):
    output_calc = lc1456.Solution().maxVowels_sw(s=s, k=k)
    assert output_calc == output_true
