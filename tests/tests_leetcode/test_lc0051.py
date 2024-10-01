import pytest

from leetcode import lc0051

examples = [
    (4, [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]),
]


@pytest.mark.parametrize("n, output_true", examples)
def test_solveNQueens(n: int, output_true: list[list[str]]):
    output_calc = lc0051.Solution().solveNQueens(n=n)
    assert len(output_calc) == len(output_true)
    for solution in output_calc:
        assert solution in output_true
