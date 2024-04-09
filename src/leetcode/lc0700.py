"""Search in a Binary Search Tree

Link: https://leetcode.com/problems/search-in-a-binary-search-tree/

You are given the `root` of a binary search tree (BST) and an integer `val`.

Find the node in the BST that the node's value equals `val` and return the subtree rooted with that node. If such a node does not exist, return `null`.
"""

from datastructures.binarytree import BinaryTreeNode


def searchBST(root: BinaryTreeNode | None, val: int) -> BinaryTreeNode | None:
    if not root:
        return None
    return root.searchBST(val=val)
