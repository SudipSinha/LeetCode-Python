"""Maximum Depth of Binary Tree

Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

from datastructures.binarytree import BinaryTreeNode


def maxDepth(root: BinaryTreeNode | None) -> int:
    if not root:
        return 0
    return root.maxDepth()
