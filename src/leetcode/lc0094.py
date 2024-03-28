"""Binary Tree Inorder Traversal

Link: https://leetcode.com/problems/binary-tree-inorder-traversal/

Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""

from datastructures.binarytree import BinaryTreeNode


def inorderTraversal_recur(root: BinaryTreeNode | None) -> list[int]:
    return root.inorderTraversal_recur() if root else []
