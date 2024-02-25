import pytest
from leetcode import lc0169

examples = [
    ([3, 2, 3], 3),
    ([2, 2, 1, 1, 1, 2, 2], 2),
]


@pytest.mark.parametrize("nums, output_true", examples)
def test_majorityElement_hashmap(nums: list[int], output_true: int):
    output_calc = lc0169.Solution().majorityElement_hashmap(nums=nums)
    assert output_calc == output_true


@pytest.mark.parametrize("nums, output_true", examples)
def test_majorityElement_Boyer_Moore(nums: list[int], output_true: int):
    output_calc = lc0169.Solution().majorityElement_Boyer_Moore(nums=nums)
    assert output_calc == output_true
