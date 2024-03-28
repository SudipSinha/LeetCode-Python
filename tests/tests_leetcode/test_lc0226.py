import pytest
from datastructures.binarytree import BinaryTreeNode
from leetcode import lc0226

examples = [
    ([2, 1, 3], [2, 3, 1]),
    ([], []),
    ([1], [1]),
]


@pytest.mark.parametrize("tree_list, output_true_list", examples)
def test_invertTree(tree_list: list[int | None], output_true_list: list[int | None]):
    tree = BinaryTreeNode.from_list_long_iter(
        BinaryTreeNode.transform_short_to_long(short=tree_list)
    )
    output_true = BinaryTreeNode.from_list_long_iter(
        BinaryTreeNode.transform_short_to_long(short=output_true_list)
    )
    output_calc = lc0226.invertTree(root=tree) if tree else None
    assert output_calc == output_true
