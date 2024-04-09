import pytest
from datastructures.binarytree import BinaryTreeNode
from leetcode import lc0700

examples = [
    ([4, 2, 7, 1, 3], 2, [2, 1, 3]),
    ([4, 2, 7, 1, 3], 5, []),
]


@pytest.mark.parametrize("tree_list, val, output_true_list", examples)
def test_searchBST(
    tree_list: list[int | None], val: int, output_true_list: list[int | None]
):
    tree = BinaryTreeNode.from_list_long_iter(
        BinaryTreeNode.transform_short_to_long(short=tree_list)
    )
    output_true = BinaryTreeNode.from_list_long_iter(
        BinaryTreeNode.transform_short_to_long(short=output_true_list)
    )
    output_calc = lc0700.searchBST(root=tree, val=val)
    assert output_calc == output_true
