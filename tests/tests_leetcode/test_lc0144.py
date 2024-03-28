import pytest
from datastructures.binarytree import BinaryTreeNode
from leetcode import lc0144

examples = [
    ([1, None, 2, 3], [1, 2, 3]),
    ([], []),
    ([1], [1]),
]


@pytest.mark.parametrize("tree_list, output_true", examples)
def test_preorderTraversal_recur(tree_list: list[int | None], output_true: list[int]):
    tree = BinaryTreeNode.from_list_long_iter(
        BinaryTreeNode.transform_short_to_long(short=tree_list)
    )
    output_calc = lc0144.preorderTraversal_recur(root=tree)
    assert output_calc == output_true
