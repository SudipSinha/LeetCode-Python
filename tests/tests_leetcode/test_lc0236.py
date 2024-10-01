import pytest

from datastructures.binarytree import BinaryTreeNode
from leetcode import lc0236

examples = [
    ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3),
    ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5),
    ([1, 2], 1, 2, 1),
]


@pytest.mark.parametrize("tree_list, p, q, output_true", examples)
def test_lowestCommonAncestor(
    tree_list: list[int | None], p: int, q: int, output_true: int
):
    tree = BinaryTreeNode.from_list_long_iter(
        BinaryTreeNode.transform_short_to_long(short=tree_list)
    )
    output_calc = lc0236.lowestCommonAncestor(root=tree, p=p, q=q)
    assert output_calc == output_true
