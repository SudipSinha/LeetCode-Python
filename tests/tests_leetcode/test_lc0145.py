import pytest
from datastructures.binarytree import BinaryTreeNode
from leetcode import lc0145

examples = [
    ([1, None, 2, 3], [3, 2, 1]),
    ([], []),
    ([1], [1]),
]


@pytest.mark.parametrize("tree_list, output_true", examples)
def test_postorderTraversal_recur(tree_list: list[int | None], output_true: list[int]):
    tree = BinaryTreeNode.from_list_long_iter(
        BinaryTreeNode.transform_short_to_long(short=tree_list)
    )
    output_calc = lc0145.postorderTraversal_recur(root=tree)
    assert output_calc == output_true
