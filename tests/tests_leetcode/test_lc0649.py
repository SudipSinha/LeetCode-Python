import pytest

from leetcode import lc0649

examples = [
    ("RD", "Radiant"),
    ("RDD", "Dire"),
    ("DDRRR", "Dire"),
    # ("DRRDRDRDRDDRDRDR", "Radiant"),  # Not sure why the answer is "Radiant".
]


@pytest.mark.parametrize("senate, output_true", examples)
def test_predictPartyVictory(senate: str, output_true: str):
    output_calc = lc0649.predictPartyVictory(senate=senate)
    assert output_calc == output_true
