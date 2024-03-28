"""Binary Tree Postorder Traversal

Link: https://leetcode.com/problems/binary-tree-postorder-traversal/

Given the root of a binary tree, return the postorder traversal of its nodes' values.
"""

from datastructures.binarytree import BinaryTreeNode


def postorderTraversal_recur(root: BinaryTreeNode | None) -> list[int]:
    return root.postorderTraversal_recur() if root else []
