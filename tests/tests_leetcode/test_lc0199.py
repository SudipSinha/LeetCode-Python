import pytest
from datastructures.binarytree import BinaryTreeNode
from leetcode import lc0199

examples = [
    ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
    ([1, None, 3], [1, 3]),
    ([], []),
]


@pytest.mark.parametrize("tree_list, output_true", examples)
def test_rightSideView(tree_list: list[int | None], output_true: list[int]):
    tree = BinaryTreeNode.from_list_long_iter(
        BinaryTreeNode.transform_short_to_long(short=tree_list)
    )
    output_calc = lc0199.rightSideView(root=tree)
    assert output_calc == output_true
