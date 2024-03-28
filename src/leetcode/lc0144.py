"""Binary Tree Preorder Traversal

Link: https://leetcode.com/problems/binary-tree-preorder-traversal/

Given the root of a binary tree, return the preorder traversal of its nodes' values.
"""

from datastructures.binarytree import BinaryTreeNode


def preorderTraversal_recur(root: BinaryTreeNode | None) -> list[int]:
    return root.preorderTraversal_recur() if root else []
