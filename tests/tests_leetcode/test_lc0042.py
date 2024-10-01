import pytest

from leetcode import lc0042

examples = [
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ([4, 2, 0, 3, 2, 5], 9),
]


@pytest.mark.parametrize("height, output_true", examples)
def test_trap_arrays(height: list[int], output_true: int):
    output_calc = lc0042.trap_arrays(height=height)
    assert output_calc == output_true


@pytest.mark.parametrize("height, output_true", examples)
def test_trap_2ptr(height: list[int], output_true: int):
    output_calc = lc0042.trap_2ptr(height=height)
    assert output_calc == output_true
