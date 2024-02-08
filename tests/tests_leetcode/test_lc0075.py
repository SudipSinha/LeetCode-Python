import pytest
from leetcode import lc0075

examples = [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ([0], [0]),
    ([1], [1]),
]


@pytest.mark.parametrize("nums, output_true", examples)
def test_moveZeroes_2ptr_replacement(nums: list[int], output_true: list[int]):
    lc0075.Solution().moveZeroes_2ptr_replacement(nums=nums)
    assert nums == output_true


@pytest.mark.parametrize("nums, output_true", examples)
def test_moveZeroes_2ptr_swap(nums: list[int], output_true: list[int]):
    lc0075.Solution().moveZeroes_2ptr_swap(nums=nums)
    assert nums == output_true
