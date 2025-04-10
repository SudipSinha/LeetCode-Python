import pytest

from leetcode import lc0509

examples = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
]


@pytest.mark.parametrize("n, output_true", examples)
def test_fib_iter(n: int, output_true: int):
    output_calc = lc0509.fib_iter(n)
    assert output_calc == output_true


@pytest.mark.parametrize("n, output_true", examples)
def test_fib_goldenratio(n: int, output_true: int):
    output_calc = lc0509.fib_goldenratio(n)
    assert output_calc == output_true


@pytest.mark.parametrize("n, output_true", examples)
def test_fib_dp_list(n: int, output_true: int):
    output_calc = lc0509.fib_dp_list(n)
    assert output_calc == output_true


@pytest.mark.parametrize("n, output_true", examples)
def test_fib_dp_dict(n: int, output_true: int):
    output_calc = lc0509.fib_dp_dict(n)
    assert output_calc == output_true


@pytest.mark.parametrize("n, output_true", examples)
def test_fib_dp_cache(n: int, output_true: int):
    output_calc = lc0509.fib_dp_cache(n)
    assert output_calc == output_true
