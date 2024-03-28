"""Diameter of Binary Tree

Link: https://leetcode.com/problems/diameter-of-binary-tree/

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""

from datastructures.binarytree import BinaryTreeNode


def diameterOfBinaryTree(root: BinaryTreeNode | None) -> int:
    return root.diameter() if root else 0


# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# def diameterOfBinaryTree(root: TreeNode | None) -> int:
#     """Diameter = maxdepth(left) + maxdepth(right).
#     Maximum depth is given by DFS.
#     Time complexity: O(n), space complexity: O(1), where `n` is the number of nodes.
#     """
#     diameter__max = 0

#     def _maxdepth_dfs(root: TreeNode | None = root) -> int:
#         nonlocal diameter__max
#         if not root:
#             return 0
#         maxdepth_left = _maxdepth_dfs(root=root.left)
#         maxdepth_right = _maxdepth_dfs(root=root.right)
#         diameter_cur = maxdepth_left + maxdepth_right
#         diameter__max = max(diameter_cur, diameter__max)
#         return 1 + max(maxdepth_left, maxdepth_right)

#     _maxdepth_dfs()
#     return diameter__max
