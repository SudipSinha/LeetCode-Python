"""Diameter of Binary Tree

Link: https://leetcode.com/problems/diameter-of-binary-tree/

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""

from datastructures.binarytree import BinaryTreeNode


def diameterOfBinaryTree(root: BinaryTreeNode | None) -> int:
    return root.diameter() if root else 0
