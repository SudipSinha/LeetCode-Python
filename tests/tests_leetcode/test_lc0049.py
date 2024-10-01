import pytest

from leetcode import lc0049

examples = [
    (
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        frozenset(
            {
                frozenset({"tea", "eat", "ate"}),
                frozenset({"bat"}),
                frozenset({"tan", "nat"}),
            }
        ),
    ),
    ([""], frozenset({frozenset({""})})),
    (["a"], frozenset({frozenset({"a"})})),
]


@pytest.mark.parametrize("strs, output_true", examples)
def test_groupAnagrams(strs: list[str], output_true: frozenset[frozenset[str]]):
    output_calc = lc0049.groupAnagrams(strs=strs)
    assert output_calc == output_true
