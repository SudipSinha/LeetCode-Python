import pytest
from leetcode import lc0001

examples = [
    ([2, 7, 11, 15], 9, {0, 1}),
    ([3, 2, 4], 6, {1, 2}),
    ([3, 3], 6, {0, 1}),
    ([3, 3], 5, set()),
]


@pytest.mark.parametrize("nums, target, output_true", examples)
def test_twoSum_naive(nums: list[int], target: int, output_true: set[int]):
    output_calc = lc0001.Solution().twoSum_naive(nums, target)
    assert output_calc == output_true


@pytest.mark.parametrize("nums, target, output_true", examples)
def test_twoSum_hashmap_2pass(nums: list[int], target: int, output_true: set[int]):
    output_calc = lc0001.Solution().twoSum_hashmap_2pass(nums, target)
    assert output_calc == output_true


@pytest.mark.parametrize("nums, target, output_true", examples)
def test_twoSum_hashmap_1pass(nums: list[int], target: int, output_true: set[int]):
    output_calc = lc0001.Solution().twoSum_hashmap_1pass(nums, target)
    assert output_calc == output_true
