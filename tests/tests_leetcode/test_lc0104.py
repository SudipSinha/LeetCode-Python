import pytest

from datastructures.binarytree import BinaryTreeNode
from leetcode import lc0104

examples = [
    ([3, 9, 20, None, None, 15, 7], 3),
    ([1, None, 2], 2),
    ([], 0),
]


@pytest.mark.parametrize("tree_list, output_true", examples)
def test_maxDepth(tree_list: list[int | None], output_true: int):
    tree = BinaryTreeNode.from_list_long_iter(
        BinaryTreeNode.transform_short_to_long(short=tree_list)
    )
    output_calc = lc0104.maxDepth(root=tree)
    assert output_calc == output_true
