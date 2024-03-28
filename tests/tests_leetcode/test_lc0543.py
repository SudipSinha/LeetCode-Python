import pytest
from datastructures.binarytree import BinaryTreeNode
from leetcode import lc0543

examples = [
    ([1, 2, 3, 4, 5], 3),
    ([1, 2], 1),
]


@pytest.mark.parametrize("tree_list, output_true", examples)
def test_diameterOfBinaryTree(tree_list: list[int | None], output_true: int):
    tree = BinaryTreeNode.from_list_long_iter(
        BinaryTreeNode.transform_short_to_long(short=tree_list)
    )
    output_calc = lc0543.diameterOfBinaryTree(root=tree)
    assert output_calc == output_true
