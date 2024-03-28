"""Invert Binary Tree

Link: https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree, and return its root.
"""

from copy import deepcopy

from datastructures.binarytree import BinaryTreeNode


def invertTree(root: BinaryTreeNode | None) -> BinaryTreeNode | None:
    if root:
        inverted = deepcopy(root)
        inverted.invert()
    else:
        inverted = None
    return inverted
