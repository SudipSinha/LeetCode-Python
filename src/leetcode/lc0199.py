"""Binary Tree Right Side View

Link: https://leetcode.com/problems/binary-tree-right-side-view/

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
"""

from datastructures.binarytree import BinaryTreeNode


def rightSideView(root: BinaryTreeNode | None) -> list[int]:
    return root.rightSideView() if root else []
